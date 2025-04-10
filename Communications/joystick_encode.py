# Written By: Benjamin Goldberg
#
#
# Read joystick values 


import pygame
import time


def start_up():
    pygame.init()
    pygame.joystick.init()

    joystick_count = pygame.joystick.get_count()
    return joystick_count


def encode():
    if start_up == 0:
        print("No Joysticks Detected!")
        exit()
    
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    name = joystick.get_name()
    print("Controller name: ", name)

    buttons = joystick.get_numbuttons()


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


    axes = joystick.get_numaxes()
    print("Number of Axes: ", axes)


    buttons = joystick.get_numbuttons()
    print("Number of Buttons: ", buttons)


    while True:
        for i in range(axes):
            axis = joystick.get_axis(i)
            print("Axis ", i, ": ", axis)


        """ for i in range(buttons):
            button = joystick.get_button(i)
            print("Button ", i, ": ", button ) """ 
        
        time.sleep(0.5)
start_up()
encode()