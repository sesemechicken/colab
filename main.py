import pygame
import threading


def performsetup(screen):
    spritethreads = []

    # loop
    # threads.append(threading.Thread(target=, args=))
    return spritethreads


def main():
    # all setup goes here ##
    pygame.init()
    # screen is where everything is drawn or blited
    screen = pygame.display.set_mode()
    clock = pygame.time.Clock()
    frametime = 0
    running = True

    # an array of sprite threads
    # spritethreads = performsetup(screen)

    # ###########################################
    # main loop runs at 60fps
    while running:
        # close program
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # used to update and draw sprites
        # for spritethread in spritethreads:
        # spritethread.run()

        # clear screen
        pygame.display.flip()
        # set speed of frames and count frames
        clock.tick(60)
        frametime += 1


main()
