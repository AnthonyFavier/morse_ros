from morse.builder import *

# pr2 robot with laser (scan) and odometry (odom) sensors, and actuators for armature (joint_trajectory_contorller) asnd wheels (cmd_vel) to the scene
pr2 = NavPR2()
pr2.add_interface("ros")

# adding human model
human = Human()
human.properties(WorldCamera = True)

# pose sensor for the human
pose = Pose()
human.append(pose)
pose.add_interface('ros')

# set the environment to tum_kitchen
env = Environment('tum_kitchen.blend')
env.set_camera_location([10.0, -10.0, 10.0])
env.set_camera_rotation([1.0470, 0, 0.7854])

# put the robot and human in better places
pr2.rotate(x=0.0, y=0.0, z=0.0)       # for roation check on the pr2
pr2.translate(x=2.5, y=3.2, z=0.0)    # put pr2 in some good place
human.translate(x=6.0, y=0.7, z=0.0)
human.rotate(x=0.0, y=0.0, z=-3.0)
