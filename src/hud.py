
import pygame

import os
from math import floor


class HUD:
    HEART_SPRITE_PATH = os.path.join('assets', 'hud', 'heart.png')

    def __init__(self):
        self.heart_pic = pygame.image.load(HUD.HEART_SPRITE_PATH)
        self.heart_pic = pygame.transform.scale(self.heart_pic, [40, 40])
        self.score = 0
        self.time = 0
        self.hp = 3

    def increase_score(self, value):
        self.score += floor(value)

    def set_hp(self, hp):
        self.hp = hp

    def draw(self, window):
        for i in range(self.hp):
            window.blit(self.heart_pic, [600 - ((1+i)*self.heart_pic.get_size()[0]), 0])
