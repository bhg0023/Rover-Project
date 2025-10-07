## Installing MAVProxy
I used this [video](https://youtu.be/nIuoCYauW3s?si=B8UhA8yvrDOfCrkB) to get started with the connection between Jetson and Pixhawk. I extracted the code from the video and placed it here for convenience.
```
sudo apt-get install python-pip python3-pip
sudo apt-get install python3-dev python3-opencv python3-wxgtk4.0 python3-matplotlib python3-lxml libxml2-dev libxslt-dev
sudo pip install PyYAML mavproxy
```
## Testing Pixhawk Connection Using MAVProxy
On the Jetson command line interface enter the following command  
```
sudo mavproxy.py --master=/dev/ttyTHS0
```
This should open mavproxy and establish a connection to the Pixhawk. You should see commands being sent to the Jetson on the command line interface.
