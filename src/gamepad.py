#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from inputs import devices, get_gamepad
from geometry_msgs.msg import Twist

def getButton():
    direction = "k"
    events = get_gamepad()
    for event in events:
       if(event.code == "ABS_X" and event.state == 0):
          direction = "j"
       elif(event.code == "ABS_X" and event.state == 255):
          direction = "l"
       elif(event.code == "ABS_Y" and event.state == 0):
          direction = "i"
       elif(event.code == "ABS_Y" and event.state == 255):
          direction = ","
       elif(event.code == "BTN_PINKIE" and event.state == 1):
          direction = "L"
       elif(event.code == "BTN_TOP2" and event.state == 1):
          direction = "J"
    return direction

if __name__ == '__main__':
    try:
        pub = rospy.Publisher('cmd_vel', Twist, queue_size = 2)
        rospy.init_node('gamepad_control')
        twist = Twist()
        if(getButton() == "i"):
           twist.linear.y = 0.5
           pub.publish(twist)

    except rospy.ROSInterruptException:
        pass

#rospy.spin()

