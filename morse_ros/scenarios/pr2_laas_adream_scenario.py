from morse.builder import *

# pr2 robot with laser (scan) and odometry (odom) sensors, and actuators
#  for armature (joint_trajectory_contorller) asnd wheels (cmd_vel) to the scene
pr2 = NavPR2()
pr2.add_interface("ros")

# set the environment to laas_adream
env = Environment('laas_adream.blend', fastmode=True)
env.set_camera_location([18.0, 4.0, 10.0])
env.set_camera_rotation([1.0, 0.0 , 1.57])

# put the robot in better place
pr2.rotate(x=0.0, y=0.0, z=0.0)       # for roation check on the pr2
pr2.translate(x=2.0, y=2.0, z=0.0)    # put pr2 in some good place

# add clock
clock = Clock()
clock.add_stream("ros")
pr2.append(clock)

env.use_relative_time(True)
env.create()
