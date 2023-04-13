import pygame as pg
from settings import *
from player import *


class UI:
    def __init__(self):

        #General Information
        self.display_surface = pg.display.get_surface()
        self.font = pg.font.SysFont(UI_FONT, UI_FONT_SIZE)

        #Health/Energy Bar Setup
        self.health_bar_rect = pg.Rect(10, 10, HEALTH_BAR_WIDTH, BAR_HEIGHT)
        self.energy_bar_rect = pg.Rect(10, 35, ENERGY_BAR_WIDTH, BAR_HEIGHT)

    def show_bar(self, current_amount, max_amount, background_rect, color):
        #Draw background rectangle
        pg.draw.rect(self.display_surface, UI_BG_COLOR, background_rect)

        #Convert health/energy to pixel
        ratio = current_amount/max_amount
        current_width = ratio*background_rect.width
        current_rect = background_rect.copy()
        current_rect.width = current_width

        #Draw the health/energy bar
        pg.draw.rect(self.display_surface, color, current_rect)
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, background_rect, 3)
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, current_rect, 3)

    def show_exp(self, experience):
        text_surface = self.font.render("Exp: "+str(int(experience)), False, TEXT_COLOR)
        x = 20 # self.display_surface.get_size()[0]-20
        y = 65 #self.display_surface.get_size()[1]-20
        text_rect = text_surface.get_rect(topleft=(x, y)) #text_surface.get_rect(bottomright=(x, y))
        pg.draw.rect(self.display_surface, UI_BG_COLOR, text_rect.inflate(20, 8))
        self.display_surface.blit(text_surface, text_rect)
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, text_rect.inflate(20, 8), 3)

    def display(self, player):
        self.show_bar(player.health, player.stats['health'], self.health_bar_rect, HEALTH_COLOR)
        self.show_bar(player.energy, player.stats['energy'], self.energy_bar_rect, ENERGY_COLOR)
        self.show_exp(player.experience)

