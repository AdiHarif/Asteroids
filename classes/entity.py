
from classes.sprite_sheet import SpriteSheet
import pygame

class Entity:	
	def __init__(self, sprite_path, start_pos, start_rotation=0, start_speed=[0,0]):
		self.sprite_sheet = SpriteSheet(sprite_path, 1, 1)
		self.pos = start_pos
		self.rotation = start_rotation
		self.speed = start_speed

	def draw(self, window):
		self.sprite_sheet.draw(window, self.pos)

	# def move(self, vector):
	# 	# moves ads the input vector to the players position. returns a copy of the new position
	# 	for i in range(2):
	# 		self.pos[i] += vector[i]

	# 	return self.pos[:]

	def update_position(self):
		for i in range(2):
			self.pos[i] += self.speed[i]

	def rotate(self, angle):
		self.angle += angle

	def accelerate(self, acc_vec):
		for i in range(2):
			self.speed[i] += self.acc_vec[i]

	# def set_position(self, new_pos):
	# 	# set the players position to be the given position
	# 	self.pos = new_pos[:]

	

	