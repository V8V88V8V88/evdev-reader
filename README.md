# evdev-reader

Reads key press events from a Linux input device (`/dev/input/event*`) and writes the key names to `events.log`. There is a Python version using `python-evdev` and a C++ version using `libevdev`.

I wrote it to see how input events travel from the kernel to userspace.

## Python

```bash
pip install -r requirements.txt
sudo python3 src/evdev_reader.py /dev/input/event2
```

## C++

```bash
sudo dnf install libevdev-devel
g++ cpp/evdev_reader.cpp -o evdev_reader -I/usr/include/libevdev-1.0 -levdev
sudo ./evdev_reader /dev/input/event2
```

Both need root to open the device. `cat /proc/bus/input/devices` shows which `eventN` is your keyboard.
