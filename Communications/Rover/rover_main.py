# Main code for Rover side

import hardware_encode
import spi_frame

# hardware encoding of video
# fifo path is: '/tmp/video_stream.h264'
# must have something reading pipe for pipe to work!!

while True:
    try:
        hardware_encode.encode()

    except KeyboardInterrupt:
        break



# frame in SPI here!

# send radio signal here