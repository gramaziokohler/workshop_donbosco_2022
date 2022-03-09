import math
import time

import compas_fab
from compas_fab.backends import RosClient
from compas_fab.robots import CollisionMesh
from compas_fab.robots import PlanningScene

from compas.artists import Artist
from compas.artists import clear
from compas.datastructures import Mesh
from compas.geometry import Frame
from compas.geometry import Transformation
from compas.geometry import Translation

def prepare_scene(robot):
    scene = PlanningScene(robot)
    mesh = Mesh.from_stl(compas_fab.get("planning_scene/floor.stl"))
    cm = CollisionMesh(mesh, "floor")
    scene.add_collision_mesh(cm)

def get_approach_vector(n):
    return (0, 0, .05)

def get_pick_frame(n):
    return Frame((0.3, 0.1, 0.05), (-1, 0, 0), (0, 1, 0))

def get_place_frame(n):
    return Frame((0.4, 0.3, 0.05), (-1, 0, 0), (0, 1, 0))

def get_start_configuration(robot):
    config = robot.zero_configuration()
#    config.joint_values = (-0.106, 5.351, 2.231, -2.869, 4.712, 1.465)
    config.joint_values = (-0.306, 4.351, 2.231, -2.869, 4.712, 1.465)
    return config

def get_number_of_parts():
    return 1

# Settings
TOLERANCE_JOINTS = [math.radians(1)] * 6
PLANNER_ID = "RRT"


def load_planning_scene(robot):
    scene = robot.client.get_planning_scene()
    collision_meshes = []
    attached_collision_meshes = []

    for co in scene.world.collision_objects:
        header = co.header
        frame_id = header.frame_id
        cms = co.to_collision_meshes()

        for cm in cms:
            if cm.frame != Frame.worldXY():
                t = Transformation.from_frame(cm.frame)
                mesh = cm.mesh.transformed(t)
            else:
                mesh = cm.mesh

            collision_meshes.append(mesh)

        for aco in scene.robot_state.attached_collision_objects:
            for acm in aco.to_attached_collision_meshes():
                frame_id = aco.object["header"]["frame_id"]
                frame = robot.forward_kinematics(robot.zero_configuration(), options=dict(link=frame_id))
                t = Transformation.from_frame(frame)

                # Local CM frame
                if (acm.collision_mesh.frame and acm.collision_mesh.frame != Frame.worldXY()):
                    t = t * Transformation.from_frame(acm.collision_mesh.frame)

                mesh = acm.collision_mesh.mesh.transformed(t)

                attached_collision_meshes.append(mesh)

    for cm in collision_meshes + attached_collision_meshes:
        Artist(cm).draw_mesh()


def draw_configurations(robot, configurations, sleep_after=None):
    joint_names = robot.get_configurable_joint_names()
    for config in configurations:
        if len(config.joint_names) == 0:
            config.joint_names = joint_names
        robot.artist.update(config)
        robot.artist.redraw()
        time.sleep(0.04)

    if sleep_after:
        time.sleep(sleep_after)


# PICK & PLACE PROCEDURE

clear()
client = RosClient("localhost")
client.run()

robot = client.load_robot(load_geometry=True)
artist = Artist(robot.model)
artist.draw_visual()
robot.artist = artist

prepare_scene(robot)
load_planning_scene(robot)
start_configuration = get_start_configuration(robot)

print('Start configuration: ', start_configuration)
draw_configurations(robot, [start_configuration], 1)

for i in range(get_number_of_parts()):
    print('Part {}\n--------'.format(i))
    print(' - Testing pick frame + approach vector reachability...')
    pick_frame = get_pick_frame(i)
    approach_pick_frame = pick_frame.transformed(Translation.from_vector(get_approach_vector(i)))

    approach_pick_config = robot.inverse_kinematics(approach_pick_frame, start_configuration)
    draw_configurations(robot, [approach_pick_config], 1)
    print(' - Pick frame + approach vector is reachable!')

    print(' - Testing pick frame reachability...')
    pick_config = robot.inverse_kinematics(pick_frame, approach_pick_config)
    draw_configurations(robot, [pick_config], 1)
    print(' - Pick frame is reachable!')

    print(' - Testing place frame + approach vector reachability...')
    place_frame = get_place_frame(i)
    approach_place_frame = place_frame.transformed(Translation.from_vector(get_approach_vector(i)))

    # we use the approach pick config as start, because we estimate is the closest
    approach_place_config = robot.inverse_kinematics(approach_place_frame, approach_pick_config)
    draw_configurations(robot, [approach_place_config], 1)
    print(' - Place frame + approach vector is reachable!')

    print(' - Testing place frame reachability...')
    place_config = robot.inverse_kinematics(place_frame, approach_place_config)
    draw_configurations(robot, [place_config], 1)
    print(' - Place frame is reachable!')

    print(' - Testing pick path')
    frames = [approach_pick_frame, pick_frame, approach_pick_frame]
    pick_trajectory = robot.plan_cartesian_motion(
        frames,
        approach_pick_config,
        options=dict(
            max_step=0.01,
            avoid_collisions=True,
        ),
    )
    
    if pick_trajectory.fraction < 1.0:
        raise Exception('Found a pick trajectory but it is not complete')
    print(' - Pick path is feasible!')
    draw_configurations(robot, pick_trajectory.points, 1)

    print(' - Testing place path')
    frames = [approach_place_frame, place_frame, approach_place_frame]
    place_trajectory = robot.plan_cartesian_motion(
        frames,
        approach_place_config,
        options=dict(
            max_step=0.01,
            avoid_collisions=True,
        ),
    )
    
    if pick_trajectory.fraction < 1.0:
        raise Exception('Found a place trajectory but it is not complete')
    print(' - Place path is feasible!')
    draw_configurations(robot, place_trajectory.points, 1)

    print(' - Testing free space path')
    goal_constraints = robot.constraints_from_configuration(approach_place_config, 
                                                            tolerances_above=TOLERANCE_JOINTS,
                                                            tolerances_below=TOLERANCE_JOINTS)
    
    freespace_trajectory = robot.plan_motion(
        goal_constraints, approach_pick_config, options=dict(planner_id=PLANNER_ID)
    )
    print(' - Free space path is feasible!')
    draw_configurations(robot, freespace_trajectory.points, 1)

    print(' - Testing start config path')
    goal_constraints = robot.constraints_from_configuration(approach_pick_config, 
                                                            tolerances_above=TOLERANCE_JOINTS,
                                                            tolerances_below=TOLERANCE_JOINTS)
    
    start_trajectory = robot.plan_motion(
        goal_constraints, start_configuration, options=dict(planner_id=PLANNER_ID)
    )
    print(' - Start config path is feasible!')
    draw_configurations(robot, start_trajectory.points, 1)

    print('FULL PICK&PLACE PATH FOUND!')
    draw_configurations(robot, 
        start_trajectory.points +
        pick_trajectory.points +
        freespace_trajectory.points + 
        place_trajectory.points
    , 1)
    

client.close()
