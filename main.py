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


def performsetup(tilesprites: list, enemysprites:list):
    playerspritegroup = pygame.sprite.Group()
    playerspritegroup.add(Player.player())

    gunspritegroup = pygame.sprite.Group()
    gunspritegroup.add(Gun.gun("shotgun"))

    tilespritesgroup = pygame.sprite.Group()
    tilespritesgroup.add(*tilesprites)

    enemyspritesgroup = pygame.sprite.Group()
    enemyspritesgroup.add(*enemysprites)

    return playerspritegroup, gunspritegroup, tilespritesgroup, enemyspritesgroup


def main():
    # setup map and game loop
    frametime = 0
    running = True
    Map.generatetiles(0)
    Map.generateenemys(0)
    # spritegroups setup based on player, gun, map and enemygeneration from map
    player, gun, tilespritesgroup, enemyspritesgroup = performsetup(Map.gettiles(), Map.getenemys())
    bulletspritesgroup = pygame.sprite.Group()
    # ###########################################
    # main loop runs at 60fps
    while running:
        # close program
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                #perform action on key press
                pressed = pygame.key.get_pressed()
                if pressed[pygame.K_w]:
                    player.sprites()[0].move('w')
                if pressed[pygame.K_a]:
                    player.sprites()[0].move('a')
                if pressed[pygame.K_d]:
                    player.sprites()[0].move('d')
                if pressed[pygame.K_SPACE]:
                    bulletspritesgroup.add(gun.sprites()[0].shoot())
            if event.type == pygame.KEYUP:
                #stop moving on key release
                if event.key not in [pygame.K_w, pygame.K_SPACE]:
                    player.sprites()[0].move()

        # clear screen
        screen.fill((0, 0, 0))
        # used to update and draw sprites
        tilespritesgroup.update()
        tilespritesgroup.draw(screen)
        player.update(Map.gettiles())
        player.draw(screen)
        gun.update(player.sprites()[0].getpos())
        gun.draw(screen)
        enemyspritesgroup.update()
        enemyspritesgroup.draw(screen)
        bulletspritesgroup.update()
        bulletspritesgroup.draw(screen)
        # clear screen
        pygame.display.flip()
        # set speed of frames and count frames
        clock.tick(60)
        frametime += 1


main()
