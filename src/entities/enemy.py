
import os
from src.entities.entity import Entity
from random import randint, uniform
from math import cos, sin, radians


class Enemy(Entity):
    SPRITE_PATH = os.path.join('assets', 'enemies', 'me_gusta_32x32.png')
    MIN_VELOCITY = 0.5
    MAX_VELOCITY = 2
    NEW_ENEMIES_COUNT_ON_DEATH = 2

    def __init__(self, scale, start_pos, speed_angle):
        super().__init__(Enemy.SPRITE_PATH, start_pos, [0, 0], -90, scale)
        self.DIE_THRESHOLD = 0.5
        self.scale = scale
        self.rotation_angle = uniform(0, 10)
        start_vel = uniform(Enemy.MIN_VELOCITY, Enemy.MAX_VELOCITY)
        self.speed = [start_vel*cos(radians(speed_angle)),
                      start_vel*sin(radians(speed_angle))]
        self.base_score = 10

    def update(self, game):
        if (self.is_out_of_bounds(game.window_size)):
            self.die(game, True)
            return
        super().update()

    def die(self, game, instant_death=False):
        new_enemies = []
        if (not instant_death):
            if (self.scale >= self.DIE_THRESHOLD):
                for i in range(self.NEW_ENEMIES_COUNT_ON_DEATH):
                    enemy = Enemy(self.scale/2, self.pos, randint(0, 360))
                    new_enemies.append(enemy)

        game.enemies.remove(self)
        game.enemies.extend(new_enemies)
        del self
