import pygame
import sys
import os

from classes.player import Player
from classes.game import Game
from classes.sprite_sheet import SpriteSheet

pygame.init()

# parameters
WINDOW_SIZE = [600, 600]

# colors
pink = [255, 192, 203]
eggplant = [57, 5, 55]




game = Game(WINDOW_SIZE, 'Asteroids', eggplant)
game.main_loop()
