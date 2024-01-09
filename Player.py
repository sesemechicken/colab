import pygame


class player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.x = 0
        self.y = 0
        self.height = 23
        self.width = 25
        self.xvel = 0
        self.yvel = 0
        self.falling = True
        self.moving = False
        self.acceleration = .2
        self.direction = 1
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill("red")
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def update(self, *args):
        if self.falling:
            self.yvel += self.acceleration
        self.rect.y += self.yvel
        if self.moving:
            self.xvel += self.acceleration * self.direction
        self.rect.x += self.xvel

    def move(self, key):
        if key == "w":
            self.yvel -= 50
            return
        if key == "d":
            self.direction = 1
            self.xvel = 0

        elif key == "a":
            self.direction = -1
            self.xvel = 0

        self.moving = True

    def collided(self, axis: tuple):

        if axis[1]:
            self.falling = False

        if axis[0]:
            self.xvel = 0
