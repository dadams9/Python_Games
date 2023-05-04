import pygame as pg
from support import import_folder
from random import choice

class AnimationPlayer:
    def __init__(self):
        #import all the images for animations in a dictionary
        #example:
        self.frames = {
                       #Force Level 1
                       'push_1_right': import_folder('images/particles/force/push/push_1/right'),
                       'push_1_left': import_folder('images/particles/force/push/push_1/left'),
                       'push_1_up': import_folder('images/particles/force/push/push_1/up'),
                       'push_1_down': import_folder('images/particles/force/push/push_1/down'),

                        #Enemy Attacks
                        'bowcaster': import_folder('images/particles/lasers/bowcaster_right/'),
                        'bowcaster_left': import_folder('images/particles/lasers/bowcaster_left/'),
                        'bowcaster_up': import_folder('images/particles/lasers/bowcaster_up/'),
                        'bowcaster_down': import_folder('images/particles/lasers/bowcaster_down/'),

                        #Enemy Deaths
                        'wookie': import_folder('images/particles/enemy_deaths/wookie/'),
                        'chewy': import_folder('images/particles/enemy_deaths/chewy/')
        }

    def reflect_images(self, frames):
        new_frames = []
        for frame in frames:
            flipped_frame = pg.transform.flip(frame, True, False)
            new_frames.append(flipped_frame)

        return new_frames


    def create_grass_particles(self, position, groups):
        animation_frames = choice(self.frames['leaf'])
        ParticleEffect(position, animation_frames, groups)

    def create_particles(self, animation_type, position, groups):
        animation_frames = self.frames[animation_type]
        ParticleEffect(position, animation_frames, groups)

class ParticleEffect(pg.sprite.Sprite):
    def __init__(self, position, animation_frames, groups):
        super().__init__(groups)
        self.frame_index = 0
        self.animation_speed = 0.15
        self.frames = animation_frames
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center=position)

    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.kill()
        else:
            self.image = self.frames[int(self.frame_index)]

    def update(self):
        self.animate()