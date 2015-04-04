import pygame
from pygame.locals import *
import controls


FRAMES_PER_SECOND = 60

_resolution = (1024, 768)
_running = True
_screen = pygame.display.set_mode(_resolution, pygame.DOUBLEBUF)

### Opens a new game window ###
def run():
    pygame.init()

    clock = pygame.time.Clock()

    while _running:
        clock.tick(60)
        print("tick " + str(_running))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stop()
            elif event.type == pygame.KEYDOWN:
                controls.call_listeners(event.key)


### Stops the game short ###
def stop():
    global _running
    _running = False

def set_resolution(res):
    global _resolution, _screen
    _resolution = res
    _screen = pygame.display.set_mode(_resolution, pygame.DOUBLEBUF)
