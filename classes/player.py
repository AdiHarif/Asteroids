
from classes.sprite_sheet import SpriteSheet
from classes.entity import Entity
from classes.shot import Shot
import pygame
from math import cos, sin, pi, radians, sqrt

class Player(Entity):	
	SPRITE_PATH  = 'assets\\players\\spaceship0.png'
	STARTING_POSITION = [0, 0]
	STARTING_ROTATION = 0
	MAX_VELOCITY = 4


	def __init__(self):
		super().__init__(Player.SPRITE_PATH, Player.STARTING_POSITION)

	def fire(self):
		center = [self.pos[i] +(self.source_size[i]/2) for i in range(2)]
		return Shot.fire(center, self.rotation)


	def accelerate(self, magnitude):
		self.speed[0] += magnitude*cos(radians(self.rotation)) 
		self.speed[1] += magnitude*sin(radians(self.rotation)) 

		norm = sqrt((self.speed[0]**2)+(self.speed[1]**2) )
		if norm > Player.MAX_VELOCITY:
			self.speed = [(dim/norm)*Player.MAX_VELOCITY for dim in self.speed]
	