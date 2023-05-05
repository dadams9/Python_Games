import pygame as pg
from settings import *
from particles import *
from random import randint

class ForcePlayer:
    def __init__(self, animation_player):
        self.animation_player = animation_player
        self.sprite_type = 'force'
        self.force_type = 'none'

    def drain(self, player,  cost, level, groups):
        self.force_type = 'drain'
        if player.energy >= cost:
            player.energy -= cost
            direction = self.get_force_direction(player)
            self.animate_force(player, direction, level, 'drain', groups)

    def lightning(self, player, cost, level, groups):
        self.force_type = 'lightning'
        if player.energy >= cost:
            player.energy -= cost
            direction = self.get_force_direction(player)
            self.animate_force(player, direction, level, 'lightning', groups)
            # if player.status.split('_')[0] == 'right':
            #     direction = pg.math.Vector2(1, 0)
            # elif player.status.split('_')[0] == 'left':
            #     direction = pg.math.Vector2(-1, 0)
            # elif player.status.split('_')[0] == 'up':
            #     direction = pg.math.Vector2(0, -1)
            # else:
            #     direction = pg.math.Vector2(0, 1)


            # for i in range(1, level+1):
            #     if direction.x > 0:#horiziontal right
            #         offset_x = i * TILESIZE * direction.x
            #         x = player.rect.centerx + offset_x - 12
            #         y = player.rect.centery + 15#+ randint(-TILESIZE//4, TILESIZE//4)
            #         self.animation_player.create_particles('lightning_1_right', (x, y), groups)
            #     elif direction.x < 0: #horiziontal left
            #         offset_x = i * TILESIZE * direction.x
            #         x = player.rect.centerx + offset_x + 12
            #         y = player.rect.centery + 15 #+ randint(-TILESIZE//4, TILESIZE//4)
            #         self.animation_player.create_particles('lightning_1_left', (x, y), groups)
            #     elif direction.y < 0: #vertical up
            #         offset_y = i * TILESIZE * direction.y
            #         x = player.rect.centerx + 15 #+ randint(-TILESIZE//4, TILESIZE//4)
            #         y = player.rect.centery + offset_y + 10
            #         self.animation_player.create_particles('lightning_1_up', (x, y), groups)
            #     else: #vertical down
            #         offset_y = i * TILESIZE * direction.y
            #         x = player.rect.centerx - 15 #+ randint(-TILESIZE//4, TILESIZE//4)
            #         y = player.rect.centery + offset_y - 10
            #         self.animation_player.create_particles('lightning_1_down', (x, y), groups)

    def push(self, player,  cost, level, groups):
        self.force_type = 'push'
        if player.energy >= cost:
            player.energy -= cost
            direction = self.get_force_direction(player)
            self.animate_force(player, direction, level, 'push', groups)


    def heal(self, player, strength, cost, groups):
        if player.energy >= cost and player.health < player.stats['health']:
                player.health += strength
                player.energy -= cost
                if player.health >= player.stats['health']:
                    player.health = player.stats['health']
                self.animation_player.create_particles('heal', player.rect.center + pg.math.Vector2(0, 0), groups)


    def get_force_direction(self, player):
        if player.status.split('_')[0] == 'right':
            direction = pg.math.Vector2(1, 0)
        elif player.status.split('_')[0] == 'left':
            direction = pg.math.Vector2(-1, 0)
        elif player.status.split('_')[0] == 'up':
            direction = pg.math.Vector2(0, -1)
        else:
            direction = pg.math.Vector2(0, 1)

        return direction

    def animate_force(self, player, direction, level, file_name, groups):
        for i in range(1, level + 1):
            if direction.x > 0:  # horiziontal right
                offset_x = i * TILESIZE * direction.x
                x = player.rect.centerx + offset_x - 12
                y = player.rect.centery + 15  # + randint(-TILESIZE//4, TILESIZE//4)
                self.animation_player.create_particles(file_name + '_right', (x, y), groups)
            elif direction.x < 0:  # horiziontal left
                offset_x = i * TILESIZE * direction.x
                x = player.rect.centerx + offset_x + 12
                y = player.rect.centery + 15  # + randint(-TILESIZE//4, TILESIZE//4)
                self.animation_player.create_particles(file_name + '_left', (x, y), groups)
            elif direction.y < 0:  # vertical up
                offset_y = i * TILESIZE * direction.y
                x = player.rect.centerx + 15  # + randint(-TILESIZE//4, TILESIZE//4)
                y = player.rect.centery + offset_y + 10
                self.animation_player.create_particles(file_name+ '_up', (x, y), groups)
            else:  # vertical down
                offset_y = i * TILESIZE * direction.y
                x = player.rect.centerx - 15  # + randint(-TILESIZE//4, TILESIZE//4)
                y = player.rect.centery + offset_y - 10
                self.animation_player.create_particles(file_name + '_down', (x, y), groups)