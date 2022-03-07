# Before running this example, make sure to run
# "docker compose up" on the docker folder
from compas_fab.backends import RosClient

from compas.artists import Artist
from compas.artists import clear

clear()

# Load robot and its geometry
with RosClient("localhost") as ros:
    robot = ros.load_robot(load_geometry=True)
    robot.info()

    artist = Artist(robot.model)
    artist.draw_visual()
