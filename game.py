import pyglet


# Global state:
objects = []

# Clases:
class Spaceship:
    def __init__ (self):
        self.x = 0
        self.y = 0
        self.rotation = 0
        self.x_speed = 0
        self.y_speed = 0
        image = pyglet.image.load('spaceship.png')
        self.sprite = pyglet.sprite.Sprite(image)
        objects.append(self)

spaceship = Spaceship()




# Pyglet
window = pyglet.window.Window()

def draw_all_objects():
    window.clear()
    for obj in objects:
        obj.sprite.draw()

window.push_handlers(
    on_draw = draw_all_objects,
)
pyglet.app.run()
