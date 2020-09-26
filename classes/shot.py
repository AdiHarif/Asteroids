
from math import sin, cos, radians
import pygame

class Shot:

    START_OFFSET = 32
    VELOCITY = 6
    COLOR = (0, 255, 255)

    def __init__(self, player_center, direction):
        self.pos = [player_center[0] + (Shot.START_OFFSET * cos(radians(direction))) , player_center[1] + (Shot.START_OFFSET * sin(radians(direction)))]
        self.dir = direction
        self.speed = [Shot.VELOCITY*cos(radians(direction)), Shot.VELOCITY*sin(radians(direction))]

    @staticmethod
    def fire(player_center, direction):
        shot = Shot(player_center, direction)
        return shot


    def update(self):
        self.pos = [self.pos[i] + self.speed[i] for i in range(2)]

    def draw(self, window):
        rect = pygame.Rect(self.pos, (1,1))
        pygame.draw.rect(window, Shot.COLOR, rect)


