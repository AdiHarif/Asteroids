
import pygame

from classes.game import Game

pygame.init()

# parametears
WINDOW_SIZE = [600, 600]



game = Game.start(WINDOW_SIZE, 'Asteroids')