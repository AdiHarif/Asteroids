
import pygame

def process_events(game):
    events = pygame.event.get(eventtype=pygame.KEYUP)
    for e in events:
        if e.key == pygame.K_ESCAPE:
            game.toggle_pause()
