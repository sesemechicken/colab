import pygame
import threading

import pygame.sprite
import Gun
import Player
import Map


def performsetup(sprites: list):
    gamesprites = [Player.player(), *sprites]
    gamespritesgroup = pygame.sprite.Group()
    for sprite in gamesprites:
        gamespritesgroup.add(sprite)
    return gamesprites[0], gamespritesgroup


def main():
    # all setup goes here ##
    pygame.init()
    # screen is where everything is drawn or blited
    screen = pygame.display.set_mode()
    clock = pygame.time.Clock()
    frametime = 0
    running = True
    generatedsprites = []
    # spritegroup setup based on player+generation from map
    player, gamespritegroup = performsetup(generatedsprites)

    # ###########################################
    # main loop runs at 60fps
    while running:
        # close program
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            # TODO elif event.type == "keydown":
            # player.move(key)
            # pass

        # clear screen
        screen.fill((0, 0, 0))
        # used to update and draw sprites
        gamespritegroup.update()
        gamespritegroup.draw(screen)
        # clear screen
        pygame.display.flip()
        # set speed of frames and count frames
        clock.tick(60)
        frametime += 1


main()
