# Written By: Benjamin Goldberg
#
# This code will encode live video into H.264 making use
# of the Pi's Hardware Encoder (h264_omx). 
# force all streams down to 5Mb/s

import webcam
import cv2

fourcc = cv2.VideoWriter_fourcc(*'H264')
out = cv2.VideoWriter('appsrc ! videoconvert ! x264enc tune=zerolatency noise-reduction=10000 bitrate=2048 speed-preset=superfast ! rtph264pay config-interval=1 pt=96 ! udpsink host=127.0.0.1 port=5000',fourcc,cv2.CAP_PROP_FPS, (800,600),True)

def send_stream():
    while webcam.cap.isOpened():
        webcam.generate_frames()
        out.write(webcam.generate_frames.image).tobytes()
        print(out)

