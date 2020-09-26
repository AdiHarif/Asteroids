
from classes.sprite_sheet import SpriteSheet
import pygame

class Player:

	PINK = [255, 192, 203]
	
	SPRITE_PATH  = 'assets\\players\\spaceship0.png'
	STARTING_POSITION = [200, 200]
	def __init__(self):
		pass
		self.sprite_sheet = SpriteSheet(Player.SPRITE_PATH, 1, 1)
		self.pos = Player.STARTING_POSITION
		# self.sprite_sheet = SpriteSheet(self.SPRITE_PATH, 1, 1)
		# self.pos = [(WINDOW_SIZE[0]-self.sprite_sheet.cell_height)/2,(WINDOW_SIZE[1]-self.sprite_sheet.cell_width)/2]
	def draw(self, window):
		self.sprite_sheet.draw(window, self.pos[0], self.pos[1])
		#pygame.draw.rect(window, Player.PINK, (self.pos[0], self.pos[1], 40, 40))

	def move(self, vector):
		# moves ads the input vector to the players position. returns a copy of the new position
		for i in range(2):
			self.pos[i] += vector[i]

		return self.pos[:]

	def set_position(self, new_pos):
		# set the players position to be the given position
		for i in range(2):
			self.pos[i] = new_pos[i]

