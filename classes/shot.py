
from math import sin, cos, radians
import pygame
from classes.entity import Entity

class Shot(Entity):
    SPRITE_PATH = 'assets\\shots\\shot1.png'
    START_OFFSET = 32
    VELOCITY = 6
    COLOR = (0, 255, 255)
    SCALE = 0.5

    def __init__(self, player_center, direction):
        start_pos =  [player_center[0] + (Shot.START_OFFSET * cos(radians(direction))) , player_center[1] + (Shot.START_OFFSET * sin(radians(direction)))]
        start_speed = [Shot.VELOCITY*cos(radians(direction)), Shot.VELOCITY*sin(radians(direction))]
        super().__init__(Shot.SPRITE_PATH, start_pos, start_speed, direction, Shot.SCALE)
        self.pos = [self.pos[i] - (self.actual_size[i]/2) for  i in range(2)]

    @staticmethod
    def fire(player_center, direction):
        shot = Shot(player_center, direction)
        return shot


