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
GPIO.setup(input_channels,GPIO.IN)  #the  pins 3,5 are set to be inputs
GPIO.setup(output_channels,GPIO.OUT) #the pins 7,8 and 10 are outputs
GPIO.add_event_detect(input_channels[0], GPIO.RISING, bouncetime=200) #sets up an interrupt to be triggered by pin3
GPIO.add_event_detect(input_channels[1], GPIO.RISING, bouncetime=200) #sets up interrupt to be triggered by pin5
#global count,up,down
count =0

# Logic that you write
def main():
    while True:
   	 GPIO.output(7,1) #Outputs high to pin 7
   	 sleep(1) #delay for 1 second
	 GPIO.output(7,0) #outputs a low to pin 7
	 sleep(1)
	


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
