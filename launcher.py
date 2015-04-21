import engine.game
import engine.graphics
from engine.scene import Scene
from engine.entity_system import Entity
from controller import PlayerController
from euclid.euclid import Vector2


scene = Scene()
ent = Entity(scene)
ent.add(engine.graphics.Sprite("assets/watermelon.png"))
ent.add(PlayerController())
ent.transform.position = Vector2(300, 200)
ent.transform.rotation = 45
ent.transform.scale = Vector2(8, 8)
scene.entities.append(ent)
engine.game.loop.append(scene)
engine.game.run()
