import pygame

from entity_system import Component


_surfaces = {"default": pygame.Surface((16, 16))}
_surfaces["default"].fill((255, 0, 0, 255))


def get_surface(filename):
    """
    Gets an image located at filename and returns it. Loads the image
    if it is not yet loaded.
    """
    global _surfaces
    surf = _surfaces.get(filename)
    if surf is None:
        surf = pygame.image.load(filename)
        _surfaces[filename] = surf
    return surf


def load_surface(filename):
    """ Loads an image into memory without doing anything with it. """
    global _surfaces
    _surfaces[filename] = pygame.image.load(filename)


class Sprite(Component):

    def __init__(self, surface_name="default"):
        self.surface = get_surface(surface_name)

    def draw(self):
        self.entity.scene.draw(self.surface, self.entity.transform)
