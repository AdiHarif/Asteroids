
import asyncio
import pygame

from src.game import Game


pygame.init()

# parametears
WINDOW_SIZE = [600, 600]


async def main():
    game = Game(WINDOW_SIZE, 'Asteroids')
    await game.start()

asyncio.run(main())
