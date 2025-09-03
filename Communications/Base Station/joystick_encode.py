# Written By: Benjamin Goldberg
#
#
# Read joystick values 


import pygame
import time


def init():
    pygame.init()
    pygame.joystick.init()

    joystick_count = pygame.joystick.get_count()

    if joystick_count == 0:
        exit()
    
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    name = joystick.get_name()
    print("Controller name: ", name)

    axes = min(joystick.get_numaxes(),4)
    #print("Number of Axes: ", axes)


    buttons = min(joystick.get_numbuttons(),12)
    #print("Number of Buttons: ", buttons)

    print("\nPress any button on your controller to start monitoring values...")

    waiting = True
    while waiting:
        # Process pygame events
        pygame.event.pump()
        
        # Check if any button is pressed
        for i in range(buttons):
            if joystick.get_button(i):
                print(f"\nButton {i} pressed! Starting monitoring...")
                waiting = False
                break
                
        # Short delay to prevent high CPU usage
        time.sleep(0.1)
    
    return joystick, axes, buttons

def encode(joystick, axes, buttons):


    '''
    Bit Layout (32-bit Packet):
    - 0-3: Axis 0 (Scaled 0-15)
    - 4-7: Axis 1 (Scaled 0-15)
    - 8-11: Axis 2 (Scaled 0-15)
    - 12-15: Axis 3 (Scaled 0-15)
    - 16-27: 12 Buttons
    - 28-32: unused 
    '''
    



    while True:
        packet = 0
        pygame.event.pump()

        for i in range(axes):
            axis = joystick.get_axis(i)
            scaled_axis_value = int((axis + 1.0) * 7.5) & 15
            packet |= (scaled_axis_value << (i * 4))

        for i in range(buttons):
            button = joystick.get_button(i)
            if button:
                packet |= (1<< (i + 16))
        
        return f"{packet:032b}"
        time.sleep(0.01)

