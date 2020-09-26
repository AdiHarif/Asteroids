
from classes.sprite_sheet import SpriteSheet
from classes.entity import Entity
import pygame
from random import randint, uniform
from math import cos, sin, radians

class Enemy(Entity):	
	SPRITE_PATH  = 'assets\\enemies\\me_gusta_32x32.png'
	MIN_VELOCITY = 0.1

	def __init__(self, game):
		super().__init__(game, self.SPRITE_PATH, [0,0])

		wall = randint(0, 3)
		angle = uniform(0, 360)
		offset = uniform(0, game.window_size[wall%2] - self.pic_size[wall%2])
		self.starting_position = [0, 0]
		if(wall==0):
			self.starting_position[0] += offset
		if(wall==1):
			self.starting_position[0] += game.window_size[0]-self.pic_size[0]
			self.starting_position[1] += offset
		if(wall==2):
			self.starting_position[0] += offset
			self.starting_position[1] += game.window_size[1]-self.pic_size[1]
		if(wall==3):
			self.starting_position[1] += offset
		start_vel = uniform(self.MIN_VELOCITY, self.MAX_VELOCITY)
		self.start_speed = (start_vel*cos(radians(angle)), start_vel*sin(radians(angle)))
		

