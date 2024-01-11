# TODO set up maps with enemy sprite generator
import os

import pygame.sprite

# load mapdata
maps = [open('assets/MAPS/' + file).read() for file in os.listdir('assets/MAPS')]
tilesize = 35
size = tilesize * 100
enemys = []
tiles = []


def generateenemys(level):
    pass


def getenemys():
    return enemys


def generatetiles(level):
    ylevel = xlevel = 0
    for y in maps:
        ylevel += 1
        for placeholder in y:
            xlevel += 1
            tiles.append(tile(xlevel, ylevel, placeholder))


def gettiles():
    return tiles


class tile(pygame.sprite.Sprite):
    def __init__(self, x, y, tiletype):
        super().__init__()
        self.size = tilesize
        self.x, self.y = x * self.size, y * self.size
        self.type = tiletype
        self.image = pygame.Surface((self.size, self.size)).convert_alpha()
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.image.fill("red")

    def returnrect(self):
        return self.rect
