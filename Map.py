# TODO set up maps with enemy sprite generator
import os

import pygame.sprite
import Enemy

# load mapdata
maps = [open('assets/MAPS/' + file).read().replace("\n", ":").split(":") for file in os.listdir('assets/MAPS')]


class map:
    """
    map files formatted as:
    word, word, word, *40
    word, word, word, *40
    *22...
    right now 1 map fills a 1920x1080 screen
    maps is formatted as [['',''],['','']]
    where [] is the main list ['',''] is a map and '' is a fill line across the x
    maps [][].split(,)[x] is used so that:
    the first bracket selects the ['',''] (map)
    second bracked selects the '', (row)
    the third bracket selects the separate items in this string that was split (column)
    """

    def __init__(self):
        self.tilesize = 32
        self.borders = ([40*self.tilesize / 4, 40*self.tilesize * 3 / 4], [22*self.tilesize / 4, 22*self.tilesize * 3 / 4])
        self.enemys = []
        self.tiles = []

    def readfile(self, level):
        for y in range(22):
            for x in range(40):
                type = maps[level][y].split(',')[x]
                if type[-1] in [number for number in range(9)]:
                    self.enemys.append(Enemy.enemy(x, y, type[0:-1], type[-1]))
                else:
                    if type != "void":
                        self.tiles.append(tile(x, y, type))

    def update(self, offset, velocity):
        if self.borders[0][0] > offset[0] or offset[0]> self.borders[0][1]:
            for tile in self.tiles:
                tile.update(offset, "x",velocity[0])
        if self.borders[1][0] > offset[1]or offset[1] > self.borders[1][1]:
            for tile in self.tiles:
                tile.update(offset, "y", velocity[1])



    def returnenemys(self):
        return self.enemys

    def returntiles(self):
        return self.tiles


class tile(pygame.sprite.Sprite):
    def __init__(self, x, y, tiletype):
        super().__init__()
        self.size = 32
        self.x, self.y = x * self.size, y * self.size
        self.type = tiletype
        # TODO add names for tile pieces for use in map files also add tile sprites
        self.image = pygame.Surface((self.size, self.size)).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.image.fill("red")

    def update(self, offset, axis, velocity):
        if axis == "x":
            self.rect.x -= velocity
        if axis == "y":
            self.rect.y -= velocity
        pass

    def returnrect(self):
        return self.rect
