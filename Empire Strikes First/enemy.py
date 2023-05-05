import pygame as pg
from settings import *
from entity import Entity
from debug import debug

class Enemy(Entity):
    def __init__(self, enemy_name, position, groups, obstacle_sprites, damage_player, trigger_death_particles):
        #general setup
        super().__init__(groups)
        self.sprite_type = 'enemy'

        #graphics setup
        self.import_character_graphics(enemy_name)
        self.status = 'down_idle'
        self.image = self.animations[self.status][self.frame_index]#pg.transform.rotozoom(pg.image.load(f'images/characters/{enemy_name}/down_idle/down_idle.png').convert_alpha(), 0, 1)

        #movement
        self.rect = self.image.get_rect(topleft=position)
        self.hitbox = self.rect.inflate(-20, -20)
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
        self.damage_player = damage_player
        self.trigger_death_partices = trigger_death_particles

        #invincibility timer
        self.vulnerable = True
        self.hit_time = None
        self.invincibility_duration = 300

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
            self.damage_player(self.attack_damage, self.attack_type)

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

        if not self.vulnerable:
            alpha = self.wave_value()
            self.image.set_alpha(alpha)
        else:
            self.image.set_alpha(255)

    def cooldowns(self):
        current_time = pg.time.get_ticks()
        if not self.can_attack:
            if current_time - self.attack_time >= self.attack_cooldown:
                self.can_attack = True

        if not self.vulnerable:
            if current_time - self.hit_time >= self.invincibility_duration:
                self.vulnerable = True

    def get_damage(self, player, attack_type):
        self.direction = self.get_player_distance_direction(player)[1]
        if self.vulnerable:
            if attack_type == 'weapon':
                self.health -= player.get_full_weapon_damage()
            else:
                self.health -= player.get_full_force_damage()
        self.hit_time = pg.time.get_ticks()
        self.vulnerable = False

    def check_death(self):
        if self.health <= 0:
            self.kill()
            self.trigger_death_partices(self.rect.center, self.enemy_name)

    def hit_reaction(self):
        if not self.vulnerable:
            self.direction *= -self.resistance

    def update(self):
        self.hit_reaction()
        self.move(self.speed)
        self.animate()
        self.cooldowns()
        self.check_death()

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