import pygame

from keybindings import KeyBinding


FRAMES_PER_SECOND = 60

key_bindings = KeyBinding()

_resolution = (1024, 768)
_running = True
screen = pygame.display.set_mode(_resolution, pygame.DOUBLEBUF)

# a list of things with a loop function
loop = []


def run():

    pygame.init()
    clock = pygame.time.Clock()

    while _running:
        clock.tick(FRAMES_PER_SECOND)

        screen.fill((0, 0, 0))

        # tick
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stop()
            elif event.type == pygame.KEYDOWN:
                key_bindings.call(event.key)
        for l in loop:
            l.loop()

        pygame.display.flip()

    pygame.quit()


def stop():
    global _running
    _running = False


def set_resolution(res):
    global _resolution, _screen
    _resolution = res
    _screen = pygame.display.set_mode(_resolution, pygame.DOUBLEBUF)
