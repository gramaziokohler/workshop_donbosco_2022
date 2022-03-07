import time
import random
from compas.artists import Artist
from compas.artists import clear
from compas.artists import redraw
from compas.robots import RobotModel

# Load robot
model = RobotModel.ur5(load_geometry=True)

# Get zero configuration
config = model.zero_configuration()

clear()

artist = Artist(model)

for _ in range(20):
    # Update config randomly
    for j in range(6):
        config.joint_values[j] += random.random() * 0.2 - 0.2

    artist.update(config)
    artist.draw_visual()
    time.sleep(0.02)
    redraw()
