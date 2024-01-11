import os
from math import floor

import pygame

# used to load
spritesheets = [pygame.image.load('assets/DINOS/' + file).convert_alpha() for file in os.listdir('assets/DINOS')]


class player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # set basic information
        self.x = 100
        self.y = 200
        self.height = 24
        self.width = 24

        # set movement bools and tools
        self.falling = False
        self.moving = False
        self.jumping = False
        self.hurt = False
        self.standingstill = True
        self.acceleration = .1
        self.direction = 1
        self.xvel = 0
        self.yvel = 0
        # used for pygameui of dino
        self.frame = 1
        self.spritesheet = spritesheets[0]
        self.image = pygame.Surface((self.width, self.height)).convert_alpha()
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def update(self, maptiles):
        # please note speed and velocity are interchangeable terms but velocity can be either direction

        # vertical movements ###########################

        # accelerate positively toward ground
        if self.falling:
            self.yvel += self.acceleration

        # accelerate negatively away from ground until a specific upward speed is reached
        if self.jumping:
            self.yvel -= self.acceleration
            if self.yvel < -4:
                self.falling = True
                self.jumping = False

        # horizontal movements ###########################

        if self.moving:
            # change velocity until max speed is reached
            if -2 <= self.xvel <= 2:
                self.xvel += self.acceleration * self.direction
        else:
            # stop moving
            self.xvel = 0

        self.checkfururecolide(maptiles)

        # apply velocity to y-axis of image
        self.rect.y += self.yvel
        # apply velocity to x-axis of image
        self.rect.x += self.xvel

        self.updatespriteimg()

    def updatespriteimg(self):
        # used to change and cycle the sprite's sheet images
        if self.hurt:
            if self.frame % 3 == 2:
                self.frame = 15
            self.frame += .2

        if self.falling:
            self.frame = 12

        elif self.jumping:
            self.frame = 11

        elif self.moving:
            if self.frame % 10 >= 9:
                self.frame = 4
            self.frame += .2

        elif self.standingstill:
            self.frame = 1

        selectedframe = pygame.Surface((self.width, self.height)).convert_alpha()
        selectedframe.blit(self.spritesheet, (0, 0), (floor(self.frame) * self.width, 0, self.height, self.width))
        if self.direction == -1:
            selectedframe = pygame.transform.flip(selectedframe, True, False)
        self.image = pygame.transform.scale(selectedframe, (self.width * 2, self.height * 2))
        self.image.set_colorkey((0, 0, 0))

    def move(self, key=None):

        if not self.jumping and key == "w":
            self.jumping = True
            return
        elif key == "d":
            self.direction = 1
            self.xvel = 0

        elif key == "a":
            self.direction = -1
            self.xvel = 0

        if key is not None:
            self.moving = True
            self.standingstill = False

        else:
            self.moving = False
            self.standingstill = True

    def checkfururecolide(self, maptiles):
        if self.rect.collideobjects(maptiles):
            print("hit")

    def getpos(self):
        return self.rect.center[0], self.rect.center[1], self.direction
