#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from ar_track_alvar_msgs.msg import AlvarMarkers
#from PoseStamped.msg import geometry_msgs 

pub = rospy.Publisher("turtle1/cmd_vel", Twist, queue_size = 10)

def callback(data):
     twist = Twist()
     size = len(data.markers)
     if data.markers:
          linear = 0
          angular = 0
          for i in range(0,size):
               linear += data.markers[i].pose.pose.position.y
               angular += data.markers[i].pose.pose.position.x
          linear = linear/size
          angular = angular/size
          if abs(linear) > abs(angular):
               twist.linear.x = -10*linear
          elif abs(linear) < abs(angular):
               twist.angular.z = 4*angular
          pub.publish(twist)

def mainloop():
    rospy.Subscriber("/ar_pose_marker", AlvarMarkers, callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        rospy.init_node('ARTurtle', anonymous = True)
        mainloop()
    except rospy.ROSInterruptException:
        pass
