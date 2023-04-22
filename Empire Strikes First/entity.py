import pygame as pg
from support import *

class Entity(pg.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.frame_index = 0
        self.animation_speed = 0.05
        self.direction = pg.math.Vector2()


    def move(self, speed):
        #Make sure that the length of the vector is always 1
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        #Multiply the vector by the speed

        self.hitbox.x += self.direction.x * speed
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical')
        self.rect.center = self.hitbox.center

    def collision(self, direction):
        if direction == "horizontal":
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):      #Tells us if there is a collision between the two rectangles
                    if self.direction.x > 0:    #moving to the right
                        self.hitbox.right = sprite.hitbox.left  #Make the right side of player = the left of the obstacle
                    if self.direction.x < 0:    #moving to the left
                        self.hitbox.left = sprite.hitbox.right  #Make the left side of the player = the right of the obstacle

        if direction == "vertical":
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0:     #moving down
                        self.hitbox.bottom = sprite.hitbox.top  #Make the bottom of player = to top of obstacle
                    if self.direction.y < 0:     #moving up
                        self.hitbox.top = sprite.hitbox.bottom  #make the top of the player = to the bottom of obstacle

    def import_character_graphics(self, name):
        character_path = f'images/characters/{name}'
        self.animations = {'up': [], 'down': [], 'left': [], 'right': [],
                           'up_idle': [], 'down_idle': [], 'left_idle': [], 'right_idle': [],
                           'up_attack': [], 'down_attack': [], 'left_attack': [], 'right_attack': []}

        for animation in self.animations.keys():
            full_path = character_path + '/' + animation
            self.animations[animation] = import_folder(full_path)