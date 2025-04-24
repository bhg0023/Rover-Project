# Written By: Benjamin Goldberg
#
# This code will encode live video into H.264 making use
# of the Pi's Hardware Encoder (h264_v4l2m2m). 
# 
#
# Sends H264 data to named pipe (FIFO) in directory /tmp/video_stream.h264



import webcam
import subprocess
import time

fifo_path = '/tmp/video_stream.h264'

""" if not os.path.exists(fifo_path):
    os.mkfifo(fifo_path) """



def encode():
    command = ['ffmpeg',
            '-y',
            '-an',
            '-framerate', '24',
                '-f', 'image2pipe',
                '-i', 'pipe:0',
                '-vf', 'format=yuv420p',
                '-c:v','h264_v4l2m2m', 
                '-max_muxing_queue_size', '1024',
                '-f', 'h264',
                fifo_path
    ]

    p = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    try:
        # Process each frame and send it to FFmpeg
        count = 0
        for frame in webcam.generate_frames():
            print("Frame read!")
            try:
                p.stdin.write(frame)  # Write each frame's byte data to ffmpeg's stdin
                print("Sent a frame!")
                count += 1
                time.sleep(1/24)
            except BrokenPipeError:
                print("BrokenPipeError: FFmpeg process may have terminated early.")
                break  # Exit the loop if ffmpeg terminates unexpectedly
    except KeyboardInterrupt:
        print("User ended")
        p.stdin.close()
        p.wait()
        err = p.stderr.read()
        print(f"Error: {err}")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        p.stdin.close()
        p.wait()
        err = p.stderr.read()
        if err:
            print(f"FFmpeg stderr:\n{err.decode()}")


        print("Process completed")




