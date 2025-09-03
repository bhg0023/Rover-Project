import busio
import board
from adafruit_ssd1306 import SSD1306_I2C
import time

def init():
    i2c = busio.I2C(board.SCL, board.SDA)
    oled = SSD1306_I2C(128, 64, i2c)

    # clear display
    oled.fill(0)
    oled.text("OLED Ready", 0, 0, 1)
    oled.show()
    time.sleep(2)

    return oled


def display(oled, latency, joystick_packet):
    oled.fill(0)

    oled.text(latency, 0, 0, 1)
    oled.text(joystick_packet, 0, 20, 1)
    oled.show()
