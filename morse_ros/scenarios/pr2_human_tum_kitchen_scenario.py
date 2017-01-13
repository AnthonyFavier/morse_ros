from morse.builder import *

# pr2 robot with laser (scan) and odometry (odom) sensors, and actuators
#  for armature (joint_trajectory_contorller) and wheels (cmd_vel) to the scene
pr2 = NavPR2()
pr2.add_interface("ros")

# teleport actuator for the pr2
teleport_pr2 = Teleport()
pr2.append(teleport_pr2)
teleport_pr2.add_interface("ros", topic="pr2_teleport_pose")

# adding human model
human = Human()
human.properties(WorldCamera = True)

# pose sensor for the human
pose = Pose()
human.append(pose)
pose.add_interface("ros", topic="human_pose")

# teleport actuator for the human
teleport_human = Teleport()
human.append(teleport_human)
teleport_human.add_interface("ros", topic="human_teleport_pose")

# set the environment to tum_kitchen
env = Environment("tum_kitchen.blend", fastmode=True)
env.set_camera_location([10.0, -10.0, 10.0])
env.set_camera_rotation([1.0470, 0, 0.7854])

# put the robot and human in some good places
pr2.translate(2.5, 3.2, 0.0)
human.translate(6.0, 0.7, 0.0)
human.rotate(0.0, 0.0, -3.0)

# add clock
clock = Clock()
clock.add_interface("ros", topic="clock")
pr2.append(clock)
human.append(clock)

env.use_relative_time(True)
env.create()
