# Connection Testing
## Installing MAVProxy
I used this [video](https://youtu.be/nIuoCYauW3s?si=B8UhA8yvrDOfCrkB) to get started with the connection between Jetson and Pixhawk. I extracted the code from the video and placed it here for convenience.
Type the following commands on the Jetson command line interface.
```
sudo apt-get install python-pip python3-pip
sudo apt-get install python3-dev python3-opencv python3-wxgtk4.0 python3-matplotlib python3-lxml libxml2-dev libxslt-dev
sudo pip install PyYAML mavproxy
```
## Testing Pixhawk Connection Using MAVProxy
On the Jetson command line interface enter the following command  
```
sudo mavproxy.py --master=/dev/ttyTHS1
```
This should open mavproxy and establish a connection to the Pixhawk. You should see commands being sent to the Jetson on the command line interface.
# MAVLink - Sending PWM commands
- [Setting up pymavlink](https://pypi.org/project/pymavlink/)

To send a command, we will be using the [command protocol](https://mavlink.io/en/services/command.html). Since we are not sending positional data, it is best to use COMMAND_LONG to send PWM values. 

Setting up the command message using COMMAND_LONG is shown below.
```Python
connection.mav.command_long_encode(
        connection.target_system,     # Target system ID
        connection.target_component,  # Target component ID
        mavutil.mavlink.MAV_CMD,      # ID of command to send
        confirmation, # 0: First transmission of this command. 1-255: Confirmation transmissions (e.g. for kill command)
        param1,       # Parameter 1 (for the specific command)
        param2,       # Parameter 2 (for the specific command)
        param3,       # Parameter 3 (for the specific command)
        param4,       # Parameter 4 (for the specific command)
        param5,       # Parameter 5 (for the specific command)
        param6,       # Parameter 6 (for the specific command))
        param7        # Parameter 7 (for the specific command)
        )
```
Commands to set servo pwm value
1. [MAV_CMD_DO_SET_SERVO](https://mavlink.io/en/messages/common.html#MAV_CMD_DO_SET_SERVO)
2. [MAV_CMD_DO_SET_ACTUATOR](https://mavlink.io/en/messages/common.html#MAV_CMD_DO_SET_ACTUATOR)

!!!! DO: Test both commands to see which one best fits our needs.
Testing the command number 2 will have the following set up.
```
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
```
