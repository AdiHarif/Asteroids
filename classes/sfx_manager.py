
import os

import pygame

class SFXManager:

    instance = None

    EXPLOSION = 'explosion'
    SHOT = 'shot'
    EFFECTS_LIST = [EXPLOSION, SHOT]

    def __init__(self):
        self.effects = {}
        for effect in SFXManager.EFFECTS_LIST:
            path = os.path.join('assets', 'sfx', f'{effect}.wav')
            sound = pygame.mixer.Sound(file=path)
            sound.set_volume(0.1)
            self.effects[effect] = sound

    @staticmethod
    def init():
        SFXManager.instance = SFXManager()

    @staticmethod
    def play(name):
        SFXManager.instance.effects[name].play()

