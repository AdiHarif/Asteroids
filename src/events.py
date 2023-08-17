
import pygame

from src.sfx_manager import SFXManager

COLLISIONEVENT = pygame.event.custom_type()

async def process_events(game):
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.QUIT:
            game.exit()
        if e.type == pygame.KEYUP:
            if e.key == pygame.K_ESCAPE:
                game.toggle_pause()
        if e.type == COLLISIONEVENT:
            if e.dict["player_collision"]:
                await game.end()
            else:
                SFXManager.play(SFXManager.EXPLOSION)

                shot = e.dict["shot"]
                if shot in game.shots:
                    game.shots.remove(shot)
                e.dict["shot"].die()

                enemy = e.dict["enemy"]
                game.hud.increase_score(enemy.base_score * (1/enemy.scale))
                game.update_score()
                enemy.die(game)
