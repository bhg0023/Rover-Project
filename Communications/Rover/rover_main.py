import hardware_encode
import radio_rover
import webcam
import threading
import os
import time

# fifo path is: '/tmp/video_stream.h264'
# must have something reading pipe for pipe to work!!

log_file_path = 'radio_rover_log.txt'
fifo_path = '/tmp/video_stream.h264'
fifo_chunk_size = 32 

# initilize functions
radio = radio_rover.init()
p = hardware_encode.init()

def send_to_radio(pkt, radio):
    try:
        radio_rover.send(radio, pkt)
    except Exception:
        pass

def packetizer(frame_bytes, seq_num=0):
    packets = []
    for i in range(0, len(frame_bytes), 28):
        header = seq_num.to_bytes(2, 'big') + (i//28).to_bytes(2, 'big')
        packets.append(header + frame_bytes[i:i+28])
    return packets

fifo_fd = os.open(fifo_path, os.O_RDONLY | os.O_NONBLOCK)
fifo = os.fdopen(fifo_fd, 'rb')

def fifo_reader():
    seq = 0
    while True:
        try:
            frame = fifo.read(4096)  # small chunk
        except BlockingIOError:
            frame = b''
        if not frame:
            time.sleep(0.001)
            continue
        packets = packetizer(frame, seq)
        for pkt in packets:
            send_to_radio(pkt, radio)
        seq += 1

# start the thread
fifo_read = threading.Thread(target=fifo_reader, daemon=True)
fifo_read.start()
video_encode = threading.Thread(target=hardware_encode.encode, args=(p,), daemon=True)
video_encode.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print('Exiting')
