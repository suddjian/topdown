from math import *

import pygame

from euclid.euclid import *


class Transform:

    def __init__(self,
                 position=Vector2(0, 0),
                 rotation=0,
                 scale=Vector2(1, 1),
                 parent=None,
                 children=[]):
        self._parent = parent
        self._children = children
        self.position = position
        self.rotation = rotation
        self.scale = scale

    def get_local_matrix(self):
        matrix = Matrix3.new_translate(_pos.x, _pos.y)
        matrix.rotate(_rot)
        matrix.scale(_scale.x, _scale.y)
        return matrix

    def get_world_matrix(self):
        matrix = get_local_matrix
        if parent is not None:
            matrix *= parent.get_world_matrix
        return matrix

    def get_world_transform(self):
        if parent is None:
            return self.clone()
        matrix = self.get_world_matrix()
        t = Transform()

    def set_parent(self, parent):
        this.parent = parent
        if parent is not None and self not in parent.children:
            parent.children.append(self)

    def copy(self):
        return Transform(self.position, self.rotation, self.scale)


class Entity:

    def __init__(self, scene, transform=Transform(), *components):
        self.scene = scene
        self.transform = transform
        self._components = []
        for comp in components:
            self.add_component(comp)

    def __getitem__(self, key):
        for comp in self._components:
            if isinstance(comp, key):
                return comp
        return None

    def __delitem__(self, key):
        for c in self._components:
            if isinstance(c, component_type):
                self._components.remove(c)
                c.entity = None

    def add(self, component):
        """
        removes all components of the same type as the given component,
        and adds the component to the entity
        """
        for i, c in enumerate(self._components):
            if isinstance(c, component.__class__):
                del self._components[i]
        self._components.append(component)
        component.entity = self

    def tick(self):
        for c in self._components:
            c.tick()

    def draw(self):
        for c in self._components:
            c.draw()

    def phys(self):
        for c in self._components:
            c.phys()


class Component:

    def tick(self):
        pass

    def phys(self):
        pass

    def draw(self):
        pass

    def get_scene(self):
        return self.entity.scene

    def get_transform(self):
        return self.entity.transform

    def set_transform(self, transform):
        self.entity.transform = transform

    def get_position(self):
        return self.entity.transform.position

    def set_position(self, pos):
        self.entity.transform.position = pos

    def get_rotation(self):
        return self.entity.transform.rotation

    def set_rotation(self, rot):
        self.entity.transform.rotation = rot

    def get_scale(self):
        return self.entity.transform.scale

    def set_scale(self, scale):
        self.entity.transform.scale = scale

    scene = property(get_scene)
    transform = property(get_transform, set_transform)
    position = property(get_position, set_position)
    rotation = property(get_rotation, set_rotation)
    scale = property(get_scale, set_scale)

    def get_component(self, component_type):
        return self.entity.get_component(compoent_type)
