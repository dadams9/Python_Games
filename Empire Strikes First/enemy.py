import pygame as pg
from settings import *
from entity import Entity

class Enemy(Entity):
    def __init__(self, enemy_name, position, groups):
        #general setup
        super().__init__(groups)
        self.sprite_type = 'enemy'

        #graphics setup
        self.import_character_graphics(enemy_name)
        self.status = 'down_idle'
        self.image = self.animations[self.status][self.frame_index]#pg.transform.rotozoom(pg.image.load(f'images/characters/{enemy_name}/down_idle/down_idle.png').convert_alpha(), 0, 1)
        self.rect = self.image.get_rect(topleft=position)

# def import_graphics(self, name):
#     #character_path = 'images/characters/vader'
#     character_path = f'images/characters/{name}'
#     self.animations = {'up': [], 'down': [], 'left': [], 'right': [],
#                        'up_idle': [], 'down_idle': [], 'left_idle': [], 'right_idle': [],
#                        'up_attack': [], 'down_attack': [], 'left_attack': [], 'right_attack': []}
#
#     for animation in self.animations.keys():
#         full_path = character_path + '/' + animation
#         self.animations[animation] = import_folder(full_path)