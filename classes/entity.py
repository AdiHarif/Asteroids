
from classes.sprite_sheet import SpriteSheet
import pygame
from math import cos, sin, pi, radians, sqrt

class Entity:
	MAX_VELOCITY = 4
	def __init__(self, sprite_path, start_pos, start_rotation=-90, start_speed=[0,0]):
		self.pic = pygame.image.load(sprite_path)
		self.pic_size = self.pic.get_size()
		self.rotation = start_rotation
		self.pos = start_pos
		self.rotation = start_rotation
		self.speed = start_speed
		self.rotated_pic = pygame.transform.rotate(self.pic, -(self.rotation+90) )
		self.rotated_pic_size = self.rotated_pic.get_size()
		self.actual_pos = [ self.pos[i] + ((self.pic_size[i]-self.rotated_pic_size[i])/2) for i in range(2)]

	def draw(self, window):
		window.blit(self.rotated_pic, self.actual_pos)
		#self.sprite_sheet.draw(window, self.pos)

	# def move(self, vector):
	# 	# moves ads the input vector to the players position. returns a copy of the new position
	# 	for i in range(2):
	# 		self.pos[i] += vector[i]

	# 	return self.pos[:]

	def update(self):
		for i in range(2):
			self.pos[i] += self.speed[i]
		
		self.rotated_pic = pygame.transform.rotate(self.pic, -(self.rotation+90) )
		self.rotated_pic_size = self.rotated_pic.get_size()
		self.actual_pos = [ self.pos[i] + ((self.pic_size[i]-self.rotated_pic_size[i])/2) for i in range(2)]


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

	
	def bounce_off_walls(self, window_size):
		if(self.pos[0] <= 0): # hit left wall
			self.pos[0] = 0
			self.speed[0] *= -1
		
		if(self.pos[0] >= (window_size[0] - self.pic_size[0] )): # hit right wall
			self.pos[0] = window_size[0] - self.pic_size[0]
			self.speed[0] *= -1
		
		if(self.pos[1] <= 0): # hit upper wall
			self.pos[1] = 0
			self.speed[1] *= -1
		
		if(self.pos[1] >= window_size[1] - self.pic_size[1]): # hit bottom wall
			self.pos[1] = window_size[1] - self.pic_size[1]
			self.speed[1] *= -1
			
	def is_out_of_bounds(self, window_size):
		return self.pos[0] <= 0 or self.pos[1] <= 0 or window_size[0]<self.pos[0]+self.pic_size[0] or window_size[1]<self.pos[1]+self.pic_size[1]
