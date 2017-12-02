#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan


range_ahead = 1 #just to initialize

def callback(msg):
    global range_ahead
    range_ahead = min(msg.ranges)

sub = rospy.Subscriber('scan', LaserScan , callback)
pub = rospy.Publisher('cmd_vel_mux/input/teleop', Twist, queue_size = 1)
rospy.init_node('wander')
change_time = rospy.Time.now() + rospy.Duration(5)
forward = True
r = rospy.Rate(10)

while not rospy.is_shutdown():
    twist = Twist()
    
    if forward:
        twist.linear.x = 1
        if (range_ahead < 0.8 or rospy.Time.now() > change_time):
            forward = False
            change_time = rospy.Time.now() + rospy.Duration(5)
    else:
        twist.angular.z = 1
        if (range_ahead > 0.8 or rospy.Time.now() > change_time):
            forward = True
            change_time = rospy.Time.now() + rospy.Duration(30)
            
    pub.publish(twist)
    r.sleep()
