#!/usr/bin/env python

import RPi.GPIO as GPIO
import rospy

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)		# Channel A
GPIO.setup(24, GPIO.IN)		# Channel B
GPIO.setup(25, GPIO.IN)		# Channel Z
global count = 0
global RPM = 0
global direction = 0			
time = rospy.Time(0)	# time = 0 secs

def loadnode():
	rospy.init("wheel_encoder_node")
	read_encoder()
	print_data()

def read_encoder():

	if (GPIO.input(23) and GPIO.input(24)):
		direction = 0	#if high on channel A & B then going forward

	elif (GPIO.input(23) and !GPIO.input(24)):
		direction = 1	#if high on A & low on B then going backwards

	if (GPIO.input(25)):
			count++

	if (time.to_sec() > 10):		#when time is greater than 10 seconds, restart count and time to recalculate rpm
		time = rospy.Time(0)
		clicks = count				#clicks is used to calculate RPM while count is reused. clicks is only initialized after 10 secs of listening
		count = 0					

	if clicks in locals():			#to check if clicks has been initialized
		RPM = clicks * 6

def print_data():

	if direction == 0:
		str1 = "Moving forward "
	if direction == 1:
		str1 = "Moving backward "

	str2 = "at " + str(RPM) + " RPM."

	rospy.loginfo(str1 + str2)

if __name__ == '__main__':
	try:
		loadnode()
	except rospy.ROSInterruptException:
		GPIO.cleanup()
		pass
