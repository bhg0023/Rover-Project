# Written By: Benjamin Goldberg
#
# This code will frame the h.264 data stream from "hardware_encode.py"
# packaged into SPI
import spidev


with open('/tmp/video_stream.h264', 'rb') as fifo:
    while True:
        chunk = fifo.read(1024)
        if not chunk:
            break
        spi.write(chunk)