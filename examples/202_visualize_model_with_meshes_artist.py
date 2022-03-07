import os
import bpy

from compas.artists import Artist
from compas.artists import clear
from compas.robots import LocalPackageMeshLoader
from compas.robots import RobotModel

base_path = bpy.path.abspath("//")
urdf_path = os.path.join(base_path, "models", "06_origins_meshes.urdf")

model = RobotModel.from_urdf_file(urdf_path)

loader = LocalPackageMeshLoader(os.path.join(base_path, "models"), "basic")
model.load_geometry(loader)

clear()
artist = Artist(model)
artist.draw_visual()
