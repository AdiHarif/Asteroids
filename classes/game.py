import pygame
from classes.player import Player
from classes.enemy import Enemy
import sys

class Game:
	clock = pygame.time.Clock()
	FPS = 60
	BACKGROUND_PATH = 'assets\\backgrounds\\space1.png'
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
		self.seconds_to_enemy = 3
		self.frames_to_next_enemy = (self.seconds_to_enemy)*(self.FPS)

		self.background_pic  = pygame.image.load(self.BACKGROUND_PATH)

		self.window_size = window_size
		pygame.display.set_caption(caption)
		self.screen = pygame.display.set_mode(window_size, 0, 32)
		self.bg_color = bg_color
		self.screen.fill(bg_color)
		self.player = Player()
		self.shots = []

	def draw_background(self):
		self.screen.blit(self.background_pic, [0, 0])

	def create_enemy(self):
		self.enemies.append(Enemy(self.window_size))

	def increase_difficulty(self):
		self.seconds_to_enemy -= 0.2

	def main_loop(self):
		while True:
			self.frames_to_next_enemy -= 1
			if(self.frames_to_next_enemy == 0):
				self.create_enemy()
				self.frames_to_next_enemy = (self.seconds_to_enemy)*(self.FPS)

			self.handle_events()
			self.handle_keys()
			for enemy in self.enemies:
				enemy.rotate(enemy.rotation_angle)
				enemy.update()
				enemy.bounce_off_walls(self.window_size)
			self.player.update()
			self.player.bounce_off_walls(self.window_size)
			self.update_shots()
			self.draw_all()
			self.clock.tick(Game.FPS)

	def draw_all(self):
		self.draw_background()
		self.player.draw(self.screen)
		for enemy in self.enemies:
			enemy.draw(self.screen)

		for shot in self.shots:
			shot.draw(self.screen)
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
		if keys_down[pygame.K_SPACE]:
			shot = self.player.fire()
			self.shots.append(shot)

	def update_shots(self):
		shots_to_remove =[]
		for shot in self.shots:
			shot.update()
			if shot.is_out_of_bounds(self.window_size):
				shots_to_remove.append(shot)

		for shot in shots_to_remove:
			self.shots.remove(shot)
			del shot
			print('shot destroyed')


	def exit(self):
		pygame.quit()
		sys.exit()