import os
import bpy

import compas
from compas.artists import Artist
from compas.artists import clear
from compas.robots import LocalPackageMeshLoader
from compas.robots import RobotModel

# Set high precision to import meshes defined in meters
compas.PRECISION = "12f"

# Prepare mesh loading from local folder
base_path = os.path.join(bpy.path.abspath("//"), "models")
loader = LocalPackageMeshLoader(base_path, "ur_description")

# Create robot model from URDF
model = RobotModel.from_urdf_file(loader.load_urdf("ur3e.urdf"))

# Also load geometry
model.load_geometry(loader)

# Draw model
clear()
artist = Artist(model)
artist.draw_visual()
