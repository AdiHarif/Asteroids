import pygame
from classes.player import Player
import sys

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
			self.handle_events()
			self.handle_keys()
		
			self.draw_all()

	def draw_all(self):
		self.screen.fill(self.bg_color)
		self.player.draw(self.screen)

		pygame.display.update()
	
	def handle_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.exit()

	def handle_keys(self):
		keys_down = pygame.key.get_pressed()
		if keys_down[pygame.K_w]:
			self.player.move([0, -1])
		if keys_down[pygame.K_a]:
			self.player.move([-1, 0])
		if keys_down[pygame.K_s]:
			self.player.move([0, 1])
		if keys_down[pygame.K_d]:
			self.player.move([1, 0])



	def exit(self):
		pygame.quit()
		sys.exit()