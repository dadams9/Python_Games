import pygame as pg
from settings import *
from tile import Tile
from player import Player
from debug import debug
from support import *
from random import choice
from weapon import Weapon
from ui import UI

class Level:
    def __init__(self):
        #get the display surface
        self.display_surface = pg.display.get_surface() #Gets the display surface from anywhere in the code

        # Sprite group setup
        self.visible_sprites = YSortCameraGroup()       #Custom sprite group
        self.obstacle_sprites = pg.sprite.Group()

        #Sprite Setup
        self.create_map()

        #Attack Sprites
        self.current_attack = None

        #User Interface
        self.ui = UI()

    def create_map(self):
        layouts = {
                'boundary': import_csv_layout('map/test_map._Floor_blocks.csv'),
                'object': import_csv_layout('map/test_map._Objects.csv')
        }

        graphics = {
            'statue': import_folder('map/Objects')
        }
        for style, layout in layouts.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x = col_index*TILESIZE
                        y = row_index*TILESIZE
                        if style == 'boundary':
                            Tile((x, y), [self.obstacle_sprites], 'invisible')
                        # if style == 'object':
                        if style == 'object':
                            #random_object_img = choice(graphics['statue'])
                            surf = graphics['statue'][1]
                            Tile((x, y), [self.visible_sprites], 'object', surf)

        #         if col == 'x':
        #             Tile((x, y), [self.visible_sprites, self.obstacle_sprites])
        #         elif col == 'p':
        #             self.player = Player((x, y), [self.visible_sprites], self.obstacle_sprites)
        self.player = Player((1000, 650), [self.visible_sprites], self.obstacle_sprites, self.create_attack, self.destroy_attack)

    def create_attack(self):
        self.current_attack = Weapon(self.player, [self.visible_sprites])

    def destroy_attack(self):
        if self.current_attack:
            self.current_attack.kill()
        self.current_attack = None

    def run(self):
        # Update and draw the game
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        self.ui.display(self.player)
        #debug(self.player.status)


class YSortCameraGroup(pg.sprite.Group):
    def __init__(self):
        #General Setup
        super().__init__()
        self.display_surface = pg.display.get_surface()
        self.half_width = self.display_surface.get_size()[0]//2
        self.half_height = self.display_surface.get_size()[1]//2
        self.offset = pg.math.Vector2()

        #creating the floor
        self.floor_surface = pg.transform.rotozoom(pg.image.load('map/test_map.png').convert(), 0, 2)
        self.floor_rect = self.floor_surface.get_rect(topleft = (0, 0))

    def custom_draw(self, player):
        #Getting the offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        #drawing the floor
        floor_offset_position = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surface, floor_offset_position)

        #for sprite in self.sprites():
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_position = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_position)