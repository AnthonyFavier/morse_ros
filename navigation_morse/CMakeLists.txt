cmake_minimum_required(VERSION 2.8.3)
project(navigation_morse)



## set up ##

## set the files
set(ROS_DEPS
  morse_ros
)

### set of packages whose message types this package use
#set(MSG_DEP_SET
#)

#set(MSG_FILES
#)

#set(SRV_FILES
#)

#set(ACT_FILES
#)

##
find_package(catkin REQUIRED COMPONENTS
#  message_generation
  ${ROS_DEPS}
#  ${MSG_DEP_SET}
)

## system dependencies are found with CMake's conventions
# find_package(Boost REQUIRED COMPONENTS system)

## add message, serviece and action files
#add_message_files(DIRECTORY msg FILES ${MSG_FILES})
#add_service_files(DIRECTORY srv FILES ${SRV_FILES})
#add_action_files(DIRECTORY action FILES ${ACT_FILES})

## generate added messages and services with any dependencies listed here
#generate_messages(
#  DEPENDENCIES
#  ${MSG_DEP_SET}
#)

## configure and declare catkin pakcage
catkin_package(
#  INCLUDE_DIRS
#    include
#  LIBRARIES person_publisher
#  CATKIN_DEPENDS
#    message_runtime
#    ${ROS_DEPS}
#    ${MSG_DEP_SET}
#  DEPENDS system_lib
)



## Build ##

## include catking include directories
#include_directories(
#  ${catkin_INCLUDE_DIRS}
#)

## declare a cpp library
#  add_library(person_publisher
#    src/${PROJECT_NAME}/navigation_morse.cpp
#  )

## declare a cpp executable
#  add_executable(navigation_morse_node src/navigation_morse_node.cpp)

## cmake target dependencies of the executable/library
#  add_dependencies(navigation_morse_node navigation_morse_generate_messages_cpp)

## libraries to link a library or executable target against
#  target_link_libraries(navigation_morse_node
#    ${catkin_LIBRARIES}
#  )



## Install ##

## executable scripts (python etc.) for installation
# install(PROGRAMS
#   scripts/start_morse.sh
#   DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
# )

# install launch, map, move_base_config and rviz files
foreach(dir launch maps move_base_config rviz)
   install(DIRECTORY ${dir}/
      DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir})
endforeach(dir)

## executables and/or libraries for installation
# install(TARGETS person_publisher person_publisher_node
#   ARCHIVE DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
#   LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
#   RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
# )

## cpp-header files for installation
# install(DIRECTORY include/${PROJECT_NAME}/
#   DESTINATION ${CATKIN_PACKAGE_INCLUDE_DESTINATION}
#   FILES_MATCHING PATTERN "*.h"
#   PATTERN ".svn" EXCLUDE
# )

## other files for installation
# install(FILES
#   # myfile1
#   DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
# )



## Testing ##

## add catch based cpp test target
# catkin_add_gtest(${PROJECT_NAME}-test test/test_person_publisher.cpp)
# if(TARGET ${PROJECT_NAME}-test)
#   target_link_libraries(${PROJECT_NAME}-test ${PROJECT_NAME})
# endif()

# catkin_add_nosetests(test)