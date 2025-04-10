# Written By: Benjamin Goldberg
#
# This code will encode live video into H.264 making use
# of the Pi's Hardware Encoder (h264_v4l2m2m). 
# 
#
# 


import webcam
import subprocess

cv2_out = webcam.generate_frames()

if not cv2_out:
    raise ValueError("Error: Byte stream from webcam.generate_frames() is empty!")

# print("Byte stream length:", len(cv2_out))  # Check the data lengths

command = ['ffmpeg',
           '-an',
           '-framerate', '24',
            '-f', 'mjpeg',
            '-i', 'pipe:0',
            '-vf', 'format=yuv420p',
            '-c:v','h264_v4l2m2m', 
            '-max_muxing_queue_size', '1024',
            '-f', 'h264',
            'pipe:1'
]

p = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

try:
    # Process each frame and send it to FFmpeg
    for cv2_out in webcam.generate_frames():
        try:
            p.stdin.write(cv2_out)  # Write each frame's byte data to ffmpeg's stdin
            print("Sent a frame!")
        except BrokenPipeError:
            print("BrokenPipeError: FFmpeg process may have terminated early.")
            break  # Exit the loop if ffmpeg terminates unexpectedly
except:
    print("other error")
    p.stdin.close()

out, err = p.communicate()
print("Error:", err)

print("Output: ", out.decode())

if p.returncode == 0:
    print("ffmpeg err: ", err.decode())

