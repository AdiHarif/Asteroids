import pygame
from classes.player import Player
from classes.enemy import Enemy
from random import randint, uniform
import sys
from classes.sfx_manager import SFXManager


class Game:
	clock = pygame.time.Clock()
	FPS = 60
	BACKGROUND_PATH = 'assets\\backgrounds\\space1.png'
	# class AlreadyInitialized():
	# 	pass

	instance = None

	# @staticmethod
	# def get_instance():
	# 	if 

	def __init__(self, window_size, caption):

		# if not Game.instance is None:
		# 	raise AlreadyInitialized
		self.enemies = []
		self.seconds_to_enemy = 6
		self.frames_to_next_enemy = (self.seconds_to_enemy)*(self.FPS)

		self.background_pic  = pygame.image.load(self.BACKGROUND_PATH)

		self.window_size = window_size
		self.caption = caption
		pygame.display.set_caption(caption)
		self.screen = pygame.display.set_mode(window_size, 0, 32)
		self.player = Player()
		self.shots = []
		SFXManager.init()

	@staticmethod
	def start(window_size, caption):
		Game.instance = Game(window_size, caption)
		Game.instance.main_loop()

	@staticmethod
	def stop():
		del Game.instance.player
		del Game.instance
		Game.instance = None
	
	@staticmethod
	def restart(window_size, caption):
		Game.stop()
		Game.start(window_size, caption)

	@staticmethod
	def draw_background():
		game = Game.instance
		game.screen.blit(game.background_pic, [0, 0])

	@staticmethod
	def create_enemy(is_new, pos):
		game = Game.instance
		if(is_new):
			wall = randint(0, 3)
			offset = uniform(0, game.window_size[wall%2]) #- self.source_size[wall%2])
			if(wall==0):
				pos[0] += offset
			if(wall==1):
				pos[0] += game.window_size[0]#-self.source_size[0]
				pos[1] += offset
			if(wall==2):
				pos[0] += offset
				pos[1] += game.window_size[1]#-self.source_size[1]
			if(wall==3):
				pos[1] += offset

		scale = uniform(0.5, 3)
		game.enemies.append( Enemy(scale, pos) )

	@staticmethod
	def increase_difficulty():
		Game.instance.seconds_to_enemy -= 0.2

	@staticmethod
	def main_loop():
		game = Game.instance
		while True:
			game.frames_to_next_enemy -= 1
			if(game.frames_to_next_enemy == 0):
				game.create_enemy(True, [0, 0])
				game.frames_to_next_enemy = (game.seconds_to_enemy)*(game.FPS)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					game.exit()
					return
			game.handle_keys()
			for enemy in game.enemies:
				enemy.rotate(enemy.rotation_angle)
				enemy.update()
				enemy.bounce_off_walls(game.window_size)
			game.player.update()
			game.player.bounce_off_walls(game.window_size)
			game.update_shots()
			game.check_and_handle_collisions()
			game.draw_all()
			game.clock.tick(Game.FPS)

	@staticmethod
	def draw_all():
		game = Game.instance
		game.draw_background()
		game.player.draw(game.screen)
		for enemy in game.enemies:
			enemy.draw(game.screen)

		for shot in game.shots:
			shot.draw(game.screen)
		pygame.display.update()
	
	# @staticmethod
	# def handle_events():
	# 	game = Game.instance
	# 	for event in pygame.event.get():
	# 		if event.type == pygame.QUIT:
	# 			game.exit()

	@staticmethod
	def handle_keys():
		game = Game.instance
		keys_down = pygame.key.get_pressed()
		if keys_down[pygame.K_w]:
			game.player.accelerate(0.2)
		if keys_down[pygame.K_a]:
			game.player.rotate(-5)
		if keys_down[pygame.K_s]:
			game.player.accelerate(-0.2)
		if keys_down[pygame.K_d]:
			game.player.rotate(5)
		if keys_down[pygame.K_SPACE]:
			shot = game.player.fire()
			if not shot is None:
				game.shots.append(shot)

	@staticmethod
	def update_shots():
		game = Game.instance
		shots_to_remove =[]
		for shot in game.shots:
			shot.update()
			if shot.is_out_of_bounds(game.window_size):
				shots_to_remove.append(shot)

		for shot in shots_to_remove:
			game.shots.remove(shot)
			del shot


	@staticmethod
	def exit():
		game = Game.instance
		pygame.quit()
		sys.exit()

	@staticmethod
	def check_and_handle_collisions():
		game = Game.instance
		for enemy in game.enemies:
			if game.player.is_colliding(enemy):
				game.restart(game.window_size, game.caption)
				return

		shots_to_remove = []
		enemies_to_remove =[]
		for shot in game.shots:
			for enemy in game.enemies:
				if shot not in shots_to_remove and enemy not in enemies_to_remove and shot.is_colliding(enemy):
					shots_to_remove.append(shot)
					enemies_to_remove.append(enemy)
					SFXManager.play(SFXManager.EXPLOSION)
		
		for shot in shots_to_remove:
			shot.die()
			game.shots.remove(shot)
			del shot

		for enemy in enemies_to_remove:
			new_enemies = enemy.die()
			print("enemies before removal: " + str(game.enemies))
			game.enemies.remove(enemy)
			print("enemies after removal: " + str(game.enemies))
			game.enemies.extend(new_enemies)
			print("enemies after extend: " + str(game.enemies))
			del enemy

	