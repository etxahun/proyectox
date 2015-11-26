import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)  # set board mode to Broadcom
GPIO.setwarnings(False)

GPIO.setup(24, GPIO.OUT)  # set up pin 18

GPIO.output(24, 0)  # turn on pin 18
