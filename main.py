
import asyncio
import pygame

from src.game import Game


pygame.init()

# parametears
WINDOW_SIZE = [600, 600]


async def main():
    game = await Game.start(WINDOW_SIZE, 'Asteroids')

asyncio.run(main())
