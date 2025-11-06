from pymavlink import mavutil

# Sets up communication interface between the PixHawk and the Jetson
# Using UART with BAUD rate: 115200
connection = mavutil.mavlink_connection('/dev/ttyTHS1', 115200)
connection.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" % (connection.target_system, connection.target_component))


message = connection.mav.command_long_encode(
        connection.target_system,  # Target system ID
        connection.target_component,  # Target component ID
        mavutil.mavlink.MAV_CMD_SET_MESSAGE_INTERVAL,  # ID of command to send
        0,  # Confirmation
        mavutil.mavlink.MAVLINK_MSG_ID_BATTERY_STATUS,  # param1: Message ID to be streamed
        1000000, # param2: Interval in microseconds
        0,       # param3 (unused)
        0,       # param4 (unused)
        0,       # param5 (unused)
        0,       # param5 (unused)
        0        # param6 (unused)
        )

connection.mav.send(message)

response = connection.recv_match(type='COMMAND_ACK', blocking=True)
if response and response.command == mavutil.mavlink.MAV_CMD_SET_MESSAGE_INTERVAL and response.result == mavutil.mavlink.MAV_RESULT_ACCEPTED:
    print("Command accepted")
else:
    print("Command failed")
