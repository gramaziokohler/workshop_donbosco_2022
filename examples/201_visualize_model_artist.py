import os
import bpy

from compas.artists import Artist
from compas.artists import clear
from compas.robots import RobotModel

base_path = bpy.path.abspath("//")
urdf_path = os.path.join(base_path, "models", "01_myfirst.urdf")

model = RobotModel.from_urdf_file(urdf_path)

clear()
artist = Artist(model)
artist.draw_visual()
