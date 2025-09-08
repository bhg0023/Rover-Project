# rover_main.py
import time
import radio
from machine import Pin, PWM

# motor Setup
class Motor:
    def __init__(self, in1, in2, pwm_pin):
        self.in1 = Pin(in1, Pin.OUT)
        self.in2 = Pin(in2, Pin.OUT)
        self.pwm = PWM(Pin(pwm_pin), freq=1000)
        self.stop()

    def _scale_speed(self, speed):
        # Scale 0–255 (from base) → 0–1023 (ESP32 PWM duty) this is not smooth, we can make it smooth 
        return int((speed / 255) * 1023)

    def forward(self, speed):
        duty = self._scale_speed(speed)
        self.in1.value(1)
        self.in2.value(0)
        self.pwm.duty(duty)

    def reverse(self, speed):
        duty = self._scale_speed(speed)
        self.in1.value(0)
        self.in2.value(1)
        self.pwm.duty(duty)

    def stop(self):
        self.in1.value(0)
        self.in2.value(0)
        self.pwm.duty(0)

# adjust the pins acording to wiring!)
left_motor = Motor(in1=18, in2=19, pwm_pin=21)
right_motor = Motor(in1=22, in2=23, pwm_pin=25)

# Rover Main 
def main():
    print("=== Rover Main Init ===")

    if not radio.initialize_controller():
        print("[ROVER] Failed to initialize radio.")
        return
    radio.set_frequency(433920000)
    print("[ROVER] Radio ready.")

    while True:
        data = radio.receive_data()
        if data:
            print(f"[ROVER] Command received: {data}")
            try:
                action, speed = data.split(":")
                speed = int(speed)

                if action == "F":
                    left_motor.forward(speed)
                    right_motor.forward(speed)
                elif action == "R":
                    left_motor.reverse(speed)
                    right_motor.reverse(speed)
                elif action == "L":
                    left_motor.reverse(speed)
                    right_motor.forward(speed)
                elif action == "R":
                    left_motor.forward(speed)
                    right_motor.reverse(speed)
                elif action == "S":
                    left_motor.stop()
                    right_motor.stop()
                else:
                    print(f"[ROVER] Unknown action: {action}")

            except ValueError:
                print(f"[ROVER] Malformed command: {data}")

        time.sleep(0.05)

if __name__ == "__main__":
    main()
