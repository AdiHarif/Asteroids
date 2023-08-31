
import os
from datetime import datetime
from math import atan2, pi, cos

from src.entities.entity import Entity
from src.entities.shot import Shot
from src.sfx_manager import SFXManager


class Player(Entity):
    SPRITE_PATH = os.path.join('assets', 'players', 'spaceship2.png')
    STARTING_POSITION = [200, 200]
    MAX_VELOCITY = 4
    FIRE_RATE = 4  # in shots per second
    SHOTS_DELTA = (1/FIRE_RATE)*(10**6)
    HIT_INVINCIBILITY = 2

    def __init__(self):
        super().__init__(Player.SPRITE_PATH, Player.STARTING_POSITION, [0, 0])
        self.last_shot = None
        self.hp = 3
        self.last_hit = None
        self.invincible = False
        self.opacity = 255

    def take_hit(self):
        if self.invincible:
            return
        self.last_hit = datetime.now()
        SFXManager.play(SFXManager.EXPLOSION)
        self.hp -= 1
        self.invincible = True

    def is_dead(self):
        return self.hp <= 0

    def fire(self):
        time = datetime.now()
        if self.last_shot is None or (time-self.last_shot).microseconds > Player.SHOTS_DELTA:
            self.last_shot = datetime.now()
            SFXManager.play(SFXManager.SHOT)
            return Shot.fire(self.pos, self.rotation)
        return None

    def set_speed(self, vector):
        for i in range(2):
            self.speed[i] = vector[i]

    def decay_speed(self):
        for i in range(2):
            if self.speed[i] > 0:
                self.speed[i] -= 0.15
                self.speed[i] = max(0, self.speed[i])
            elif self.speed[i] < 0:
                self.speed[i] += 0.15
                self.speed[i] = min(0, self.speed[i])

    def point_to(self, target):
        dx = (target[0] - self.pos[0])
        dy = (target[1] - self.pos[1])
        self.rotation = atan2(dy, dx) * (180/pi)

    def update(self):
        super().update()
        self.decay_speed()
        if self.invincible:
            time_from_hit = (datetime.now()-self.last_hit)
            self.opacity = (((cos(time_from_hit.microseconds/0.5e5) + 1)/2) * 200) + 55
            self.invincible = time_from_hit.seconds < Player.HIT_INVINCIBILITY
        else:
            self.opacity = 255
        self.actual_pic.set_alpha(self.opacity)
