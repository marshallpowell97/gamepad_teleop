#! /usr/bin/env python

from __future__ import print_function

import rospy
from geometry_msgs.msg import Twist
from inputs import devices, get_gamepad



def main():

    while 1:
        events = get_gamepad()
        for event in events:
               print(event.code)


if __name__ == "__main__":
    main()
