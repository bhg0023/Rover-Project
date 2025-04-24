# Main code for Base Station Side

import joystick_encode

while True:
    try:
        joystick_encode.encode()

    except KeyboardInterrupt:
        break