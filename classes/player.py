
from classes.sprite_sheet import SpriteSheet
from classes.entity import Entity
import pygame

class Player(Entity):	
	SPRITE_PATH  = 'assets\\players\\spaceship0.png'
	STARTING_POSITION = [0, 0]
	STARTING_ROTATION = 0


	def __init__(self, game):
		super().__init__(game, Player.SPRITE_PATH, Player.STARTING_POSITION)

