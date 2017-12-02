#!/usr/bin/env python

import rospy
import serial

PORT = '/dev/ttyS0'     #port taken from wheel_velocity.py, does port change or is this always the same for sabertooth?
BUS = serial.Serial(PORT)

def serialWriter(direction, speed, address):
	checksum = (address + direction + speed) & 127
	BUS.write(chr(address))     #address for sabertooth
	BUS.write(chr(direction))   #direction for motors 1 & 2 (0 or 1 and 4 or 5)
	BUS.write(chr(speed))       #between 0 - 127
	BUS.write(chr(checksum))    #checksum is double checking mechanism of sabertooth
	rospy.loginfo("Address: " + str(address) + " direction: " + str(direction) + " speed: " + str(speed))

def initiate_motor():
	rospy.init_node('saber_node' , anonymous = True)
	while not rospy.is_shutdown():
		serialWriter(0,50,129) #hard code commands here also must hard code speed = 0 for motor to stop

if __name__ == '__main__':
	try:
		intiate_motor()
	except rospy.ROSInterruptException:  #question: can i put a serialWriter(0,0,address) and serialWriter(4,0,address) in this exception to avoid zombie motor?
		pass

