
import pygame

from random import randint, random, uniform
from math import sin, cos, radians

from src.entities.entity import Entity

class Particle(Entity):
    DECAY_FACTOR = 0.92
    def __init__(self,  start_pos, start_speed, color, size, rotation_speed):
        self.source_pic = pygame.surface.Surface((size, size))
        self.color = color
        self.size = size
        self.rotation_speed = rotation_speed
        self.source_pic.fill(color)
        super().__init__(start_pos, start_speed)
        self.liveness = 1

    def update(self):
        super().update()
        self.liveness *= Particle.DECAY_FACTOR
        self.speed = [axis_speed * Particle.DECAY_FACTOR for axis_speed in self.speed]
        self.color = [int(color * Particle.DECAY_FACTOR) for color in self.color]
        self.size *= Particle.DECAY_FACTOR
        self.source_pic = pygame.transform.rotozoom(self.source_pic, 0, Particle.DECAY_FACTOR)
        self.source_pic.fill(self.color)
        self.rotate(self.rotation_speed)

    def is_dead(self):
        return self.liveness < 0.1

def spawn_explosion(pos):
    full_yellow = [235, 174, 52]
    full_red = [235, 61, 26]
    particles = []
    for i in range(randint(10,20)):
        angle = radians(randint(0, 360))
        color = []
        for i in range(3):
            factor = random()
            color.append(full_red[i] * factor + full_yellow[i] * (1 - factor))

        starting_velocity = 2.5 * uniform(0.6, 1.2)
        praticle_speed = [cos(angle) * starting_velocity, sin(angle) * starting_velocity]
        particles.append(Particle(pos, praticle_speed, color, randint(5, 8), uniform(-5, 5)))
    return particles