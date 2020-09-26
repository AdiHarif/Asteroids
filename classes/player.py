
from classes.sprite_sheet import SpriteSheet
from classes.entity import Entity
from classes.shot import Shot
import pygame
class Player(Entity):	
	SPRITE_PATH  = 'assets\\players\\spaceship0.png'
	STARTING_POSITION = [0, 0]
	STARTING_ROTATION = 0


	def __init__(self, game):
		super().__init__(game, Player.SPRITE_PATH, Player.STARTING_POSITION)

	def fire(self):
		center = [self.pos[i] +(self.pic_size[i]/2) for i in range(2)]
		return Shot.fire(center, self.rotation)