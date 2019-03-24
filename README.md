# gamepad_teleop

ROS node to control robot in teleop mode with USB game controller (SNES). Publishes to the `cmd_vel` topic.

To use:

1. `cd ~/catkin_ws/src`
2. `git clone https://github.com/marshallpowell97/gamepad_teleop.git`
3. `sudo pip install inputs`
4. `cd catkin_ws && catkin_make`
5. Launch with `roslaunch gamepad_teleop gamepad.launch`
