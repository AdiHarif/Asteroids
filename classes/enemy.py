
from classes.sprite_sheet import SpriteSheet
from classes.entity import Entity
import pygame
from random import randint, uniform
from math import cos, sin, radians

class Enemy(Entity):	
	SPRITE_PATH  = 'assets\\enemies\\me_gusta_32x32.png'
	MIN_VELOCITY = 0.1
	MAX_VELOCITY = 4

	def __init__(self, window_size):
		super().__init__(Enemy.SPRITE_PATH, [0,0])
		
		self.rotation_angle = uniform(0, 10)
		self.seconds_to_rotation = 0.01
		self.frames_to_next_rotation = 60*self.seconds_to_rotation # TODO: change 60 to FPS (consts file)

		wall = randint(0, 3)
		speed_angle = uniform(0, 360)
		offset = uniform(0, window_size[wall%2] - self.source_size[wall%2])
		if(wall==0):
			self.pos[0] += offset
		if(wall==1):
			self.pos[0] += window_size[0]-self.source_size[0]
			self.pos[1] += offset
		if(wall==2):
			self.pos[0] += offset
			self.pos[1] += window_size[1]-self.source_size[1]
		if(wall==3):
			self.pos[1] += offset
		start_vel = uniform(Enemy.MIN_VELOCITY, Enemy.MAX_VELOCITY)
		self.speed = [start_vel*cos(radians(speed_angle)), start_vel*sin(radians(speed_angle))]
		
	def advance_to_rotation(self):
		self.frames_to_next_rotation -= 1
		if(self.frames_to_next_rotation <= 0):
			self.frames_to_next_rotation = 60*self.seconds_to_rotation # TODO: change 60 to FPS
			self.rotate(self.rotation_angle)
