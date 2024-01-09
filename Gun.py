import pygame.sprite


class gun(pygame.sprite.Sprite):
    def __init__(self, playerx, playery, type):
        super().__init__()
        self.height = 23
        self.width = 25
        self.x, self.y = playerx, playery
        self.ammo = 0
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill("green")

    def update(self, *args):
        pass


class bullet(pygame.sprite.Sprite):
    def __init__(self, gunx, guny, type):
        super().__init__()
        self.height = 2
        self.width = 4
        self.x, self.y = gunx, guny
        self.velx = 10
        self.vely = 0
        self.acceleration = .1
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill("white")
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def update(self, *args):
        self.rect.x += self.velx,
        self.rect.y += self.vely
        self.velx -= self.acceleration
        self.vely += self.acceleration

    def getpos(self):
        return
