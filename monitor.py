import os
import shutil
from pyudev import Context, Monitor, MonitorObserver


def device_event(action, device):
    if action == "add":
        # Check if the connected device is a Kindle
        if device.get("ID_FS_TYPE") == "vfat" and "Kindle" in device.get(
            "ID_FS_LABEL", ""
        ):
            print(f"Kindle detected: {device.device_node}")
            kindle_path = device.get("DEVNAME")
            clippings_path = os.path.join(kindle_path, "documents", "MyClippings.txt")
            target_path = (
                "/path/to/destination/MyClippings.txt"  # Change to your desired path
            )

            # Copy MyClippings.txt to the target path
            if os.path.exists(clippings_path):
                shutil.copy(clippings_path, target_path)
                print(f"Copied MyClippings.txt to {target_path}")
            else:
                print("MyClippings.txt not found on the device.")


context = Context()
monitor = Monitor.from_netlink(context)
monitor.filter_by(subsystem="block")

observer = MonitorObserver(monitor, callback=device_event, name="monitor-observer")
observer.start()

try:
    while True:
        pass
except KeyboardInterrupt:
    observer.send_stop()
