import pygame
from collision import collision

# all setup goes here ##
pygame.init()
# screen is where everything is drawn or blited
screen = pygame.display.set_mode((600,400))
clock = pygame.time.Clock()
height,width=screen.get_size()
import pygame.sprite
import Gun
import Player
import Map


def performsetup(tilesprites: list, enemysprites: list):
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
    currentmap = Map.map()
    currentmap.readfile(0)
    # spritegroups setup based on player, gun, map and enemygeneration from map
    player, gun, tilespritesgroup, enemyspritesgroup = performsetup(currentmap.returntiles(), currentmap.returnenemys())
    bulletspritesgroup = pygame.sprite.Group()
    # ###########################################
    # main loop runs at 60fps
    while running:
        # perform action on key press
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w]:
            player.sprites()[0].move('w')
        if pressed[pygame.K_a]:
            player.sprites()[0].move('a')
        if pressed[pygame.K_d]:
            player.sprites()[0].move('d')
        if pressed[pygame.K_SPACE]:
            if gun.sprites()[0].shottimer == 0:
                bulletspritesgroup.add(gun.sprites()[0].shoot())

                # close program
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYUP:
                # stop moving on key release
                if event.key not in [pygame.K_w, pygame.K_SPACE]:
                    player.sprites()[0].move()
        # clear screen
        screen.fill((0, 0, 0))
        # used to update and draw sprites
        currentmap.update(player.sprites()[0].rect.topleft, (player.sprites()[0].xvel,player.sprites()[0].yvel))
        tilespritesgroup.draw(screen)

        player.update(currentmap.returntiles(), currentmap.returnenemys())
        player.draw(screen)

        gun.update(player.sprites()[0].getpos())
        gun.draw(screen)

        enemyspritesgroup.update()
        enemyspritesgroup.draw(screen)

        bulletspritesgroup.update()
        bulletspritesgroup.draw(screen)

        collision(tilespritesgroup,player,gun,enemyspritesgroup,bulletspritesgroup)
        # clear screen
        pygame.display.flip()
        # set speed of frames and count frames
        clock.tick(60)
        frametime += 1


main()
