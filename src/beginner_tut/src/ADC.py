#!/usr/bin/env python

#must get adc library from https://github.com/adafruit/Adafruit_Python_ADS1x15.git
#check https://learn.adafruit.com/raspberry-pi-analog-to-digital-converters/ads1015-slash-ads1115
#channels 0-3 are conneted to potentiameter, and chip connects to SDA and SCL on pi

import RPi.GPIO as GPIO
import rospy
from Adafruit_ADS1x15 import ADS1115
adc = ADS1115() #declares adc as an object of the ADS1115 class
r = rospy.Rate(10) #10 Hz

def reader():   
	pot1 = 0 #intialize potentiameters & use them as 4 ch of adc
	pot2 = 1
	pot3 = 2
	pot4 = 3

	while not rospy.is_shutdown():
		val1 = adc.read_adc(pot1, 0)
		val2 = adc.read_adc(pot2, 0)
		val3 = adc.read_adc(pot3, 0)
		val4 = adc.read_adc(pot4, 0)

		rospy.loginfo("Potentiameter 1 reading: " + str(val1))
		rospy.loginfo("Potentiameter 2 reading: " + str(val2))
		rospy.loginfo("Potentiameter 3 reading: " + str(val3))
		rospy.loginfo("Potentiameter 4 reading: " + str(val4))
		r.sleep()

if __name__ == '__main__':
	try:
		rospy.init_node('ADC_node', anonymous=True)
		reader()
	except rospy.ROSInterruptException:
		pass
