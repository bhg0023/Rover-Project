# Written By: Benjamin Goldberg
#
# This code will frame the h.264 data stream from "hardware_encode.py"
# packaged into SPI

import spidev
import hardware_encode

spi = spi.SpiDev()
spi.open(bus, device)

# SPI settings
