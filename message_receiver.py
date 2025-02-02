import socket
import time
import threading


class ReceiveServer:
    def __init__(self, host_ip, host_port):
        self.host_ip = host_ip  # This is going to be the IP address of your machine
        self.host_port = int(host_port)  # This is the port you want to keep open for communication (20201 should do)

        self.server_thread = None

    def messageReceiver(self):
        # Sets socket options for IPv4 address type and TCP protocol
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # This binds the socket to your home machine
        server.bind((self.host_ip, self.host_port))
        
        # This basically starts the receiver server
        server.listen()

        
        while True:
            # This waits until a connection has been made to continue
            client_socket, client_address = server.accept()
            message = client_socket.recv(1024)

            # This decodes the data so it is printable
            message = message.decode('utf-8')

            # When a message is received, it will print to the terminal
            print(f"The message received is: {message}")


if __name__ == '__main__':
    # Replace these values with the ones you want to use
    host_ip = '127.0.0.1'
    host_port = 20201

    # This creates an instance of the "TransmitClient" class
    server = ReceiveServer(host_ip=host_ip, host_port=host_port)

    # Starts the server in a thread so you can do stuff in the while loop below if you want to.
    server.server_thread = threading.Thread(target=server.messageReceiver)
    server.server_thread.start()

    # Allow the program to run indefinitely so it doesn't close down immediately
    while True:
        pass
