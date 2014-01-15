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

# mark morse_config files for installation
install(FILES
  morse_config/robot_urdf/pr2.urdf
  morse_config/robot_urdf/readme
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/morse_config/robot_urdf
)
install(FILES
  morse_config/blender_files/tum_kitchen.blend
  morse_config/blender_files/laas_adream.blend
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/morse_config/blender_files
)
install(FILES
  morse_config/morse_scripts/tum_kitchen_scenario.py
  morse_config/morse_scripts/laas_adream_scenario.py
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/morse_config/morse_scripts
)
install(FILES
  morse_config/maps/tum_kitchen_map.yaml
  morse_config/maps/tum_kitchen_map.pgm
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/morse_config/maps
)

# mark move_base_config files for installation
install(FILES
  move_base_config/base_local_planner_params.yaml
  move_base_config/costmap_common_params.yaml
  move_base_config/dwa_local_planner_params.yaml
  move_base_config/global_costmap_params.yaml
  move_base_config/local_costmap_params.yaml
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/move_base_config
)

# mark launch files for installation
install(FILES
  launch/pr2.launch
  launch/map.launch
  launch/locate.launch
  launch/nav.launch
  launch/pr2_tum_kitchen.launch
  launch/pr2_laas_adream.launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/launch
)

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
