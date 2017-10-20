#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def mainloop():
	pub = rospy.Publisher("chatter" , String, queue_size = 10)
	rospy.loginfo("entered mainloop()") #prints message to terminal
	rate = rospy.Rate(10) #sets loop speed to 10Hz
	while not rospy.is_shutdown():
                str_hello = "Hello from Python"
		pub.publish(str_hello)
		rate.sleep()

if __name__ == '__main__':
	try:
		rospy.init_node('Hello', anonymous = True)
		mainloop()
	except rospy.ROSInterruptException:
		pass
