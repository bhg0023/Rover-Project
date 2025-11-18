from pymavlink import mavutil
import time

# Sets up communication interface between the PixHawk and the Jetson
# Using UART with BAUD rate: 57600
connection = mavutil.mavlink_connection('/dev/ttyTHS1', 57600)
connection.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" % (connection.target_system, connection.target_component))

message = connection.mav.command_long_encode(
    connection.target_system,
    connection.target_component,
    mavutil.mavlink.MAV_CMD_DO_SET_SERVO, 
    0, 
    1, 
    1000,
    0, 0, 0, 0, 0
)

connection.mav.send(message)

user_input = float(input("enter something"))
while(user_input != -1.0):
    user_input = float(input("PWM (micro sec):"))
    message = connection.mav.command_long_encode(
        connection.target_system,
        connection.target_component,
        mavutil.mavlink.MAV_CMD_DO_SET_SERVO, 
        0, 
        1, 
        user_input,
        0, 0, 0, 0, 0
    )
    connection.mav.send(message)
