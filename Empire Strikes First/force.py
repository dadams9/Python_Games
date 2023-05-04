import pygame as pg
from settings import *
from particles import *

class ForcePlayer:
    def __init__(self, animation_player):
        self.animation_player = animation_player

    def drain(self):
        pass

    def lightning(self):
        pass

    def push(self, player, strength, cost, groups):
        pass

    def heal(self, player, strength, cost, groups):
        if player.energy >= cost and player.health < player.stats['health']:
                player.health += strength
                player.energy -= cost
                if player.health >= player.stats['health']:
                    player.health = player.stats['health']
                self.animation_player.create_particles('heal', player.rect.center + pg.math.Vector2(0, 0), groups)
