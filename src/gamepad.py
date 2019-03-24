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
       if(event.code == "ABS_X" and event.state == 255):
          direction = "l"
       if(event.code == "ABS_Y" and event.state == 0):
          direction = "i"
       if(event.code == "ABS_Y" and event.state == 255):
          direction = ","
       if(event.code == "BTN_PINKIE" and event.state == 1):
          direction = "L"
       if(event.code == "BTN_TOP2" and event.state == 1):
          direction = "J"
       return direction

def gamepad():
   rospy.init_node('teleop_twist_gamepad')
   pub = rospy.Publisher('cmd_vel', Twist, queue_size = 10)
   twist = Twist()
   button = getButton()
   if(button == "i"):
      twist.linear.x = 0.5
      pub.publish(twist)
   if(button == ","):
      twist.linear.x = -0.5
      pub.publish(twist)
   if(button == "j"):
      twist.angular.z = 1
      pub.publish(twist)
   if(button == "l"):
      twist.angular.z = -1
      pub.publish(twist)


if __name__ == '__main__':
    try:
        while(1):
           gamepad()

    except rospy.ROSInterruptException:
        pass


