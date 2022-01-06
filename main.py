from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

window.borderless = False
window.title = 'pytol 2'


def update():
    cube.rotation_x += time.dt * 20

    if held_keys["escape"]:
        if menu:
            application.quit()
        else:
            application.paused = True


# create a window
app = Ursina()

# make a cube
cube = Entity(model="cube", collider="mesh", color=color.rgb(32, 174, 130), position=(-47, 2, 0), rotation=(45, 45, 0),
              texture="white_cube", double_sided=True)
platform = Entity(texture_scale=(32, 32), model="plane", collider="mesh", texture="floor.png", scale=(100, 10, 100),
                  double_sided=True)
top = duplicate(platform, position=(0, 30, 0), rotation_z=180)
left = duplicate(platform, position=(-50, 15, 0), rotation_z=90, scale_=(30, 30, 30), texture="wall.png",texture_scale=(32, 22))
# run it

player = FirstPersonController(speed=9, jump_height=3, jump_up_duration=1)
player.cursor.enabled = True
player.cursor.model = Entity(parent=camera.ui, model='quad', texture="pcro.png", scale=(.02, .035),
                             color=color.white, )
Sky()
player.disable()
bg = Entity(model='quad', scale=())
logo = Entity(model="quad", scale=(.7, .3), texture="title", position=(.5, .2))
logo.parent = camera.ui
window.fullscreen = True
camera.position = (-43, .2, 1)
camera.rotation = (0, -85, 0)
menu = True
app.run()
