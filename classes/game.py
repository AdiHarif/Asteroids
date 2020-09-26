import pygame
from classes.player import Player
from classes.enemy import Enemy
import sys

class Game:
	clock = pygame.time.Clock()
	FPS = 60
	# class AlreadyInitialized():
	# 	pass

	# instance = None

	# @staticmethod
	# def get_instance():
	# 	if 

	def __init__(self, window_size, caption, bg_color):

		# if not Game.instance is None:
		# 	raise AlreadyInitialized
		self.enemies = []
		self.window_size = window_size
		pygame.display.set_caption(caption)
		self.screen = pygame.display.set_mode(window_size, 0, 32)
		self.bg_color = bg_color
		self.screen.fill(bg_color)
		self.player = Player(self)

	def main_loop(self):
		while True:
			self.handle_events()
			self.handle_keys()
			self.player.update_position()
			for enemy in self.enemies:
				enemy.update_position()

			self.draw_all()
			self.clock.tick(Game.FPS)

	def draw_all(self):
		self.screen.fill(self.bg_color)
		self.player.draw(self.screen)
		for enemy in self.enemies:
			enemy.draw(self.screen)
		pygame.display.update()
	
	def handle_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.exit()

	def handle_keys(self):
		keys_down = pygame.key.get_pressed()
		if keys_down[pygame.K_w]:
			self.player.accelerate(0.2)
		if keys_down[pygame.K_a]:
			self.player.rotate(-1)
		if keys_down[pygame.K_s]:
			self.player.accelerate(-0.2)
		if keys_down[pygame.K_d]:
			self.player.rotate(1)
		if keys_down[pygame.K_RETURN]:
			self.enemies.append(Enemy(self))


	def exit(self):
		pygame.quit()
		sys.exit()