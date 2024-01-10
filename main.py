import pygame

# all setup goes here ##
pygame.init()
# screen is where everything is drawn or blited
screen = pygame.display.set_mode()
clock = pygame.time.Clock()

import threading
import pygame.sprite
import Gun
import Player
import Map


def performsetup(sprites: list):
    playerspritegroup = pygame.sprite.Group()
    playerspritegroup.add(Player.player())

    gunspritegroup = pygame.sprite.Group()
    gunspritegroup.add(Gun.gun("shotgun"))

    gamespritesgroup = pygame.sprite.Group()
    gamespritesgroup.add(*sprites)

    return playerspritegroup, gunspritegroup, gamespritesgroup


def main():
    frametime = 0
    running = True
    generatedsprites = []
    # spritegroup setup based on player+generation from map
    player, gun, gamespritegroup = performsetup(generatedsprites)

    # ###########################################
    # main loop runs at 60fps
    while running:
        # close program
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                pressed = pygame.key.get_pressed()
                if pressed[pygame.K_w]:
                    player.sprites()[0].move('w')
                if pressed[pygame.K_a]:
                    player.sprites()[0].move('a')
                if pressed[pygame.K_d]:
                    player.sprites()[0].move('d')
                if pressed[pygame.K_SPACE]:
                    gun.sprites()[0].shoot()
                    print(1)
            if event.type == pygame.KEYUP:
                if event.key not in [pygame.K_w, pygame.K_SPACE]:
                    player.sprites()[0].move()

        # clear screen
        screen.fill((0, 0, 0))
        # used to update and draw sprites
        player.update()
        player.draw(screen)
        gun.update(player.sprites()[0].getpos())
        gun.draw(screen)
        gamespritegroup.update()
        gamespritegroup.draw(screen)
        # clear screen
        pygame.display.flip()
        # set speed of frames and count frames
        clock.tick(60)
        frametime += 1


main()
