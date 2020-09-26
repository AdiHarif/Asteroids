
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

    