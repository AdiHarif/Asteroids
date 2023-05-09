
import pygame

class Entity:
	OUT_OF_BOUNDS_SPAWN_OFFSET = 50
	OUT_OF_BOUNDS_DEATH_OFFSET = 100
	
	def __init__(self, sprite_path, start_pos, start_speed, start_rotation=-90, scale=1):
		self.source_pic = pygame.image.load(sprite_path)
		self.source_size = self.source_pic.get_size()
		self.pos = start_pos[:]
		self.rotation = start_rotation
		self.scale = scale
		self.speed = start_speed[:]

		self.actual_pic = pygame.transform.rotozoom(self.source_pic, -(self.rotation+90), self.scale )
		self.actual_size = self.actual_pic.get_size()
		self.actual_pos = [ self.pos[i] + ((self.source_size[i]-self.actual_size[i])/2) for i in range(2)]

	def draw(self, window):
		window.blit(self.actual_pic, self.actual_pos)

	def update(self):
		for i in range(2):
			self.pos[i] += self.speed[i]

		self.actual_pic = pygame.transform.rotozoom(self.source_pic, -(self.rotation+90), self.scale )
		self.actual_size = self.actual_pic.get_size()
		self.actual_pos = [ self.pos[i] + ((self.source_size[i]-self.actual_size[i])/2) for i in range(2)]

	def rotate(self, angle):
		self.rotation += angle

	def bounce_off_walls(self, window_size):
		if(self.pos[0] <= 0): # hit left wall
			self.pos[0] = 0
			self.speed[0] *= -1

		if(self.pos[0] >= (window_size[0] - self.source_size[0] )): # hit right wall
			self.pos[0] = window_size[0] - self.source_size[0]
			self.speed[0] *= -1

		if(self.pos[1] <= 0): # hit upper wall
			self.pos[1] = 0
			self.speed[1] *= -1

		if(self.pos[1] >= window_size[1] - self.source_size[1]): # hit bottom wall
			self.pos[1] = window_size[1] - self.source_size[1]
			self.speed[1] *= -1

	def is_out_of_bounds(self, window_size):
		return \
			self.pos[0] <= 0 - self.OUT_OF_BOUNDS_DEATH_OFFSET \
			or self.pos[0] >= window_size[0] + self.OUT_OF_BOUNDS_DEATH_OFFSET \
			or self.pos[1] <= 0 - self.OUT_OF_BOUNDS_DEATH_OFFSET \
			or self.pos[1] >= window_size[1] + self.OUT_OF_BOUNDS_DEATH_OFFSET

	def is_colliding(self, ent):
		rect1 = self.source_pic.get_rect().move(self.pos)
		rect2 = ent.source_pic.get_rect().move(ent.pos)
		return rect1.colliderect(rect2)

	def die(self):
		pass

	def keep_in_bounds(self, window_size):
		self.pos[0] = max(0, self.pos[0])
		self.pos[0] = min(window_size[0], self.pos[0])
		self.pos[1] = max(0, self.pos[1])
		self.pos[1] = min(window_size[1], self.pos[1])
