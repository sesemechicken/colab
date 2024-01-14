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
        # used for pygameui of dinosuar
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
            if abs(self.xvel) <= 2:
                self.xvel += self.acceleration * self.direction
        else:
            # stop moving
            self.xvel = 0

        # check for collide before hitting
        # self.checkfururecolide(maptiles)
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

        # make a new surface to load the image on
        selectedframe = pygame.Surface((self.width, self.height)).convert_alpha()
        # make frame size smaller than the image but covering one frame at a time =
        selectedframe.blit(self.spritesheet, (0, 0), (floor(self.frame) * self.width, 0, self.height, self.width))
        # used if facing opposite way
        if self.direction == -1:
            selectedframe = pygame.transform.flip(selectedframe, True, False)
        # resize and set as active image
        self.image = pygame.transform.scale(selectedframe, (self.width * 2, self.height * 2))
        self.image.set_colorkey((0, 0, 0))

    def move(self, key=None):
        # if no key is pressed at all
        if key is None:
            self.moving = False
            self.standingstill = True
            self.xvel = 0

        elif not self.jumping and key == "w":
            self.jumping = True

        # horizontal controls change direction and reset velocity
        elif key == "d":
            self.direction = 1
            self.moving = True
            self.standingstill = False

        elif key == "a":
            self.direction = -1
            self.moving = True
            self.standingstill = False

    def checkfururecolide(self, maptiles):
        if self.rect.collideobjects(maptiles):
            print("hit")

    # currentlly used to make gun in right place
    def getpos(self):
        return self.rect.center[0], self.rect.center[1], self.direction
