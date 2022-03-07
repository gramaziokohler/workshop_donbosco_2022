from compas.artists import Artist
from compas.artists import clear
from compas.robots import RobotModel

model = RobotModel.ur5(load_geometry=True)

config = model.zero_configuration()
frame = model.forward_kinematics(config)

clear()
artist = Artist(frame)
artist.draw_origin()
artist.draw_axes()

artist = Artist(model)
artist.update(config)
artist.draw_visual()
