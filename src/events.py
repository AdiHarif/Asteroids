
import pygame

def process_events(game):
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.QUIT:
            game.exit()
        if e.type == pygame.KEYUP:
            if e.key == pygame.K_ESCAPE:
                game.toggle_pause()
