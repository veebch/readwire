import subprocess
import os
import shutil


def find_kindle_mount_point():
    # Execute lsblk to list all block devices with their mount points
    result = subprocess.run(
        ["lsblk", "-J", "-o", "NAME,LABEL,MOUNTPOINT"], capture_output=True, text=True
    )
    if result.returncode == 0:
        devices = result.stdout
        try:
            # Parse the JSON output
            import json

            devices_json = json.loads(devices)
            # Look for a device labeled 'Kindle'
            for device in devices_json["blockdevices"]:
                if "children" in device:
                    for part in device["children"]:
                        if part["label"] == "Kindle" and part["mountpoint"]:
                            return part["mountpoint"]
        except json.JSONDecodeError:
            print("Error decoding JSON from lsblk output.")
    else:
        print("lsblk command failed.")
    return None


def copy_clippings_file(mount_point):
    clippings_path = os.path.join(mount_point, "documents", "My Clippings.txt")
    target_path = os.path.join(os.getenv("HOME"), "MyClippings.txt")
    print(f"Looking for Clippings at {clippings_path}")
    if os.path.exists(clippings_path):
        try:
            shutil.copy(clippings_path, target_path)
            print(f"Copied MyClippings.txt to {target_path}")
        except Exception as e:
            print(f"Failed to copy file: {e}")
    else:
        print("MyClippings.txt not found on the device.")


# Find Kindle mount point
kindle_mount = find_kindle_mount_point()
if kindle_mount:
    print(f"Kindle mounted at: {kindle_mount}")
    copy_clippings_file(kindle_mount)
else:
    print("Kindle not found or not mounted.")
