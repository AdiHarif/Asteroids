
from classes.sprite_sheet import SpriteSheet
from classes.entity import Entity
from classes.shot import Shot

from datetime import datetime
import pygame
from math import cos, sin, pi, radians, sqrt

class Player(Entity):	
	SPRITE_PATH  = 'assets\\players\\spaceship1.png'
	STARTING_POSITION = [0, 0]
	STARTING_ROTATION = 0
	MAX_VELOCITY = 4
	FIRE_RATE = 4 # in shots per second
	SHOTS_DELTA = (1/FIRE_RATE)*(10**6)


	def __init__(self):
		super().__init__(Player.SPRITE_PATH, Player.STARTING_POSITION)
		self.last_shot = None

	def fire(self):
		time = datetime.now()
		if self.last_shot is None or (time-self.last_shot).microseconds > Player.SHOTS_DELTA:
			self.last_shot = datetime.now()
			center = [self.pos[i] +(self.source_size[i]/2) for i in range(2)]
			return Shot.fire(center, self.rotation)
		return None

	def accelerate(self, magnitude):
		self.speed[0] += magnitude*cos(radians(self.rotation)) 
		self.speed[1] += magnitude*sin(radians(self.rotation)) 

		norm = sqrt((self.speed[0]**2)+(self.speed[1]**2) )
		if norm > Player.MAX_VELOCITY:
			self.speed = [(dim/norm)*Player.MAX_VELOCITY for dim in self.speed]
	