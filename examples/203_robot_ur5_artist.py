from compas.artists import Artist
from compas.artists import clear
from compas.robots import RobotModel

model = RobotModel.ur5(load_geometry=True)

clear()
artist = Artist(model)
artist.draw_visual()
