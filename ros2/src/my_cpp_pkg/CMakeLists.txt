cmake_minimum_required(VERSION 3.8)
project(my_cpp_pkg)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)

# Add the executable
add_executable(my_first_node src/my_first_node.cpp)
add_executable(my_oops_node src/my_oops_node.cpp)
add_executable(subscriber_node src/subscriber_node.cpp)
# Link libraries
ament_target_dependencies(my_first_node rclcpp)
ament_target_dependencies(my_oops_node rclcpp)
ament_target_dependencies(subscriber_node rclcpp std_msgs)

# Install the executable
install(TARGETS
  my_first_node
  my_oops_node
  subscriber_node

  DESTINATION lib/${PROJECT_NAME}
)


if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # comment the line when a copyright and license is added to all source files
  set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # comment the line when this package is in a git repo and when
  # a copyright and license is added to all source files
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
