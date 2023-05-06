
import os

from classes.entity import Entity
from random import randint, uniform
from math import cos, sin, radians

class Enemy(Entity):	
	SPRITE_PATH  = os.path.join('assets', 'enemies', 'me_gusta_32x32.png')
	MIN_VELOCITY = 0.1
	MAX_VELOCITY = 2

	def __init__(self, scale, start_pos):
		super().__init__(Enemy.SPRITE_PATH, start_pos, [0, 0], -90, scale)
		self.DIE_THRESHOLD = 0.5
		self.scale = scale
		self.rotation_angle = uniform(0, 10)
		speed_angle = uniform(0, 360)
		start_vel = uniform(Enemy.MIN_VELOCITY, Enemy.MAX_VELOCITY)
		self.speed = [start_vel*cos(radians(speed_angle)), start_vel*sin(radians(speed_angle))]
		
		self.base_score = 10
		

	def die(self):
		new_enemies = []
		new_enemies_count = 2
		if(self.scale >= self.DIE_THRESHOLD):
			for i in range(new_enemies_count):
				enemy = Enemy(self.scale/2, self.pos)
				new_enemies.append(enemy)

		return new_enemies
