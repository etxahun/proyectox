import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)  # set board mode to Broadcom
GPIO.setwarnings(False)

GPIO.setup(24, GPIO.OUT)  # set up pin 18

GPIO.output(24, 1) # turn off pin 18
