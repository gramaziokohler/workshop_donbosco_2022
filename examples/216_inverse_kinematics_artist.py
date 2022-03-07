import time

from compas_fab.backends.kinematics.solvers import UR5Kinematics

from compas.artists import Artist
from compas.artists import clear
from compas.geometry import Frame
from compas.robots import RobotModel

model = RobotModel.ur5(load_geometry=True)

f = Frame((0.417, 0.191, -0.005), (-0.000, 1.000, 0.000), (1.000, 0.000, 0.00))

solutions = UR5Kinematics().inverse(f)

clear()
artist = Artist(model)

for jv in solutions:
    config = model.zero_configuration()
    config.joint_values = jv
    artist.update(config)
    artist.draw_visual()
    artist.redraw()
    time.sleep(1)
