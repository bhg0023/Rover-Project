import pyrf24
import time

CE_PIN = 18
CSN_PIN = 0

def init():
    radio = pyrf24.RF24(CE_PIN, CSN_PIN)

    address = b"00000"
    result = radio.begin()
    radio.powerUp()
    if not result:
        print("Radio not initilized at all!")
    radio.setPALevel(1)
    radio.setChannel(76)
    radio.setAutoAck(True)
    radio.setPayloadSize(32)
    radio.openWritingPipe(address)
    radio.openReadingPipe(0, address)
    radio.startListening()
    radio.print_details()

    return radio

def send(radio, message):
    # radio.stopListening()           
    result = radio.write(message) #Transmit over TX and store result
    # If result == 1, the message was transmited. 
    if not result:
        print("Transmission Failed!")
    else:
        print("Transmission Sucess!")


def read(radio):
    radio.startListening()
    if radio.available():
        payload = radio.read(128)
        return payload
