import pygame as pg
import pygame.key
from entity import Entity
from support import *
from settings import *


class Player(Entity):
    def __init__(self, pos, groups, obstacle_sprites, create_attack, destroy_attack, create_force): #po =position, groups=assign the sprite to the group
        super().__init__(groups) #initiate the sprite group
        self.image = pg.transform.rotozoom(pg.image.load('images/characters/vader/down_idle/down_idle_up.png').convert_alpha(), 0, 1)
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-28, -30)   #Reduction in rectangle size to define hitbox.

        #Graphics setup
        self.import_character_graphics('vader')
        #self.import_player_assets()
        self.status = 'down'
        #self.frame_index = 0   #Shared with enemies
        #self.animation_speed = 0.05    #shared with enemies


        #Movement
        #self.direction = pg.math.Vector2() #shared with enemies
        self.attacking = False
        self.attack_cooldown = 400
        self.attack_time = None


        self.obstacle_sprites = obstacle_sprites

        #Weapon & Force
        self.create_attack = create_attack
        self.destroy_attack = destroy_attack
        self.weapon_index = 0
        self.weapon = list(weapon_data.keys())[self.weapon_index]
        self.can_switch_weapon = True
        self.weapon_switch_time = None
        self.weapon_switch_duration_cooldown = 200

        #Force
        self.create_force = create_force
        self.force_index = 0
        self.force = list(force_data.keys())[self.force_index]
        self.can_switch_force = True
        self.force_switch_time = None
        self.force_switch_duration_cooldown = 200

        #Stats
        self.stats = {'health': 100, 'energy': 60, 'attack': 10, 'force': 4, 'speed': 3}
        self.max_stats = {'health': 300, 'energy': 140, 'attack': 20, 'force': 10, 'speed': 6}
        self.upgrade_cost = {'health': 100, 'energy': 100, 'attack': 100, 'force': 100, 'speed': 100}
        self.health = self.stats['health']
        self.energy = self.stats['energy']
        self.speed = self.stats['speed']
        self.experience = 10000


        #damage timer
        self.vulnerable = True
        self.hurt_time = None
        self.invulnerability_duration = 500


    # def import_player_assets(self):
    #     character_path = 'images/characters/vader'
    #     #character_path = 'images/characters/wookie'
    #     self.animations = {'up': [], 'down': [], 'left': [], 'right': [],
    #                        'up_idle': [], 'down_idle': [], 'left_idle': [], 'right_idle': [],
    #                        'up_attack': [], 'down_attack': [], 'left_attack': [], 'right_attack': []}
    #
    #     for animation in self.animations.keys():
    #         full_path = character_path + '/' + animation
    #         self.animations[animation] = import_folder(full_path)

    def input(self):
        #Prevent the player from doing anything while attacking
        if not self.attacking:
            keys = pygame.key.get_pressed()

            #Movement input
            if keys[pg.K_UP]:
                self.direction.y = -1
                self.status = 'up'
            elif keys[pg.K_DOWN]:
                self.direction.y = 1
                self.status = 'down'
            else:
                self.direction.y = 0

            if keys[pg.K_RIGHT]:
                self.direction.x = 1
                self.status = 'right'
            elif keys[pg.K_LEFT]:
                self.direction.x = -1
                self.status = 'left'
            else:
                self.direction.x = 0


            #Attack input
            if keys[pg.K_SPACE]:
                self.attacking = True
                self.create_attack()
                self.attack_time = pg.time.get_ticks()

            #Force input
            if keys[pg.K_f]:
                self.attacking = True
                style = list(force_data.keys())[self.force_index]
                strength = list(force_data.values())[self.force_index]['strength'] + self.stats['force']
                cost = list(force_data.values())[self.force_index]['cost']
                level = list(force_data.values())[self.force_index]['level']
                self.create_force(style, strength, cost, level)
                self.attack_time = pg.time.get_ticks()

            #Change force ability
            if keys[pg.K_d] and self.can_switch_force:
                self.can_switch_force = False
                self.force_switch_time = pg.time.get_ticks()

                if self.force_index < len(list(force_data.keys()))-1:
                    self.force_index += 1
                else:
                    self.force_index = 0
                self.force = list(force_data.keys())[self.force_index]

            #Change weapon
            if keys[pg.K_w] and self.can_switch_weapon:
                self.can_switch_weapon = False
                self.weapon_switch_time = pg.time.get_ticks()

                if self.weapon_index < len(list(weapon_data.keys()))-1:
                    self.weapon_index += 1
                else:
                    self.weapon_index = 0
                self.weapon = list(weapon_data.keys())[self.weapon_index]




    def get_status(self):
        #Idle Status
        #Check if player is not moving
        if self.direction.x == 0 and self.direction.y == 0:
            #Check if player is already in idle state and not attacking
            if not 'idle' in self.status and not 'attack' in self.status:
                self.status = self.status + '_idle'


        #Attack Status
        if self.attacking:
            #Make it so the player isn't moving when attacking
            self.direction.x = 0
            self.direction.y = 0
            #Check if player is already attacking
            if not 'attack' in self.status:
                #Overwrite the idle so can attack from idle position
                if 'idle' in self.status:
                    self.status = self.status.replace('_idle', '_attack')
                else:
                    self.status = self.status + '_attack'
        else:
            if 'attack' in self.status and self.direction.x == 0 and self.direction.y == 0:
                self.status = self.status.replace('_attack', '_idle')
            elif 'attack' in self.status:
                self.status = self.status.replace('_attack', '')

    # def move(self, speed):
    #     #Make sure that the length of the vector is always 1
    #     if self.direction.magnitude() != 0:
    #         self.direction = self.direction.normalize()
    #     #Multiply the vector by the speed
    #
    #     self.hitbox.x += self.direction.x * speed
    #     self.collision('horizontal')
    #     self.hitbox.y += self.direction.y * speed
    #     self.collision('vertical')
    #     self.rect.center = self.hitbox.center
    #
    # def collision(self, direction):
    #     if direction == "horizontal":
    #         for sprite in self.obstacle_sprites:
    #             if sprite.hitbox.colliderect(self.hitbox):      #Tells us if there is a collision between the two rectangles
    #                 if self.direction.x > 0:    #moving to the right
    #                     self.hitbox.right = sprite.hitbox.left  #Make the right side of player = the left of the obstacle
    #                 if self.direction.x < 0:    #moving to the left
    #                     self.hitbox.left = sprite.hitbox.right  #Make the left side of the player = the right of the obstacle
    #
    #     if direction == "vertical":
    #         for sprite in self.obstacle_sprites:
    #             if sprite.hitbox.colliderect(self.hitbox):
    #                 if self.direction.y > 0:     #moving down
    #                     self.hitbox.bottom = sprite.hitbox.top  #Make the bottom of player = to top of obstacle
    #                 if self.direction.y < 0:     #moving up
    #                     self.hitbox.top = sprite.hitbox.bottom  #make the top of the player = to the bottom of obstacle

    def cooldowns(self):
        current_time = pg.time.get_ticks()

        if self.attacking:
            if current_time - self.attack_time >= self.attack_cooldown + weapon_data[self.weapon]['cooldown']:
                self.attacking = False
                self.destroy_attack()

        if not self.can_switch_weapon:
            if current_time - self.weapon_switch_time >= self.weapon_switch_duration_cooldown:
                self.can_switch_weapon = True

        if not self.can_switch_force:
            if current_time - self.force_switch_time >= self.force_switch_duration_cooldown:
                self.can_switch_force = True


        if not self.vulnerable:
            if current_time - self.hurt_time >= self.invulnerability_duration:
                self.vulnerable = True

    def animate(self):
        animation = self.animations[self.status]

        #Loop over the frame_index
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        #Set the image
        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center=self.hitbox.center)

        #flicker if hit
        if not self.vulnerable:
            alpha = self.wave_value()
            self.image.set_alpha(alpha)
        else:
            self.image.set_alpha(255)


    def get_full_weapon_damage(self):
        base_damage = self.stats['attack']
        weapon_damage = weapon_data[self.weapon]['damage']
        return base_damage + weapon_damage

    def get_full_force_damage(self):
        base_damage = self.stats['force']
        force_damage = force_data[self.force]['strength']
        return force_damage + base_damage

    def get_cost_by_index(self, index):
        return list(self.upgrade_cost.values())[index]

    def get_value_by_index(self, index):
        return list(self.stats.values())[index]

    def energy_recovery(self):
        if self.energy < self.stats['energy']:
            self.energy += .005 * self.stats['force']
        else:
            self.energy = self.stats['energy']

    def update(self):
        self.input()
        self.get_status()
        self.animate()
        self.cooldowns()
        self.move(self.stats['speed'])
        self.energy_recovery()



