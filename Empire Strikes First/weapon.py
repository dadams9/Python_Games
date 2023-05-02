import pygame as pg


class Weapon(pg.sprite.Sprite):
    def __init__(self, player, groups):
        super().__init__(groups)
        self.sprite_type = 'weapon'

        direction = player.status.split('_')[0]     #parse 'up_attack' to get just 'up'

        #Graphics
        full_path = f'images/characters/vader/attacks/{player.weapon}/{direction}.png'
        #full_path = f'images/characters/wookie/{player.weapon}/{direction}.png'
        self.image = pg.image.load(full_path).convert_alpha()


        #Placement
        if direction == 'right':
            self.rect = self.image.get_rect(midleft=player.rect.midright + pg.math.Vector2(-13, 13))
        elif direction == 'left':
            self.rect = self.image.get_rect(midright=player.rect.midleft + pg.math.Vector2(13, 13))
        elif direction == 'up':
            self.rect = self.image.get_rect(midbottom=player.rect.midtop + pg.math.Vector2(15, 20))
        elif direction == 'down':
            self.rect = self.image.get_rect(midtop=player.rect.midbottom + pg.math.Vector2(-15, -14))

        # if direction == 'right':
        #     self.image_box = self.image.get_rect(midleft=player.rect.midright + pg.math.Vector2(-13, 13))
        #     self.rect = self.image_box.inflate(0, 0)
        # elif direction == 'left':
        #     self.image_box = self.image.get_rect(midright=player.rect.midleft + pg.math.Vector2(13, 13))
        #     self.rect = self.image_box.inflate(0, 0)
        # elif direction == 'up':
        #     self.image_box = self.image.get_rect(midbottom=player.rect.midtop + pg.math.Vector2(15, 20))
        #     self.rect = self.image_box.inflate(0, 0)
        # elif direction == 'down':
        #     self.image_box = self.image.get_rect(midtop=player.rect.midbottom + pg.math.Vector2(-15, -14))
        #     self.rect = self.image_box.inflate(0, 0)


        #self.rect = self.rect.inflate(-30, -30)