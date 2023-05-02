import pygame as pg
from support import import_folder

class AnimationPlayer:
    def __init__(self):
        #import all the images for animations in a dictionary
        #example:
        self.frames = {
                       #Force Level 1
                       'push_1_right': import_folder('images/particles/force/push/push_1/right'),
                       'push_1_left': import_folder('images/particles/force/push/push_1/left'),
                       'push_1_up': import_folder('images/particles/force/push/push_1/up'),
                       'push_1_down': import_folder('images/particles/force/push/push_1/down')
        }

    def reflect_images(self, frames):
        new_frames = []
        for frame in frames:
            flipped_frame = pg.transform.flip(frame, True, False)
            new_frames.append(flipped_frame)

        return new_frames
class ParticleEffect(pg.sprite.Sprite):
    def __init__(self, position, animation_frames, groups):
        super().__init__(groups)
        self.frame_index = 0
        self.animation_speed = 0.15
        self.frames = animation_frames
        self.image = self.image.get_rect[self.frame_index]

    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame >= len(self.frames):
            self.kill()
        else:
            self.image = self.frames[int(self.frame_index)]

    def update(self):
        self.animate()