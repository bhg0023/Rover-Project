import pyrf24
import time

# pyrf24.RF24_DRIVER = "SPIDEV"

CE_PIN = 18
CSN_PIN = 0
address = b"00000"

def init():
    radio = pyrf24.RF24(CE_PIN, CSN_PIN)
    result = radio.begin()
    radio.powerUp()


    if not result:
        print("Radio not initilized at all!")


    radio.setPALevel(1)
    radio.setChannel(76)
    radio.setAutoAck(True)
    radio.setRetries(5, 15)  # 5 retries, 500us delay × 15 = 7.5ms retry delay
    radio.setPayloadSize(128)
    radio.openWritingPipe(address)
    radio.openReadingPipe(0, address)
    

    time.sleep(0.1)
    radio.print_details()

    return radio

def send(radio, message):
    radio.stopListening()
    result = radio.write(message)

    if not result:
        print("Transmission Failed!")
    else:
        print("Transmission Sucess!")


def read(radio):
    radio.startListening()
    if radio.available():
        payload = radio.read(32)
        print("Recieved: ", payload)

    time.sleep(0.1)
    