import pygame
from math import floor


class HUD:
    def __init__(self):
        self.score = 0
        self.time = 0

    def increase_score(self, value):
        self.score += floor(value)


class Text:
    def __init__(self, text, font, size, x, y, color, bg_color=None):
        self.size = size
        self.color = color
        self.bg_color = bg_color
        self.pos = [x, y]
        self.font = pygame.font.Font(font, size)
        self.text = self.font.render(text, True, color, bg_color)
        self.rect = self.text.get_rect()

    def update_text(self, new_text):
        self.text = self.font.render(new_text, True, self.color, self.bg_color)

    def draw(self, window):
        window.blit(self.text, self.rect)
