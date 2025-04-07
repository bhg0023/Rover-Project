# Written By: Benjamin Goldberg
#
# This code will encode live video into H.264 making use
# of the Pi's Hardware Encoder (h264_omx). 
# force all streams down to 5Mb/s
#
# 


import webcam
import subprocess

cv2_out = webcam.generate_frames()

if not cv2_out:
    raise ValueError("Error: Byte stream from webcam.generate_frames() is empty!")

print("Byte stream length:", len(cv2_out))  # Check the data lengths

command = ['ffmpeg',
            '-f',
            '-i', 'pipe:',
            '-f', 'mjpeg',
            '-c:v','mjpeg', 
            'out.jpg'
]

p = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

p.stdin.write(cv2_out)
p.stdin.close()



""" fourcc = cv2.VideoWriter_fourcc(*'H264')
out = cv2.VideoWriter('appsrc ! videoconvert ! x264enc tune=zerolatency noise-reduction=10000 bitrate=2048 speed-preset=superfast ! rtph264pay config-interval=1 pt=96 ! udpsink host=127.0.0.1 port=5000',fourcc,cv2.CAP_PROP_FPS, (800,600),True)

def send_stream():
    while webcam.cap.isOpened():
        frame = webcam.generate_frames()
        out.write(webcam.generate_frames()).tobytes()
        print(out)

 """