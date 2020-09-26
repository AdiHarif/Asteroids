import pygame
import classes.player

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

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
				self.exit()
            if event.type == pygame.KEYDOWN:
                pass

    def exit(self):
        pygame.quit()
        sys.exit()