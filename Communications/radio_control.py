

import serial
import time

# Configuration
SERIAL_PORT = "/dev/ttyS0"  # Replace with your serial port
BAUD_RATE = 9600  # Adjust if we need
CONTROLLER_ADDRESS = 0x01  # Replace with your controller's address

# Initialize the serial communication
try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    print(f"Serial port {SERIAL_PORT} initialized successfully.")
except serial.SerialException as e:
    print(f"Error initializing serial port: {e}")
    exit()


def send_at_command(command):
  """Sends an AT command and returns the response."""
  ser.write((command + "\r\n").encode())
  time.sleep(0.1)  # Allow time for the module to process
  response = ""
  while ser.in_waiting > 0:
    response += ser.readline().decode().strip()
  return response


def initialize_controller():
    """Initializes the ATREB215 module and the remote controller."""
    print("Initializing controller...")

    # Example AT commands (replace with actual commands for your module)
    response = send_at_command("AT")
    print(f"AT: {response}")  # Check for basic communication

    response = send_at_command("AT+ADDR=" + str(CONTROLLER_ADDRESS))
    print(f"AT+ADDR: {response}")  # Set the controller address

    # Add more initialization commands as needed (frequency, power, etc.)
    # ...

    if "OK" in response:
      print("Controller initialized successfully.")
      return True
    else:
      print("Controller initialization failed.")
      return False



def set_frequency(frequency_hz):
    """Sets the operating frequency."""
    # Replace with the correct AT command to set the frequency
    command = f"AT+FREQ={frequency_hz}" # Example
    response = send_at_command(command)
    print(f"Set frequency to {frequency_hz}Hz: {response}")


def send_data(data):
    """Sends data to the controller."""
    # Implement data sending logic based on the module's specifications.
    print(f"Sending data: {data}")
    # ... (Example)
    # ser.write(data.encode())

def receive_data():
    """Receives data from the controller."""
    # Implement data receiving logic.
    # ... (Example)
    if ser.in_waiting > 0:
        data = ser.readline().decode().strip()
        print(f"Received data: {data}")
    else:
        print("No data received")
        return None
    return data



if __name__ == "__main__":
    if initialize_controller():
        set_frequency(433920000)  # Set example frequency (adjust as needed)


        while True:
          #Example interaction loop
          send_data("command1")  # Example: Send a command
          received_data = receive_data()

          time.sleep(1) # adjust as needed

    else:
        print("Exiting due to initialization error")


    ser.close()