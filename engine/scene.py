import pygame

import game
from euclid.euclid import Vector2


class Scene:

    def __init__(self, surface=game.screen):
        self.entities = []
        self.surface = surface

    def loop(self):
        for e in self.entities:
            e.tick()

        for e in self.entities:
            e.phys()

        for e in self.entities:
            e.draw()

    def draw(self, surface, transform):
        # transform the surface before drawing it
        sc = (transform.scale.x * surface.get_width(),
              transform.scale.y * surface.get_height())

        s = pygame.transform.smoothscale(surface, sc)
        r1 = s.get_rect()  # the rect before rotation
        s = pygame.transform.rotozoom(s, transform.rotation, 1)
        r2 = s.get_rect()  # the rect after rotation
        # have to adjust position after rotating, because rotation can
        # make the surface bigger

        # s = pygame.transform.rotate(surface, transform.rotation)

        # translation, adjusted for possible rotation resizing
        trans = Vector2((r1.width - r2.width) / 2,
                        (r1.height - r2.height) / 2)
        trans += transform.position

        self.surface.blit(s, trans)
