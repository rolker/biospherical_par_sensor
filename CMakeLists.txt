cmake_minimum_required(VERSION 2.8.3)
project(biospherical_par_sensor)

find_package(catkin REQUIRED COMPONENTS
  rospy message_generation std_msgs
)

catkin_python_setup()

add_message_files(
  FILES
  par.msg
)

generate_messages(
  DEPENDENCIES
  std_msgs
)

catkin_package(
  CATKIN_DEPENDS rospy 
)

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

