# Main code for Rover side

import hardware_encode
import os
import time
import radio_rover
import threading
import time
import subprocess
import matplotlib.pyplot as plt
import rover_display

# fifo path is: '/tmp/video_stream.h264'
# must have something reading pipe for pipe to work!!

log_file_path = 'radio_rover_log.txt'
fifo_path = '/tmp/video_stream.h264'
fifo_chunk_size = 32 

radio = radio_rover.init()
# p = hardware_encode.init()
oled = rover_display.init()

def sender_thread():
    print("Starting sender thread...")
    while not os.path.exists(fifo_path):
        print("Waiting for FIFO path to open....")
        time.sleep(0.5)


    """ try:
        initial_fd = os.open(fifo_path, os.O_RDONLY)
        with os.fdopen(initial_fd, 'rb') as initial_fifo:
            print("Opened FIFO in blocking mode first")
            initial_chunk = initial_fifo.read(fifo_chunk_size)
            if initial_chunk:
                print(f"Read initial {len(initial_chunk)} bytes")
                radio_rover.send(radio, initial_chunk)
    except Exception as e:
        print(f"Initial FIFO error: {e}") """


    fifo_fd = os.open(fifo_path, os.O_RDONLY)
    with os.fdopen(fifo_fd, 'rb') as fifo:

        while True:
            try:
                chunk = fifo.read(fifo_chunk_size)
                if chunk:
                    print(f"Read {len(chunk)} bytes from FIFO.")  # Debugging line
                    result = radio_rover.send(radio, chunk)
                    if not result: 
                        print("Transmission failed!")
                    else:
                        time.sleep(0.5)
                else:
                    print("FIFO empty waiting for data....")
                    time.sleep(0.1)
            except BlockingIOError:
                print("BlockingIOError")
                time.sleep(0.5)
            except Exception as e:
                print(f"Error in sender: {e}")
                time.sleep(0.5)

def encoder_thread():
    print("Starting encoder thread...")
    try:
        hardware_encode.encode(p)
    except Exception as e:
        print(f"Encoder error: {e}")


"""
encoder = threading.Thread(target=encoder_thread, daemon=True)
sender = threading.Thread(target=sender_thread, daemon=True)


sender.start()
time.sleep(5)
encoder.start()
time.sleep(5)
 """

latency_list = []
def log_latency():
    total_latency = 0.0
    message_count = 0
    last_log_time = 0
    with open(log_file_path, 'a') as log_file:
        while True:
            try:
                message = radio_rover.read(radio)
                recieved_time = time.time()
                
                if message: 
                    try: 
                        decoded = message.decode('utf-8')
                        parts = decoded.split('|', 2) # split into timestamp, counter, and payload
                        if len(parts) >= 3:
                            sent_time_str, counter, payload = parts
                            sent_time = float(sent_time_str)
                            
                            if recieved_time - last_log_time >= 0.1:
                                latency = (recieved_time - sent_time) * 1000 # get it in ms
                                latency_list.append(latency)
                                
                                
                                message_count += 1
                                total_latency += latency
                                avg_latency = total_latency / message_count
                                print(f"Received #{counter}, Latency: {latency:.2f} ms, Avg: {avg_latency:.2f} ms")

                                print(payload)
                                last_log_time = recieved_time

                                oled_latency = "Latency" + str(latency)
                                oled_payload = "Payload" + str(payload)
                                rover_display.display(oled, oled_latency, oled_payload)
                        else:
                            print(f"Malformed message: {decoded}")
                    except Exception as e:  
                        print(f"Decode/Parse Error: {e}")
            except KeyboardInterrupt:
                break

def plot_latency(latency_list):
    plt.figure(figsize=(10, 4))
    plt.plot(latency_list, marker='o', linestyle='-', color='blue')
    plt.title("Latency Over Time")
    plt.xlabel("Sample #")
    plt.ylabel("Latency (ms)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("latency_plot.png")  # Save instead of show
    print("Plot saved to latency_plot.png")

# Run the logging function for a certain period of time
print("Logging latencies...")
log_latency()  # Log latencies sequentially

# After logging, plot the collected latencies
print("Plotting latencies...")
plot_latency(latency_list)
 
