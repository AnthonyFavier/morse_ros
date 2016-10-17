from morse.builder import *

# set the environment to laas_adream
env = Environment("laas_adream.blend", fastmode=True)
env.set_camera_location([18.0, 4.0, 10.0])
env.set_camera_rotation([1.0, 0.0 , 1.57])

# creates a new instance of the morsy robot
morsy = Morsy()

# add clock
clock = Clock()
clock.add_interface("ros", topic="clock")
morsy.append(clock)

env.use_relative_time(True)
env.create()
