import subprocess
import os
import shutil
import re


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
    target_path = os.path.join(
        os.getcwd(), "My_Clippings.txt"
    )  # Save to the current working directory
    print(f"Looking for Clippings at {clippings_path}")
    if os.path.exists(clippings_path):
        try:
            shutil.copy(clippings_path, target_path)
            print(f"Copied My Clippings.txt to {target_path}")
        except Exception as e:
            print(f"Failed to copy file: {e}")
    else:
        print("My Clippings.txt not found on the device.")


def parse_clippings_from_file(file_path):
    # Open and read the contents of the clippings file using 'utf-8-sig' to handle BOM if present
    with open(file_path, "r", encoding="utf-8-sig") as file:
        clippings = file.read()

    # Manually remove any stray BOM characters throughout the file
    clippings = clippings.replace("\ufeff", "")

    # Regex to split the entries and remove unnecessary lines and trim spaces
    entries = re.split(r"={10,}", clippings)
    parsed_entries = []
    unique_entries = set()
    for entry in entries:
        entry = re.sub(
            r"^-.*$", "", entry, flags=re.MULTILINE
        ).strip()  # Remove highlight details
        if entry:
            # Extract the book title and the highlight text
            title_match = re.search(r"^(.*?)\n", entry, re.MULTILINE | re.DOTALL)
            highlight_match = re.search(r"\n(.+)", entry, re.MULTILINE | re.DOTALL)
            if title_match and highlight_match:
                title = title_match.group(1).strip()
                title = re.sub(
                    r"\(.*?\)$", "", title
                ).strip()  # Remove author name in parentheses
                highlight = highlight_match.group(1).strip()
                # Combine title and highlight to ensure uniqueness
                combined = f"{title}\t{highlight}"
                if combined not in unique_entries:
                    unique_entries.add(combined)
                    parsed_entries.append((highlight, title))
    return parsed_entries


def save_parsed_clippings_to_tsv(parsed_entries, output_file_path):
    # Save the parsed clippings into a TSV file format
    with open(output_file_path, "w", encoding="utf-8") as file:
        file.write("Highlight\tBook Title\n")
        for highlight, title in parsed_entries:
            file.write(f"{highlight}\t{title}\n")


# Path to the clippings file and the output file
clippings_file_path = "My_Clippings.txt"
output_tsv_path = "clippings_parsed.tsv"

# Find Kindle mount point
kindle_mount = find_kindle_mount_point()
if kindle_mount:
    print(f"Kindle mounted at: {kindle_mount}")
    copy_clippings_file(kindle_mount)
else:
    print("Kindle not found or not mounted.")

# Parse clippings from file and save to a new TSV file
parsed_clippings = parse_clippings_from_file(clippings_file_path)
save_parsed_clippings_to_tsv(parsed_clippings, output_tsv_path)

print(f"Clippings parsed and saved to {output_tsv_path}")
