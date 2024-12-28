import sys

from evdev import InputDevice, categorize, ecodes

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <input_device>", file=sys.stderr)
    sys.exit(1)

device = InputDevice(sys.argv[1])

with open("events.log", "a") as log_file:
    for event in device.read_loop():
        if event.type == ecodes.EV_KEY:
            key_event = categorize(event)
            if event.value == 1:  # Key press event
                log_file.write(key_event.keycode + '\n')
                log_file.flush()
