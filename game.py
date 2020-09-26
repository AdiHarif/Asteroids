import pygame
import sys
import os

pygame.init()

# parameters

# colors
pink = [255, 192, 203]
eggplant = [57, 5, 55]

WINDOW_SIZE = [600, 600]

class Game:

	# class AlreadyInitialized():
	# 	pass

	# instance = None

	# @staticmethod
	# def get_instance():
	# 	if 

	def __init__(self, window_size, caption, bg_color):

		# if not Game.instance is None:
		# 	raise AlreadyInitialized

		self.window_size = window_size
		pygame.display.set_caption(caption)
		self.screen = pygame.display.set_mode(window_size, 0, 32)
		self.bg_color = bg_color
		self.screen.fill(bg_color)
		self.player = Player()

	def main_loop(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
		
			self.draw_all()

	def draw_all(self):
		self.screen.fill(self.bg_color)
		self.player.draw(self.screen)

		pygame.display.update()


class SpriteSheet:
	def __init__(self, file_name, rows_count, cols_count):
		print(file_name)
		self.sheet = pygame.image.load(file_name)
		self.rows_count = rows_count
		self.cols_count = cols_count
		self.rect = self.sheet.get_rect()
		w = self.cell_width = self.rect.width / cols_count
		h = self.cell_height = self.rect.height / rows_count
		# calc cell area
		# self.cells_areas = [ ((i%cols)*w, (i/cols)*h, w, h) for i in range(self.totalCellCount) ]
		self.cells_areas = [[ (i*h, j*w , h, w) for j in range(cols_count)] for i in range(rows_count)]
		# self.cells = []
		# for i in range(self.rows_count*self.cols_count):
		#     self.cells.append(((i%cols_count)*w, (i//cols_count)*h, w, h))    
		
	def draw(self, dest_surface, x, y, cell_row=0, cell_col=0):
		dest_surface.blit(self.sheet, (x, y), self.cells_areas[cell_row][cell_col])


class Player:
	SPRITE_PATH  = 'assets\\players\\spaceship0.png'
	pos = [200, 200]
	def __init__(self):
		pass
		# self.sprite_sheet = SpriteSheet(Player.SPRITE_PATH, 1, 1)
		# self.sprite_sheet = SpriteSheet(self.SPRITE_PATH, 1, 1)
		# self.pos = [(WINDOW_SIZE[0]-self.sprite_sheet.cell_height)/2,(WINDOW_SIZE[1]-self.sprite_sheet.cell_width)/2]
	def draw(self, window):
		# self.sprite_sheet.draw(window, self.pos[0], self.pos[1])
		pygame.draw.rect(window, pink, (self.pos[0], self.pos[1], 40, 40))

game = Game(WINDOW_SIZE, 'Asteroids', eggplant)
game.main_loop()
