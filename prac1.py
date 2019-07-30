#!/usr/bin/python3
"""
Practical 1
Readjust this Docstring as follows:
Names: Ameen Jardine
Student Number: JRDMUH002
Prac: 1
Date: 22/07.2018
"""

# import Relevant Librares
import RPi.GPIO as GPIO
from time import sleep
#Setup 
GPIO.setmode(GPIO.BOARD) #congifures to BOARD mode, so uses board numbering
input_channels=[3,5] #input pins 3 and 5
output_channels = [7,8,10] #output pins 7,8 and 10
GPIO.setup(input_channels,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)  #the  pins 3,5 are set to be inputs
GPIO.setup(output_channels,GPIO.OUT) #the pins 7,8 and 10 are outputs
GPIO.add_event_detect(input_channels[0], GPIO.RISING, bouncetime=200) #sets up an interrupt to be triggered by pin3
GPIO.add_event_detect(input_channels[1], GPIO.RISING, bouncetime=200) #sets up interrupt to be triggered by pin5
#global count,up,down
count =0

# Logic that you write
def main():
    count =0 #variable to be used as index in array of values

    values = [(0,0,0),(0,0,1),(0,1,0),(0,1,1),(1,0,0),(1,0,1),(1,1,0),(1,1,1)] #binary values
    GPIO.output(output_channels,values[0]) #ensures no LEDs are on initially 
    while True:

	if GPIO.event_detected(input_channels[1]): #detects button press for count up
		count+=1
		if count==8:
			count=0 #so that values "wrap around" from highest, jumps to lowest
		print(count)
		GPIO.output(output_channels,values[count]) #Outputs correct value to LEDS

	elif GPIO.event_detected(input_channels[0]): #detects button press for count down
		count-=1 #decrements value
		if count==-1:
			count=7 #7 corresponds to 111 i.e. max value
        	print(count) #displays decimal number on terminal
		GPIO.output(output_channels,values[count]) #Outputs the correct binary number on the LEDS


# Only run the functions if
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
