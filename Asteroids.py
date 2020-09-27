import pygame
import sys
import os

from classes.game import Game

pygame.init()

# parametears
WINDOW_SIZE = [600, 600]

# colors
pink = [255, 192, 203]
eggplant = [57, 5, 55]




game = Game(WINDOW_SIZE, 'Asteroids', eggplant)
game.main_loop()
d