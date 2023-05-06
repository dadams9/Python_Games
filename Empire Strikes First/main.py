import pygame as pg
import sys
from settings import *
from debug import debug
from level import Level
import random


class Game:
    def __init__(self):
        #general setup
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(CAPTION)
        self.clock = pg.time.Clock()

        self.level = Level()    #Create an instance of the Level class in level.py

    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_u:
                        self.level.toggle_menu()

            self.screen.fill(FILL_COLOR)
            self.level.run()        #Call the run method of the level instance
            pg.display.update()
            self.clock.tick(FPS)    #Tells the while loop to loop FPS times per second

if __name__ == '__main__':
    game = Game()
    game.run()