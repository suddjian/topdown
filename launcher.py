import game
import graphics
from scene import Scene
from entity_system import Entity
from controller import PlayerController
from euclid.euclid import Vector2


scene = Scene()
ent = Entity(scene)
ent.add(graphics.Sprite("assets/watermelon.png"))
ent.add(PlayerController())
ent.transform.position = Vector2(300, 200)
ent.transform.rotation = 45
# ent.transform.scale = Vector2(10, 10)
scene.entities.append(ent)
game.loop.append(scene)
game.run()
