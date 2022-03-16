import math

from compas_fab.backends import RosClient
from rtde_control import RTDEControlInterface as RTDEControl
from rtde_receive import RTDEReceiveInterface as RTDEReceive

from compas.artists import Artist
from compas.robots import Configuration

if __name__ == "__main__":

    # Create Ros Client
    ros = RosClient()
    ros.run()

    # Load robot and create artist
    robot = ros.load_robot(load_geometry=True)
    artist = Artist(robot.model)
    artist.draw_visual()
    config = robot.zero_configuration()

    # Create UR Client
    ur_c = RTDEControl("127.0.0.1")
    ur_r = RTDEReceive("127.0.0.1")
    print("Connected.")

    # Read value of joints
    robot_joints = ur_r.getActualQ()

    # update visualization
    config.joint_values = robot_joints
    artist.update(config)
    artist.redraw()

    # Print received values
    config = Configuration.from_revolute_values(robot_joints)
    print(config)

    # Change a joint value [°]
    robot_joints[0] += math.radians(15)

    # Move robot the new pos
    speed = 0.5  # rad/s
    accel = 1.4  # rad/s^2
    nowait = False
    ur_c.moveJ(robot_joints, speed, accel, nowait)

    # update visualization
    config.joint_values = robot_joints
    artist.update(config)
    artist.redraw()

    # End of Code
    print("Finished")

    # Close client
    ros.close()
