# TODO set up maps with enemy sprite generator
import os

import pygame.sprite

import Enemy

# load mapdata
maps = [open('assets/MAPS/' + file).read() for file in os.listdir('assets/MAPS')]
tilesize = 35
size = tilesize * 100
enemys = []
tiles = []


def generateenemys():

    pass


def getenemys():
    return enemys

def readfile(level):
    ylevel = -1
    for y in maps:
        xlevel = -1
        ylevel += 1
        for type in y:
            xlevel += 1
            if type[-1] in ["{number}" for number in range(9)]:
                enemys.append(Enemy.enemy(xlevel, ylevel, type[0:-1], type[-1]))
            else:
                tiles.append(tile(xlevel, ylevel, type))

def generatetiles():
    pass


def gettiles():
    return tiles


class tile(pygame.sprite.Sprite):
    def __init__(self, x, y, tiletype):
        super().__init__()
        self.size = tilesize
        self.x, self.y = x * self.size, y * self.size
        self.type = tiletype
        # TODO add names for tile pieces for use in map files also add tile sprites
        self.image = pygame.Surface((self.size, self.size)).convert_alpha()
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.image.fill("red")

    def returnrect(self):
        return self.rect
