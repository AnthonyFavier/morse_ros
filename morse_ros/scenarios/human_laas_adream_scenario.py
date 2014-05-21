from morse.builder import *

# adding human model
human = Human()
human.properties(WorldCamera = True)

# pose sensor for the human
pose = Pose()
human.append(pose)
pose.add_interface('ros')

# set the environment to laas_adream
env = Environment('laas_adream.blend')
env.set_camera_location([18.0, 4.0, 10.0])
env.set_camera_rotation([1.0, 0.0 , 1.57])

# put the human in better places
human.translate(x=3.0, y=4.0, z=0.0)
human.rotate(x=0.0, y=0.0, z=0.0)
