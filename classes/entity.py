
from classes.sprite_sheet import SpriteSheet
import pygame
from math import cos, sin, pi, radians, sqrt

class Entity:
	MAX_VELOCITY = 4
	def __init__(self, game, sprite_path, start_pos, start_speed=[0,0], start_rotation=-90):
		#self.sprite_sheet = SpriteSheet(sprite_path, 1, 1)
		self.game = game
		self.pic = pygame.image.load(sprite_path)
		self.pic_size = self.pic.get_size()
		self.pos = start_pos
		self.rotation = start_rotation
		self.speed = start_speed

	def draw(self, window):
		rotated_pic = pygame.transform.rotate(self.pic, -(self.rotation+90) )
		window.blit(rotated_pic, self.pos)
		#self.sprite_sheet.draw(window, self.pos)

	# def move(self, vector):
	# 	# moves ads the input vector to the players position. returns a copy of the new position
	# 	for i in range(2):
	# 		self.pos[i] += vector[i]

	# 	return self.pos[:]

	def update_position(self):
		for i in range(2):
			self.pos[i] += self.speed[i]
		
		if(self.pos[0] <= 0): # hit left wall
			self.pos[0] = 0
			self.speed[0] *= -1
		
		if(self.pos[0] >= (self.game.window_size[0] - self.pic_size[0] )): # hit right wall
			self.pos[0] = self.game.window_size[0] - self.pic_size[0]
			self.speed[0] *= -1
		
		if(self.pos[1] <= 0): # hit upper wall
			self.pos[1] = 0
			self.speed[1] *= -1
		
		if(self.pos[1] >= self.game.window_size[1] - self.pic_size[1]): # hit bottom wall
			self.pos[1] = self.game.window_size[1] - self.pic_size[1]
			self.speed[1] *= -1
			

	def rotate(self, angle):
		self.rotation += angle

	# def accelerate(self, acc_vec):
	# 	for i in range(2):
	# 		self.speed[i] += self.acc_vec[i]

	def accelerate(self, magnitude):
		self.speed[0] += magnitude*cos(radians(self.rotation)) 
		self.speed[1] += magnitude*sin(radians(self.rotation)) 

		norm = sqrt((self.speed[0]**2)+(self.speed[1]**2) )
		if norm > Entity.MAX_VELOCITY:
			self.speed = [(dim/norm)*Entity.MAX_VELOCITY for dim in self.speed]
	

	# def set_position(self, new_pos):
	# 	# set the players position to be the given position
	# 	self.pos = new_pos[:]