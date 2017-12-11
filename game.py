import pyglet
from pyglet.window import key
import math

# Consts tj. konstanty
ROTATION_SPEED = 4   #radians per sec (python operates only with radians)

# Global state:
objects = []

pressed_keys = set()
# Clases:
class Spaceship:
    def __init__ (self):
        self.x = 20
        self.y = 40
        self.rotation = 0
        self.x_speed = 40
        self.y_speed = 30

        image = pyglet.image.load('spaceship.png')
        image.anchor_x = image.width // 2
        image.anchor_y = image.height // 2
        self.sprite = pyglet.sprite.Sprite(image)
        self.update_sprite()

        objects.append(self)

    def update_sprite(self):
        self.sprite.x = self.x
        self.sprite.y = self.y
        self.sprite.rotation = 90 - math.degrees(self.rotation)  #conversion from radians to degrees (pyglet uses only degrees), also, pyglet's zero is up, ours is on right, that's why 90 -....

    def tick(self,dt):
        #print(pressed_keys)
        rotation_speed = 0
        if key.LEFT in pressed_keys:
            rotation_speed += ROTATION_SPEED
        if key.RIGHT in pressed_keys:
            rotation_speed -= ROTATION_SPEED

        self.rotation += rotation_speed * dt
        self.x += dt*self.x_speed
        self.y += dt*self.y_speed

        self.x %= window.width
        self.y %= window.height
        self.update_sprite()

spaceship = Spaceship()



# Pyglet
window = pyglet.window.Window()

def draw_all_objects():
    window.clear()
    for obj in objects:
        obj.sprite.draw()

def tick_all_objects(dt):
    for obj in objects:
        obj.tick(dt)
def key_pressed(sym,mod):
    pressed_keys.add(sym)

def key_released(sym,mod):
    pressed_keys.discard(sym)

window.push_handlers(
    on_draw=draw_all_objects,
    on_key_press=key_pressed,
    on_key_release=key_released,
)

pyglet.clock.schedule_interval(tick_all_objects, 1/30)

pyglet.app.run()
