import pygame as pg


class EnemyWeapon(pg.sprite.Sprite):
    def __init__(self, enemies, groups):
        super().__init__(groups)
        for enemy in enemies:
            if 'attack' in enemy.status:
                direction = enemy.status.split('_')[0]     #parse 'up_attack' to get just 'up'

                #Graphics
                full_path = f'images/characters/{enemy.name}/{direction}.png'
                self.image = pg.image.load(full_path).convert_alpha()

                #Placement
                if enemy.name == 'wookie' or enemy.name == 'chewy':
                    if direction == 'right':
                        self.rect = self.image.get_rect(midleft=enemy.rect.midright + pg.math.Vector2(-13, 13))
                    elif direction == 'left':
                        self.rect = self.image.get_rect(midright=enemy.rect.midleft + pg.math.Vector2(13, 13))
                    elif direction == 'up':
                        self.rect = self.image.get_rect(midbottom=enemy.rect.midtop + pg.math.Vector2(15, 20))
                    elif direction == 'down':
                        self.rect = self.image.get_rect(midtop=enemy.rect.midbottom + pg.math.Vector2(-15, -14))
