from pymavlink import mavutil

# Sets up communication interface between the PixHawk and the Jetson
# Using UART with BAUD rate: 115200
connection = mavutil.mavlink_connection('/dev/ttyTHS1', 115200)
connection.wait_heartbeat()

# Send PWM command