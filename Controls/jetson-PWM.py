import Jetson.GPIO as GPIO

pin = 32
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)

pwm = GPIO.PWM(pin, 150)

pwm.start(22.5)
