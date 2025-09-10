import threading
import time

from radio_rover import RadioRover
from video_rover import VideoRover


def radio_listener(radio):
    """ Continuously listen for commands from base station. """
    while True:
        cmd = radio.receive()
        if cmd:
            print(f"[ROVER] Received command: {cmd}")
            # TODO: forward to controls module later
        time.sleep(0.01)  # prevent CPU hogging


def video_streamer(video):
    """ Continuously run video handling (capture/stream). """
    while True:
        video.update()
        time.sleep(0.05)


def main():
    print("[ROVER] Initializing subsystems...")

    # Init Modules 
    radio = RadioRover()
    video = VideoRover()

    # Start Threads
    radio_thread = threading.Thread(target=radio_listener, args=(radio,), daemon=True)
    video_thread = threading.Thread(target=video_streamer, args=(video,), daemon=True)

    radio_thread.start()
    video_thread.start()

    print("[ROVER] Rover subsystems running (radio + video).")

    # Main Loop 
    try:
        while True:
            # Could add rover status updates here
            time.sleep(1)
    except KeyboardInterrupt:
        print("[ROVER] Shutdown requested.")


if __name__ == "__main__":
    main()

