
import os

from math import sin, cos, radians
from classes.entity import Entity


class Shot(Entity):
    SPRITE_PATH = os.path.join('assets', 'shots', 'shot2.png')
    START_OFFSET = 16
    VELOCITY = 6
    COLOR = (0, 255, 255)
    SCALE = 0.3

    def __init__(self, player_center, direction):
        start_pos = [player_center[0] + (Shot.START_OFFSET * cos(radians(
            direction))), player_center[1] + (Shot.START_OFFSET * sin(radians(direction)))]
        start_speed = [
            Shot.VELOCITY*cos(radians(direction)), Shot.VELOCITY*sin(radians(direction))]
        super().__init__(Shot.SPRITE_PATH, start_pos, start_speed, direction, Shot.SCALE)

    @staticmethod
    def fire(player_center, direction):
        shot = Shot(player_center, direction)
        return shot
