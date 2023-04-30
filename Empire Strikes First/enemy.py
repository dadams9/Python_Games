import pygame as pg
from settings import *
from entity import Entity

class Enemy(Entity):
    def __init__(self, enemy_name, position, groups, obstacle_sprites):
        #general setup
        super().__init__(groups)
        self.sprite_type = 'enemy'

        #graphics setup
        self.import_character_graphics(enemy_name)
        self.status = 'down_idle'
        self.image = self.animations[self.status][self.frame_index]#pg.transform.rotozoom(pg.image.load(f'images/characters/{enemy_name}/down_idle/down_idle.png').convert_alpha(), 0, 1)

        #movement
        self.rect = self.image.get_rect(topleft=position)
        self.hitbox = self.rect.inflate(0, -10)
        self.obstacle_sprites = obstacle_sprites

        #stats
        self.enemy_name = enemy_name
        enemy_info = enemy_data[self.enemy_name]
        self.health = enemy_info['health']
        self.exp = enemy_info['exp']
        self.speed = enemy_info['speed']
        self.attack_damage = enemy_info['damage']
        self.resistance = enemy_info['resistance']
        self.attack_radius = enemy_info['attack_radius']
        self.notice_radius = enemy_info['notice_radius']
        self.attack_type = enemy_info['attack_type']


        #player interaction
        self.can_attack = True
        self.attack_time = None
        self.attack_cooldown = 400

    def get_player_distance_direction(self, player):
        enemy_vec = pg.math.Vector2(self.rect.center)
        player_vec = pg.math.Vector2(player.rect.center)
        distance = (player_vec - enemy_vec).magnitude()

        if distance > 0:
            direction = (player_vec - enemy_vec).normalize()

        else:
            direction = pg.math.Vector2()

        return distance, direction

    def get_status(self, player):
        distance = self.get_player_distance_direction(player)[0]

        if distance <= self.attack_radius and self.can_attack == True:
            if self.status != 'attack':
                self.frame_index = 0
            self.status = 'attack'
        elif distance <= self.notice_radius:
            self.status = 'move'
        else:
            self.status = 'idle'


    def actions(self, player):
        if self.status == 'attack':
            self.attack_time = pg.time.get_ticks()
        elif self.status == 'move':
            self.direction = self.get_player_distance_direction(player)[1]
        else:
            self.direction = pg.math.Vector2()


    def animate(self):
        animation = self.animations[self.status]

        #Loop over the frame_index
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            if self.status == 'attack':
                self.can_attack = False
            self.frame_index = 0

        #Set the image
        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center=self.hitbox.center)

    def cooldown(self):
        if not self.can_attack:
            current_time = pg.time.get_ticks()
            if current_time - self.attack_time >= self.attack_cooldown:
                self.can_attack = True


    def update(self):
        self.move(self.speed)
        self.animate()
        self.cooldown()

    def enemy_update(self, player):
        self.actions(player)
        self.get_status(player)


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