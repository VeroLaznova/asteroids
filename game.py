import pyglet


# Global state:
objects = []

# Clases:
class Spaceship:
    def __init__ (self):
        self.x = 20
        self.y = 40
        self.rotation = 0
        self.x_speed = 1
        self.y_speed = 3

        image = pyglet.image.load('spaceship.png')
        self.sprite = pyglet.sprite.Sprite(image)
        self.update_sprite()

        objects.append(self)

    def update_sprite(self):
        self.sprite.x = self.x
        self.sprite.y = self.y

    def tick(self,dt):
        self.x += dt*self.x_speed
        self.x += dt*self.y_speed
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

window.push_handlers(
    on_draw = draw_all_objects,
)

pyglet.clock.schedule_interval(tick_all_objects, 1/30)

pyglet.app.run()
