#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist


pub = rospy.Publisher('cmd_vel_mux/input/teleop', Twist, queue_size=1)

rospy.init_node('bot_control')

twist = Twist()

def motion():
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        cmd = input("Enter char: ")
        if cmd == 5:
            twist.linear.x = 0.5
        elif cmd == 1:
            twist.angular.z = 1
        elif cmd == 3:
            twist.angular.z = -1
        elif cmd == 2:
            twist.linear = -0.5
        else:
            twist.linear.x = 0
            twist.angular.z = 0
        pub.publish(twist)
        rate.sleep()


motion()
