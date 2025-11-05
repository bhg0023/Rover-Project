import Jetson.GPIO as GPIO

pin = 32
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)

# Setting pwm to 150 Hz
pwm = GPIO.PWM(pin, 150)

# Neutral state (1.5 ms) is at 22.5% DC for f = 150 Hz
# Initialize PWM to 22.5% DC
pwm.start(22.5)


# Conversion
def conv_pwm(dc_motor):
    dc_jetson = (3/40)*dc_motor + 22.5
    if (dc_jetson > 30):
        dc_jetson = 30
    elif (dc_jetson < 15 ):
        dc_jetson = 15
    return dc_jetson

set_pwm = int(input("Enter new pwm: "))
while(set_pwm != 1000):
    pwm.ChangeDutyCycle(conv_pwm(set_pwm))
    set_pwm = int(input("Enter new pwm (1000 to end): "))

pwm.stop()
GPIO.cleanup()
