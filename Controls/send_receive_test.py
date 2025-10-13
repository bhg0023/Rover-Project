from pymavlink import mavutil

# Sets up communication interface between the PixHawk and the Jetson
# Using UART with BAUD rate: 115200
connection = mavutil.mavlink_connection('/dev/ttyTHS1', 115200)
connection.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" % (connection.target_system, connection.target_component))


''' set_pwm - Function definition
Parameters:
    direction: -1 --> reverse
                0 --> neutral
                1 --> forward

          PWM: range from 0-100 
Return:
    pwm_send: float indicating the pwm signal that will be sent to the pixhawk
'''
def set_pwm(direction, pwm):
    pwm_send = 1000
    '''     #### use if python version is not above 3.10
    # if direction == 0: # Neutral
    #     pwm_send = 0
    # elif direction == 1: # Forward
    #     pwm_send = pwm/100
    # elif direction == -1:
    #     pwm_send = -(pwm/100)
    '''
    match direction:
        case -1: # reverse
            pwm_send = -(pwm/100)
        case 0:  # neutral
            pwm_send = 0
            print("hello 0")
        case 1:  # forward
            pwm_send = pwm/100

    connection.mav.command_long_encode(
        connection.target_system,
        connection.target_component, 
        mavutil.mavlink.MAV_CMD_DO_SET_ACTUATOR, 
        0, 
        pwm_send, # Actuator 1 
        'NaN',    # Actuator 2
        'NaN',    # Actuator 3
        'NaN',    # Actuator 4
        'NaN',    # Actuator 5
        'NaN',    # Actuator 6
        0         # Index of actuator set
    )

    return pwm_send


# Initialize PWM
user_pwm = 0
set_direction = 1
set_pwm(set_direction, user_pwm)

print("Default direction: Forward")
while(user_pwm != -1):
    user_pwm = int(input("PWM duty cycle [0-100] (1000 to change direction): "))
    if (user_pwm == 1000):
        set_direction = int(input("Set direction \n\treverse = -1, \n\tneutral = 0, \n\tforward = 1\n:: ")) 
        user_pwm = int(input("PWM duty cycle [0-100]: "))
    print(str(set_pwm(set_direction, user_pwm)))   
