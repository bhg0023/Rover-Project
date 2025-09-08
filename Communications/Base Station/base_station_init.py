Base Station Main Init
Rover Challenge - Communications System
"""
 
import sys
import threading
import signal
from modules.radio import RadioHandler
from modules.joystick import JoystickHandler
from modules.gui import BaseStationGUI
from modules.telemetry import TelemetryHandler
from modules.video import VideoStreamHandler
 
# Global stop event
stop_event = threading.Event()
 
def signal_handler(sig, frame):
    print("\n[!] Shutting down Base Station...")
    stop_event.set()
    sys.exit(0)
 
def main():
    print("[Base Station] Initializing...")
 
    # Register Ctrl+C handler
    signal.signal(signal.SIGINT, signal_handler)
 
    #  Initialize Core Modules
    radio = RadioHandler(frequency=2.5e9, spi_bus=0, spi_ce=0)  # 2.5 GHz module
    joystick = JoystickHandler(device_id=0)
    telemetry = TelemetryHandler(radio)
    video = VideoStreamHandler()
 
    #  Start Threads
    radio_thread = threading.Thread(target=radio.listen_loop, args=(stop_event,))
    joystick_thread = threading.Thread(target=joystick.listen_loop, args=(stop_event,))
    telemetry_thread = threading.Thread(target=telemetry.update_loop, args=(stop_event,))
    video_thread = threading.Thread(target=video.stream_loop, args=(stop_event,))
 
    radio_thread.start()
    joystick_thread.start()
    telemetry_thread.start()
    video_thread.start()
 
    #  Launch GUI
    gui = BaseStationGUI(radio, joystick, telemetry, video)
    gui.run()  # Blocking call
 
    # Clean shutdown
    stop_event.set()
    radio_thread.join()
    joystick_thread.join()
    telemetry_thread.join()
    video_thread.join()
    print("[Base Station] Shutdown complete.")
 
if __name__ == "__main__":
    main()
