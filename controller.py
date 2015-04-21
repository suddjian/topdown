import pygame

import game
from entity_system import Component


class PlayerController(Component):

    def tick(self):
        self.entity.transform.rotation += 4
