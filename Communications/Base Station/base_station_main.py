# Main code for Base Station Side

import joystick_encode
import radio_base_station
import time

log_file_path = 'radio_base_station_log.txt'
radio = radio_base_station.init()
joystick, axes, buttons = joystick_encode.init()
counter = 0

with open(log_file_path, 'a') as log_file:
    while True:
        try:
            
            joystick_packet = joystick_encode.encode(joystick, axes, buttons)
            counter += 1
            sent_time = time.time()
            message = f"{sent_time}|{counter}|{joystick_packet}"
            radio_base_station.send(radio, message.encode()) 
            """ log_file.write(f"[{sent_time}] Message sent: {message}\n")
            log_file.flush() """ 

           # radio_base_station.read(radio)
        except KeyboardInterrupt:
            break