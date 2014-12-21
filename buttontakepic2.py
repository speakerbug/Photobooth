import time
import picamera
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

right_button = 3
left_button = 5

GPIO.setup(right_button, GPIO.IN)
GPIO.setup(left_button, GPIO.IN)

while GPIO.input(left_button) and GPIO.input(right_button):
    pass
    if GPIO.input(left_button) == False:
        print("Left button pressed")
    if GPIO.input(right_button) == False:
        print("Right button pressed")