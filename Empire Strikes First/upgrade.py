import pygame as pg
from settings import *

class Upgrade:
    def __init__(self, player):
        #general setup
        self.display_surface = pg.display.get_surface()
        self.player = player
        self.attribute_number = len(player.stats)
        self.attribute_names = list(player.stats.keys())
        self.max_values = list(player.max_stats.values())
        self.font = pg.font.SysFont(UI_FONT, UI_FONT_SIZE)

        #Item Creation
        self.vertical_margin = 0.2
        self.height = self.display_surface.get_size()[1] * (1-self.vertical_margin) #To leave some margin
        self.width = self.display_surface.get_size()[0] // (self.attribute_number + 1)
        self.create_items()

        #Selection System
        self.selection_index = 0
        self.selection_time = None
        self.can_move = True



    def input(self):
        keys = pg.key.get_pressed()
        if self.can_move:
            if keys[pg.K_RIGHT] and self.selection_index < self.attribute_number-1:
                self.selection_index += 1
                self.can_move = False
                self.selection_time = pg.time.get_ticks()
            elif keys[pg.K_LEFT] and self.selection_index >= 1:
                self.selection_index -= 1
                self.can_move = False
                self.selection_time = pg.time.get_ticks()
            if keys[pg.K_SPACE]:
                self.item_list[self.selection_index].trigger(self.player)
                self.can_move = False
                self.selection_time = pg.time.get_ticks()

    def selection_cooldown(self):
        if not self.can_move:
            current_time = pg.time.get_ticks()
            if current_time - self.selection_time >= 300:
                self.can_move = True


    def create_items(self):
        self.item_list = []

        for index, item in enumerate(range(self.attribute_number)):

            #horizontal position
            full_width = self.display_surface.get_size()[0]
            increment = full_width // self.attribute_number
            left = (item * increment) + (increment - self.width)//2
            #vertical position
            top = self.vertical_margin/2 * self.display_surface.get_size()[1]

            #create object
            item = Item(left, top, self.width, self.height, index, self.font)
            self.item_list.append(item)


    def display(self):
        self.input()
        self.selection_cooldown()
        for index, item in enumerate(self.item_list):
            #get attributes
            name = self.attribute_names[index]
            value = self.player.get_value_by_index(index)
            max_value = self.max_values[index]
            cost = self.player.get_cost_by_index(index)
            item.display(self.display_surface, self.selection_index, name, value, max_value, cost)
        #self.display_surface.fill('black')


class Item:
    def __init__(self, left, top, width, height, index, font):
        self.rect = pg.Rect(left, top, width, height)
        self.index = index
        self.font = font


    def display_names(self, surface, name, cost, current_val, selected):
        color = TEXT_COLOR_SELECTED if selected else TEXT_COLOR

        #Title
        title_surface = self.font.render(name, False, color)
        title_rect = title_surface.get_rect(midtop=self.rect.midtop + pg.math.Vector2(0, 20))

        #Cost
        cost_surface = self.font.render(str(cost), False, color)
        cost_rect = cost_surface.get_rect(midtop=self.rect.midtop + pg.math.Vector2(0, 40))

        #Current Value
        current_surface = self.font.render(str(int(current_val)), False, color)
        current_rect = current_surface.get_rect(midbottom=self.rect.midbottom + pg.math.Vector2(0, -20))

        #Draw
        surface.blit(title_surface, title_rect)
        surface.blit(cost_surface, cost_rect)
        surface.blit(current_surface, current_rect)

    def display_bar(self, surface, value, max_value, selected):
        #Drawing setup
        top = self.rect.midtop + pg.math.Vector2(0, 80)
        bottom = self.rect.midbottom + pg.math.Vector2(0, -60)
        color = BAR_COLOR_SELECTED if selected else BAR_COLOR

        #bar setup
        full_height = bottom[1] - top[1]
        relative_number = (value / max_value) * full_height
        width = 30
        height = 10
        value_rect = pg.Rect(top[0]-width/2, bottom[1] - relative_number, width, height)

        #draw element
        pg.draw.line(surface, color, top, bottom, 5) #width of 5
        pg.draw.rect(surface, color, value_rect)

    def trigger(self, player):
        upgrade_attribute = list(player.stats.keys())[self.index]
        if player.experience >= player.upgrade_cost[upgrade_attribute] and player.stats[upgrade_attribute] < player.max_stats[upgrade_attribute]:
            player.experience -= player.upgrade_cost[upgrade_attribute]
            player.stats[upgrade_attribute] = int(player.stats[upgrade_attribute] *1.2)+1
            player.upgrade_cost[upgrade_attribute] = int(player.upgrade_cost[upgrade_attribute]*1.4)

        if player.stats[upgrade_attribute] > player.max_stats[upgrade_attribute]:
            player.stats[upgrade_attribute] = player.max_stats[upgrade_attribute]


    def display(self, surface, selection_num, name, value, max_value, cost):
        if self.index == selection_num:
            pg.draw.rect(surface, UPGRADE_BG_COLOR_SELECTED, self.rect)
            pg.draw.rect(surface, UI_BORDER_COLOR, self.rect, 4)
        else:
            pg.draw.rect(surface, UI_BG_COLOR, self.rect)
            pg.draw.rect(surface, UI_BORDER_COLOR, self.rect, 4)

        self.display_names(surface, name.upper(), cost, value, self.index == selection_num)
        self.display_bar(surface, value, max_value, self.index == selection_num)