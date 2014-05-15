cmake_minimum_required(VERSION 2.8.3)
project(navigation_morse)

## Find catkin macros and libraries
find_package(catkin REQUIRED COMPONENTS
  morse_ros
)

###################################
## catkin specific configuration ##
###################################
catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES navigation_morse
#  CATKIN_DEPENDS other_catkin_pkg
#  DEPENDS system_lib
)

###########
## Build ##
###########

## Specify additional locations of header files
## Your package locations should be listed before other locations
# include_directories(include)

## Declare a cpp library
# add_library(navigation_morse
#   src/${PROJECT_NAME}/navigation_morse.cpp
# )

## Declare a cpp executable
# add_executable(navigation_morse_node src/navigation_morse_node.cpp)

## Add cmake target dependencies of the executable/library
## as an example, message headers may need to be generated before nodes
# add_dependencies(navigation_morse_node navigation_morse_generate_messages_cpp)

## Specify libraries to link a library or executable target against
# target_link_libraries(navigation_morse_node
#   ${catkin_LIBRARIES}
# )

#############
## Install ##
#############

# all install targets should use catkin DESTINATION variables
# See http://ros.org/doc/api/catkin/html/adv_user_guide/variables.html
foreach(dir morse_config/robot_urdf morse_config/blender_files morse_config/morse_scripts morse_config/maps move_base_config launch)
   install(DIRECTORY ${dir}/ 
      DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir})
endforeach(dir)

#############
## Testing ##
#############

## Add gtest based cpp test target and link libraries
# catkin_add_gtest(${PROJECT_NAME}-test test/test_navigation_morse.cpp)
# if(TARGET ${PROJECT_NAME}-test)
#   target_link_libraries(${PROJECT_NAME}-test ${PROJECT_NAME})
# endif()

## Add folders to be run by python nosetests
# catkin_add_nosetests(test)
