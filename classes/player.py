
from classes.sprite_sheet import SpriteSheet
from classes.entity import Entity
import pygame

class Player(Entity):	
	SPRITE_PATH  = 'assets\\players\\spaceship0.png'
	STARTING_POSITION = [200, 200]
	STARTING_ROTATION = 0


	def __init__(self):
		super().__init__(Player.SPRITE_PATH, Player.STARTING_POSITION, Player.STARTING_ROTATION)
