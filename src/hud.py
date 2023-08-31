
import pygame

import os
from math import floor

from src.util_classes.text import Text

white = [255, 255, 255]

class HUD:
    HEART_SPRITE_PATH = os.path.join('assets', 'hud', 'heart.png')

    def __init__(self):
        self.heart_pic = pygame.image.load(HUD.HEART_SPRITE_PATH)
        self.heart_pic = pygame.transform.scale(self.heart_pic, [40, 40])
        self.score = 0
        self.score_text = Text(
            "SCORE: " + str(self.score), 'freesansbold.ttf', 32, 0, 0, white)
        self.time = 0
        self.hp = 3

    def increase_score(self, value):
        self.set_score(self.score + floor(value))

    def set_hp(self, hp):
        self.hp = hp

    def set_score(self, score):
        self.score = score
        self.score_text.update_text("SCORE: " + str(self.score))

    def draw(self, window):
        for i in range(self.hp):
            window.blit(self.heart_pic, [600 - ((1+i)*self.heart_pic.get_size()[0]), 0])
        self.score_text.draw(window)
