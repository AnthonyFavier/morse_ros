from morse.builder import *

# pr2 robot with laser (scan) and odometry (odom) sensors, and actuators
#  for armature (joint_trajectory_contorller) and wheels (cmd_vel) to the scene
pr2 = NavPR2()
pr2.add_interface("ros")

# set the environment to tum_kitchen
env = Environment('tum_kitchen.blend', fastmode=True)
env.set_camera_location([10.0, -10.0, 10.0])
env.set_camera_rotation([1.0470, 0, 0.7854])

# add clock
clock = Clock()
clock.add_interface("ros", topic="clock")
pr2.append(clock)

# create teleport actuator
teleport = Teleport()
teleport.add_interface("ros", topic="pr2_teleport_pose")
pr2.append(teleport)

# put the robot in some good place
pr2.translate(2.5, 3.2, 0.0)

env.use_relative_time(True)
env.create()
