## Testing Pixhawk Connection Using MAVProxy
On the Jetson command line interface enter the following command  
```
sudo mavproxy.py --master=/dev/ttyTHS0
```
This should open mavproxy and establish a connection to the Pixhawk. You should see commands being sent to the Jetson on the command line interface.
