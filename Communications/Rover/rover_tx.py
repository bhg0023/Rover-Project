import pyrf24

CE_PIN = 18
CSN_PIN = 0

def init():
    radio = pyrf24.RF24.begin(CE_PIN, CSN_PIN)
    address = b"00000"
    result = radio.begin()
    radio.powerUp()
    if not result:
        print("Radio not initilized at all!")
    radio.openWritingPipe(address)
    radio.stop_listening()
    return radio

def send(radio, message):
    result = radio.write(message)
    if not result:
        print("Transmission Failed!")
    else:
        print("Transmission Success!")
    