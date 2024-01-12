import os
from math import floor
import random

import pygame.sprite

# load gun frames
# pistolframes = pygame.image.load('assets/PISTOL/').convert_alpha()
# assultframes = pygame.image.load('assets/ASSAULT RIFLE/').convert_alpha()
shotgunframes = pygame.image.load('assets/SHOTGUN/spritesheet.png').convert_alpha()


class gun(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        # basic info about guns
        self.height = 32
        self.width = 160
        self.x, self.y = 0, 0
        self.direction = 1
        if type == "shotgun":
            self.framesprite = shotgunframes
        # elif type == "assult rifle":
        # self.framesprite = assultframes
        # elif type == "pistol":
        # self.framesprite = pistolframes
        self.type = type
        self.ammo = 0
        self.shooting = False
        # used for gun ui
        self.frame = 0
        self.image = pygame.Surface((self.width, self.height)).convert_alpha()
        self.rect = self.image.get_rect(midtop=(self.x, self.y))

    def updatespriteimg(self):
        # changes the ui image
        if self.shooting:
            self.frame += .25
        if self.frame >= 4:
            self.shooting = False
            self.frame = 0

        selectedframe = pygame.Surface((self.width, self.height)).convert_alpha()
        selectedframe.blit(self.framesprite, (0, 0), (self.width * floor(self.frame), 0, self.width, self.height))
        # some handwritten values due to inconsitencies
        if self.direction == -1:
            selectedframe = pygame.transform.flip(selectedframe, True, False)
            self.x -= 30
        else:
            self.x += 50
        self.image = pygame.transform.scale(selectedframe, (self.width / 1.5, self.height / 1.5))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect(midtop=(self.x, self.y + 5))

    def update(self, playerpos):
        # uses the player loaction to place the gun and update the image
        self.x, self.y, self.direction = playerpos
        self.updatespriteimg()

    def shoot(self):
        self.shooting = True
        # make a bullet and animate the gun
        bullets=[bullet(self.rect.center, self.direction) for i in range(5)]
        return bullets


class bullet(pygame.sprite.Sprite):
    def __init__(self, gunpos, direction):
        # unfinished
        super().__init__()
        self.height = 2
        self.width = 4
        self.x, self.y = gunpos[0], gunpos[1]
        self.velx = 7 + random.randint(-5, 5)/2
        self.vely = -1 + random.randint(-5, 5)/5
        if direction <0:
            self.velx*=-1
        self.direction=direction
        self.acceleration = .1
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill("white")
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def update(self, *args):
        self.velx -= self.acceleration* self.direction
        self.vely += self.acceleration
        self.rect.x += self.velx
        self.rect.y += self.vely / 2
        if -.5<self.velx<.5:
            self.kill()

    def getpos(self):
        return self.rect.x, self.rect.y
