# TODO set up maps with enemy sprite generator
import os

import pygame.sprite

import Enemy

# load mapdata
maps = [open('assets/MAPS/' + file).read().replace("\n", ":").split(":") for file in os.listdir('assets/MAPS')]
'''
map files formatted as:
word, word, word, *40
word, word, word, *40...

maps is formatted as [['',''],['','']]
where [] is the main list ['',''] is a map and '' is a fill line across the x
maps [][].split(,)[x] is used so that:
the first bracket selects the ['',''] (map)
second bracked selects the '', (row)
the third bracket selects the separate items in this string that was split (column)
'''
tilesize = 32
size = tilesize * 40
enemys = []
tiles = []


def readfile(level):
    for y in range(40):
        for x in range(40):
            type = maps[level][y].split(',')[x]
            if type[-1] in [number for number in range(9)]:
                enemys.append(Enemy.enemy(x, y, type[0:-1], type[-1]))
            else:
                if type != "void":
                    tiles.append(tile(x, y, type))


def returnenemys():
    return enemys


def returntiles():
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

    def update(self, offset):
        pass

    def returnrect(self):
        return self.rect
