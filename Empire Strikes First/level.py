import pygame as pg
from settings import *
from tile import Tile
from player import Player
from debug import debug
from support import *
from random import choice
from weapon import Weapon
from ui import UI
from enemy import Enemy
from particles import AnimationPlayer
from random import randint
from force import ForcePlayer

class Level:
    def __init__(self):
        #get the display surface
        self.display_surface = pg.display.get_surface() #Gets the display surface from anywhere in the code

        # Sprite group setup
        self.visible_sprites = YSortCameraGroup()       #Custom sprite group
        self.obstacle_sprites = pg.sprite.Group()

        #Attack Sprites
        self.current_attack = None
        self.attack_sprites = pg.sprite.Group()
        self.attackable_sprites = pg.sprite.Group()

        #Sprite Setup
        self.create_map()

        #User Interface
        self.ui = UI()

        #particles
        self.animation_player = AnimationPlayer()
        self.force_player = ForcePlayer(self.animation_player)

    def create_map(self):
        layouts = {
                'boundary': import_csv_layout('map/test_map._Floor_blocks.csv'),
                'object': import_csv_layout('map/test_map._Objects.csv'),
                'entity': import_csv_layout('map/test_map._Entities.csv')
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


                        if style == 'entity':
                            if col == '238':    #Import Player, #(1000, 650)
                                self.player = Player(
                                                (x, y),
                                                [self.visible_sprites],
                                                self.obstacle_sprites,
                                                self.create_attack,
                                                self.destroy_attack,
                                                self.create_force)
                            else:
                                if col == '239': enemy_name = 'wookie'
                                elif col == '20': enemy_name = 'chewy'
                                Enemy(enemy_name,
                                      (x, y),
                                      [self.visible_sprites, self.attackable_sprites],
                                      self.obstacle_sprites,
                                      self.damage_player,
                                      self.trigger_death_particles)


        #         if col == 'x':
        #             Tile((x, y), [self.visible_sprites, self.obstacle_sprites])
        #         elif col == 'p':
        #             self.player = Player((x, y), [self.visible_sprites], self.obstacle_sprites)


    def create_attack(self):
        self.current_attack = Weapon(self.player, [self.visible_sprites, self.attack_sprites])

    def create_force(self, style, strength, cost, level):
        if style == 'heal': #heal
            self.force_player.heal(self.player, strength, cost, [self.visible_sprites])

        if style == 'lightning':
            self.force_player.lightning(self.player, cost, level, [self.visible_sprites, self.attack_sprites])

        if style == 'push':
            self.force_player.push(self.player, cost, level, [self.visible_sprites, self.attack_sprites])

        if style == 'drain':
            self.force_player.drain(self.player, cost, level, [self.visible_sprites, self.attack_sprites])



    def destroy_attack(self):
        if self.current_attack:
            self.current_attack.kill()
        self.current_attack = None

    def player_attack_logic(self):
        if self.attack_sprites: #If there is anything inside attack_sprites
            for attack_sprite in self.attack_sprites:
                collision_sprites = pg.sprite.spritecollide(attack_sprite, self.attackable_sprites, False)
                if collision_sprites: #if we have any collision
                    for target_sprite in collision_sprites: #Now we finally have the sprite colliding with our weapon
                        if target_sprite.sprite_type == 'grass':
                            position = target_sprite.rect.center
                            offset = pg.math.Vector2(0, 55)
                            for leaf in range(randint(3, 6)):
                                self.animation_player.create_grass_particles(position-offset, [self.visible_sprites])
                            target_sprite.kill()
                        elif target_sprite.sprite_type == 'enemy':
                            target_sprite.get_damage(self.player, attack_sprite.sprite_type, self.force_player.force_type)


    def damage_player(self, amount, attack_type):
        if self.player.vulnerable == True:
            self.player.health -= amount
            self.player.vulnerable = False
            self.player.hurt_time = pg.time.get_ticks()
            #spawn particles
            self.animation_player.create_particles(attack_type, self.player.rect.center, [self.visible_sprites])

    def trigger_death_particles(self, position, particle_type):
        self.animation_player.create_particles(particle_type, position, [self.visible_sprites])

    def run(self):
        # Update and draw the game
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        self.visible_sprites.enemy_update(self.player)
        self.player_attack_logic()
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

    def enemy_update(self, player):
        enemy_sprites = [sprite for sprite in self.sprites() if hasattr(sprite, 'sprite_type') and sprite.sprite_type == 'enemy']
        for enemy in enemy_sprites:
            enemy.enemy_update(player)