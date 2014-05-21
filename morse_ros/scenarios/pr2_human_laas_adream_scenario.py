from morse.builder import *

# pr2 robot with laser (scan) and odometry (odom) sensors, and actuators for armature (joint_trajectory_contorller) asnd wheels (cmd_vel) to the scene
pr2 = NavPR2()
pr2.add_interface("ros")

# adding human model
human = Human()
human.properties(WorldCamera = True)

# set the environment to laas_adream
env = Environment('laas_adream.blend')
env.set_camera_location([18.0, 4.0, 10.0])
env.set_camera_rotation([1.0, 0.0 , 1.57])

# put the robot and human in better places
pr2.rotate(x=0.0, y=0.0, z=0.0)       # for roation check on the pr2
pr2.translate(x=2.0, y=2.0, z=0.0)
human.translate(x=3.0, y=4.0, z=0.0)
human.rotate(x=0.0, y=0.0, z=0.0)
