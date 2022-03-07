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
artist.draw_visual()

steps = [random.random() * 0.2 - 0.2 for _ in range(6)]

for _ in range(20):
    # Update config randomly
    for j in range(6):
        config.joint_values[j] += steps[j]

    artist.update(config)
    artist.redraw()
    time.sleep(0.02)
