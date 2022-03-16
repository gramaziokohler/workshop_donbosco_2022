import math

from rtde_control import RTDEControlInterface as RTDEControl
from rtde_receive import RTDEReceiveInterface as RTDEReceive

from compas.robots import Configuration

if __name__ == "__main__":

    # Create UR Client
    ur_c = RTDEControl("127.0.0.1")
    ur_r = RTDEReceive("127.0.0.1")
    print("Connected.")

    # Print received values
    config = Configuration.from_revolute_values([0] * 6)
    print(config)

    # Move robot the new pos
    speed = 0.5  # rad/s
    accel = 1.4  # rad/s^2
    nowait = False
    ur_c.moveJ(config.joint_values, speed, accel, nowait)

    # End of Code
    print("Finished")
