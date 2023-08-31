
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


class Text:
    def __init__(self, text, font, size, x, y, color, bg_color=None):
        self.size = size
        self.color = color
        self.bg_color = bg_color
        self.pos = [x, y]
        self.font = pygame.font.Font(font, size)
        self.text = self.font.render(text, True, color, bg_color)


    def update_text(self, new_text):
        self.text = self.font.render(new_text, True, self.color, self.bg_color)

    def draw(self, window):
        window.blit(self.text, self.pos)
