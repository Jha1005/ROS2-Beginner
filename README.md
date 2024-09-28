System Requirements
 <br>
Ubuntu Linux (recommended)
<br> Ubuntu 22.04 LTS (Jammy Jellyfish)

Installation 
<br>
link => https://docs.ros.org/en/humble/Installation.html

<br>
Creating a ROS2 Workspace

Create a new directory for your workspace:

mkdir -p ~/ros2_ws/src
cd ~/ros2_ws

Build the workspace:

bashCopycolcon build

Source the workspace:

bashCopysource ~/ros2_ws/install/setup.bash
Creating Packages
Python Package

Navigate to the src directory:

bashCopycd ~/ros2_ws/src

Create a new Python package:

bashCopyros2 pkg create --build-type ament_python my_py_pkg

Create a Python node:

bashCopycd my_py_pkg
mkdir my_py_pkg/my_node
touch my_py_pkg/my_node/my_node.py

Edit my_py_pkg/my_node/my_node.py with your preferred text editor and add your node code.

C++ Package

Navigate to the src directory:

bashCopycd ~/ros2_ws/src

Create a new C++ package:

ros2 pkg create --build-type ament_cmake my_cpp_pkg

Create a C++ node:

bashCopycd my_cpp_pkg
mkdir src
touch src/my_node.cpp

Edit src/my_node.cpp with your preferred text editor and add your node code.
Update CMakeLists.txt to build your node.

Building the Workspace
After creating or modifying packages, build your workspace:
bashCopycd ~/ros2_ws
colcon build
To build only specific packages:
bashCopycolcon build --packages-select my_py_pkg my_cpp_pkg
Running Nodes

Source your workspace:

bashCopysource ~/ros2_ws/install/setup.bash

Run a Python node:

bashCopyros2 run my_py_pkg my_node

Run a C++ node:

bashCopyros2 run my_cpp_pkg my_node
Useful Commands

List all packages in the workspace:
bashCopyros2 pkg list

List all nodes currently running:
bashCopyros2 node list

List all topics:
bashCopyros2 topic list
