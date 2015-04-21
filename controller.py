import pygame

import engine.game
from engine.entity_system import Component


class PlayerController(Component):

    def tick(self):
        self.entity.transform.rotation += 4
