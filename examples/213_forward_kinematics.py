from compas.robots import RobotModel

model = RobotModel.ur5(load_geometry=False)

# Get some relevant link names for FK
print(model.get_base_link_name())
print(model.get_end_effector_link_name())

# Create config
config = model.zero_configuration()

# Get FK for tip
print(model.forward_kinematics(config))
# Get FK for base
print(model.forward_kinematics(config, link_name=model.get_base_link_name()))
