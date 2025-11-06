from pymavlink import mavutil

# Sets up communication interface between the PixHawk and the Jetson
# Using UART with BAUD rate: 57600
connection = mavutil.mavlink_connection('/dev/ttyTHS1', 57600)
connection.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" % (connection.target_system, connection.target_component))

# Reading LiPo battery voltage
msg = connection.recv_match(type='SYS_STATUS', blocking=True)
print("Battery Voltage: " + str(msg.voltage_battery) +  ", " + "Battery Remaining: " + str(msg.battery_remaining) + "%")
