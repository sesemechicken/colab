import pygame
import threading


def performsetup(screen):
    spritethreads=[]

    # loop
    # threads.append(threading.Thread(target=, args=))
    return spritethreads


def main():
    pygame.init()
    screen = pygame.display.set_mode()
    clock = pygame.time.Clock()
    frametime = 0
    running = True
    spritethreads = performsetup(screen)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for spritethread in spritethreads:
            spritethread.run()
        pygame.display.flip()
        clock.tick(30)
        frametime += 1



main()

