#!/usr/bin/env python

import RPi.GPIO as GPIO
import rospy
from hx711 import HX711

hx = HX711(5, 6)					#( gpio input 5 and dout on HX, gpio output 6 and clock on HX)
hx.set_reading_format("LSB", "MSB") #sets idk honestly
hx.set_reference_unit(10.3)			#turns input into kg
hx.reset()							#restarts chip
hx.tare()							#zeroes the scale / accounts for mass of hopper


def loadpub():
	rospy.init_node("hx_node")		#node name hx_node		
	readCell()

def readCell():
    while not rospy.is_shutdown():
        val = hx.get_weight_med(5)											#reads 5 data points and return median
        rospy.set_param('/weight', abs(val))								#sets weight to absolute of val
		rospy.loginfo( "weight is " + str(rospy.get_param("/weight")))		#prints to rosout 
        hx.reset()

if __name__ == '__main__':
	try:
		loadpub()
	except rospy.ROSInterruptException:
		GPIO.cleanup()
		pass
