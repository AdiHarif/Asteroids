
import pygame

from datetime import datetime

from src.entities.particle import spawn_explosion
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
            game.last_enemy_collision = datetime.now()
            if e.dict["player_collision"]:
                game.player.take_hit()
                if game.player.is_dead():
                    await game.end()
            else:
                SFXManager.play(SFXManager.EXPLOSION)
                game.particles += spawn_explosion(e.dict["position"])

                shot = e.dict["shot"]
                if shot in game.shots:
                    game.shots.remove(shot)
                e.dict["shot"].die()

                enemy = e.dict["enemy"]
                game.hud.increase_score(enemy.base_score * (1/enemy.scale))
                enemy.die(game)
