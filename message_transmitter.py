import socket
import time
import threading

'''
This code has nothing to do with protobufs, all that stuff was taken out. This
code is simply used to transmit a string of text from one RPi to another.
'''

class TransmitClient:
    def __init__(self, receiver_ip, receiver_port, transmit_hz):
        self.receiver_ip = receiver_ip  # This is going to be the IP address of the other machine
        self.receiver_port = int(receiver_port)  # This is the port you want to keep open for communication (20201 should do)
        self.transmit_hz = transmit_hz  # This is how often a message is sent

        self.client_thread = None

    # This is the function you will start in a thread
    def messageTransmitter(self):
        # Run code in while loop so it transmits indefinitely until we cancel it
        while True:
            
            # This is the string of text that will be sent
            message = "enter your data here"

            # Uses "try-except" block to handle any errors if they occur
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect((self.receiver_ip, self.receiver_port))

                    # Before sending the data we must encode it
                    s.sendall(message.encode('utf-8'))
                    print(f"The message being sent is: {message}")
      

            # Code executes if there is an error:
            except socket.error as e:
                    print(f"Socket error: {e}")
            except Exception as e:
                print(f"Unexpected error: {e}")
            
            # Delay the next iteration of the loop
            time.sleep(1/transmit_hz)

if __name__ == '__main__':
    # Replace these values with the ones you want to use
    receiver_ip = '127.0.0.1'
    receiver_port = 20201
    transmit_hz = 1

    # This creates an instance of the "TransmitClient" class
    client = TransmitClient(receiver_ip=receiver_ip, receiver_port=receiver_port, transmit_hz=transmit_hz)

    # Starts the server in a thread so you can do stuff in the while loop below if you want to.
    client.client_thread = threading.Thread(target=client.messageTransmitter)
    client.client_thread.start()

    # Allow the program to run indefinitely so it doesn't close down immediately
    while True:
        pass