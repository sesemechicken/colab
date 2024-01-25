import pygame


def collision(tilespritesgroup, player, gun, enemyspritesgroup, bulletspritesgroup):
    touching=False
    for tiles in tilespritesgroup:
        if pygame.sprite.spritecollide(tiles, player.sprites(), False, pygame.sprite.collide_mask):
            touching = True
            if player.sprites()[0].yvel<-1:
                player.sprites()[0].rect.y+=3
                player.sprites()[0].yvel*=-1/2
                return
            if player.sprites()[0].falling:
                player.sprites()[0].land()
                return
            if player.sprites()[0].xvel>1 and tiles.rect.left<player.sprites()[0].rect.right:
                player.sprites()[0].xvel=0
                player.sprites()[0].rect.x-=2
            if player.sprites()[0].xvel<-1 and tiles.rect.right>player.sprites()[0].rect.left:
                player.sprites()[0].xvel=0
                player.sprites()[0].rect.x+=2
    if not touching:
        player.sprites()[0].falling = True
        print(player.sprites()[0].falling)
    pass
