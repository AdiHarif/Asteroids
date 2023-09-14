import os
import asyncio
import pygame
import sys
from random import randint, uniform
from enum import Enum
from datetime import datetime, timedelta

from src.entities.player import Player
from src.entities.enemy import Enemy
from src.hud import HUD
from src.sfx_manager import SFXManager
from src.util_classes.text import Text
import src.events as events


# colors
pink = [255, 192, 203]
eggplant = [57, 5, 55]
white = [255, 255, 255]
black = [0, 0, 0]

class GameStatus(Enum):
    RUNNING = 1
    PAUSED = 2

class Game:
    clock = pygame.time.Clock()
    FPS = 60
    BACKGROUND_PATH = os.path.join('assets', 'backgrounds', 'space1.png')
    INCREASING_DIFFICULTY_FACTOR = 0.95
    SPAWNRATE_UPDATE_INTERVAL = 3

    def toggle_pause(self):
        if self.status == GameStatus.RUNNING:
            self.status = GameStatus.PAUSED
        elif self.status == GameStatus.PAUSED:
            self.status = GameStatus.RUNNING


    def __init__(self, window_size, caption):
        self.caption = caption
        pygame.display.set_caption(caption)
        self.background_pic = pygame.image.load(self.BACKGROUND_PATH)
        self.window_size = window_size
        self.screen = pygame.display.set_mode(window_size, 0, 32)
        SFXManager.init()
        self.hud = HUD()

        self.enemies = None
        self.seconds_to_enemy = None
        self.player = None
        self.shots = None
        self.status = None

    async def start(self):
        self.player = Player()
        self.enemies = []
        self.shots = []
        self.hud.set_score(0)
        self.seconds_to_enemy = 3
        self.last_enemy_spawn = datetime.now()
        self.last_spawn_rate_update = datetime.now()

        self.status = GameStatus.RUNNING
        await self.main_loop()

    async def end(self):
        message = Text(
            "You Lost! Your final score is: " + str(self.hud.score), 'freesansbold.ttf', 20, 0, 550, white)
        message.draw(self.screen)
        message = Text(
            "Press any key to restart.", 'freesansbold.ttf', 20, 0, 575, white)
        message.draw(self.screen)
        pygame.display.update()

        events = []
        while len(events) == 0:
            events = pygame.event.get(eventtype=pygame.KEYDOWN)
            await asyncio.sleep(0.1)

        await self.start()
        return

    async def update(self):
        if (datetime.now() - self.last_enemy_spawn > timedelta(seconds=self.seconds_to_enemy)):
            self.create_enemy()
            self.last_enemy_spawn = datetime.now()

        if (datetime.now() - self.last_spawn_rate_update > timedelta(seconds=self.SPAWNRATE_UPDATE_INTERVAL)):
            self.seconds_to_enemy *= self.INCREASING_DIFFICULTY_FACTOR
            self.last_spawn_rate_update = datetime.now()

        for enemy in self.enemies:
            enemy.rotate(enemy.rotation_angle)
            enemy.update(self)

        self.player.update()
        self.player.keep_in_bounds(self.window_size)
        self.update_shots()
        self.check_collisions()
        self.hud.set_hp(self.player.hp)

    def draw_background(self):
        self.screen.blit(self.background_pic, [0, 0])

    @staticmethod
    def calculate_speed_angle(base, offset):
        return uniform(base - offset, base + offset)

    def calculate_spawn_info(self):
        pos = [0, 0]
        wall = randint(0, 3)
        offset = uniform(0, self.window_size[wall % 2])
        speed_angle_offset = 60
        speed_angle = 0

        if (wall == 0):
            pos[0] += offset
            pos[1] -= Enemy.OUT_OF_BOUNDS_SPAWN_OFFSET
            speed_angle = self.calculate_speed_angle(90, speed_angle_offset)
        if (wall == 1):
            pos[0] += self.window_size[0] + Enemy.OUT_OF_BOUNDS_SPAWN_OFFSET
            pos[1] += offset
            speed_angle = self.calculate_speed_angle(180, speed_angle_offset)
        if (wall == 2):
            pos[0] += offset
            pos[1] += self.window_size[1] + Enemy.OUT_OF_BOUNDS_SPAWN_OFFSET
            speed_angle = self.calculate_speed_angle(270, speed_angle_offset)
        if (wall == 3):
            pos[0] -= Enemy.OUT_OF_BOUNDS_SPAWN_OFFSET
            pos[1] += offset
            speed_angle = self.calculate_speed_angle(0, speed_angle_offset)

        scale = uniform(0.5, 3)
        return speed_angle, pos, scale

    def create_enemy(self):
        speed_angle, pos, scale = self.calculate_spawn_info()
        self.enemies.append(Enemy(scale, pos, speed_angle))

    async def main_loop(self):

        while True:
            # IO handling
            if (self.status != GameStatus.PAUSED):
                self.handle_mouse()
                self.handle_keys()

            # Updating game's state
            if (self.status != GameStatus.PAUSED):
                await self.update()

            # Events handling
            await events.process_events(self)

            # Drawing
            self.draw_all()
            self.clock.tick(Game.FPS)
            await asyncio.sleep(0)

    def draw_all(self):
        self.draw_background()
        self.player.draw(self.screen)

        for enemy in self.enemies:
            enemy.draw(self.screen)

        for shot in self.shots:
            shot.draw(self.screen)

        self.hud.draw(self.screen)
        pygame.display.update()

    def handle_keys(self):
        keys_down = pygame.key.get_pressed()

        player_speed = [0, 0]
        if keys_down[pygame.K_w]:
            player_speed[1] -= 3
        if keys_down[pygame.K_a]:
            player_speed[0] -= 3
        if keys_down[pygame.K_s]:
            player_speed[1] += 3
        if keys_down[pygame.K_d]:
            player_speed[0] += 3

        if (not player_speed[0] == 0) or (not player_speed[1] == 0):
            self.player.set_speed(player_speed)

        if keys_down[pygame.K_SPACE]:
            shot = self.player.fire()
            if not shot is None:
                self.shots.append(shot)

    def handle_mouse(self):
        mouse_pos = pygame.mouse.get_pos()
        self.player.point_to(mouse_pos)

        if pygame.mouse.get_pressed()[0]:
            shot = self.player.fire()
            if not shot is None:
                self.shots.append(shot)

    def update_shots(self):
        for shot in self.shots:
            shot.update()
            if shot.is_out_of_bounds(self.window_size):
                self.shots.remove(shot)
                del shot

    def exit(self):
        pygame.quit()
        sys.exit()

    def check_collisions(self):
        for enemy in self.enemies:
            if self.player.is_colliding(enemy):
                e = pygame.event.Event(events.COLLISIONEVENT, player_collision=True)
                pygame.event.post(e)

        for shot in self.shots:
            for enemy in self.enemies:
                if shot.is_colliding(enemy):
                    e = pygame.event.Event(events.COLLISIONEVENT, player_collision=False, shot=shot, enemy=enemy)
                    pygame.event.post(e)
