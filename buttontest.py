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
GPIO.setmode(GPIO.BOARD) #configures to BOARD mode, so uses board numbering
input_channel= 3 #input pin 3
output_channel = 7 #output pins 7
GPIO.setup(input_channel,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)  #pin 3 is an input
GPIO.setup(output_channel,GPIO.OUT) #pin 7 is an output
GPIO.add_event_detect(input_channel, GPIO.RISING,bouncetime=200) #sets up an interrupt to be triggered by pin3
state = False

# Logic that you write
def main():
    state = False
    while True:
	if GPIO.event_detected(input_channel):
		state =not state #toggles

        if state==True:
        	GPIO.output(7,1) #Outputs high to pin 7

   	else:
	 	GPIO.output(7,0) #Outputs a low to pin 7

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
