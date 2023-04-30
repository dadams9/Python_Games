import pygame as pg
from debug import debug
from settings import *
from entity import Entity
from support import *

class Enemy(Entity):
    def __init__(self, enemy_name, position, groups, obstacle_sprites, create_attack, destroy_attack):
        #general setup
        super().__init__(groups)
        self.sprite_type = 'enemy'

        #graphics setup
        self.import_character_graphics(enemy_name)
        self.status = 'down_idle'
        self.image = self.animations[self.status][self.frame_index]#pg.transform.rotozoom(pg.image.load(f'images/characters/{enemy_name}/down_idle/down_idle.png').convert_alpha(), 0, 1)
        self.direction = pg.math.Vector2()


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

        #movement
        self.rect = self.image.get_rect(topleft=position)
        self.hitbox = self.rect.inflate(0, -10)
        self.moving = False

        self.obstacle_sprites = obstacle_sprites
        self.create_enemy_attack = create_attack
        self.destroy_enemy_attack = destroy_attack

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
        distance_to_player = self.get_player_distance_direction(player)[0]

        if abs(self.direction.x) > abs(self.direction.y):
            if self.direction.x >= 0:
                self.status = 'right'
            elif self.direction.x < 0:
                self.status = 'left'
        else:
            if self.direction.y >= 0:
                self.status = 'down'
            elif self.direction.y < 0:
                self.status = 'up'



        if distance_to_player <= self.attack_radius:
            self.attacking = True
            if 'attack' not in self.status:
                if 'idle' not in self.status:
                    self.status = self.status + '_attack'
                else:
                    self.status = self.status.replace('_idle', '_attack')
            self.attack_time = pg.time.get_ticks()
            #self.status = 'attack'
            self.moving = True

        elif distance_to_player <= self.notice_radius:
            self.status = self.status.replace('_idle', '')
            #self.status = 'move'
            self.moving = True
        else:
            if 'idle' not in self.status:
            #self.status = 'idle'
                self.status = self.status + '_idle'
            else:
                self.status = 'down_idle'
            self.direction.x = 0
            self.direction.y = 0
            self.moving = False



        # Idle Status
        # Check if player is not moving
        if self.direction.x == 0 and self.direction.y == 0:
            # Check if player is already in idle state and not attacking
            if not 'idle' in self.status and not 'attack' in self.status:
                self.status = self.status + '_idle'

            # Attack Status
            if self.attacking:
                # Make it so the player isn't moving when attacking
                self.direction.x = 0
                self.direction.y = 0
                # Check if player is already attacking
                if not 'attack' in self.status:
                    # Overwrite the idle so can attack from idle position
                    if 'idle' in self.status:
                        self.status = self.status.replace('_idle', '_attack')
                    else:
                        self.status = self.status + '_attack'
            else:
                if 'attack' in self.status and self.direction.x == 0 and self.direction.y == 0:
                    self.status = self.status.replace('_attack', '_idle')
                elif 'attack' in self.status:
                    self.status = self.status.replace('_attack', '')


    def cooldowns(self):
        current_time = pg.time.get_ticks()

        if self.attacking:
            if current_time - self.attack_time >= self.attack_cooldown:
                self.attacking = False
                self.destroy_enemy_attack()


    def actions(self, player):
        if self.status == 'attack':
            print("attack")

        #elif  self.status == 'move':
       # elif 'idle' not in self.status and 'attack' not in self.status:
        elif self.moving:
            self.direction = self.get_player_distance_direction(player)[1]

        else:
            self.direction = pg.math.Vector2()



    def animate(self):
        animation = self.animations[self.status]

        #Loop over the frame_index
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        #Set the image
        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center=self.hitbox.center)

    def update(self):
        debug(self.direction.y)
        self.move(self.speed)
        self.animate()
        self.cooldowns()



    def enemy_update(self, player):
        self.get_status(player)
        self.actions(player)





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