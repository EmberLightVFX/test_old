import math
import re
import sys
import json

DEBUG = False
# Read input from stdin (provided via shell script)
if DEBUG:
    from pprint import pprint

    BODY = """"""

else:
    BODY = sys.argv[1]


def cleanup_block(text: str) -> tuple[str, str | None]:
    lines = text.splitlines()
    category = str(lines[0].strip())
    data = None
    if str(lines[2].strip()) != "_No response_":
        data = "\n".join(lines[2:]).strip()
    return (category, data)


# Function to extract and convert the first number to a numeric type
def extract_single_number(text: str) -> float:
    number: list[str] = re.findall(r"\d*\.\d+|\d+", text.replace(",", "."))
    return float(number[0]) if "." in number else int(number[0])


def extract_dual_numbers(text: str) -> list[float]:
    numbers = re.findall(r"\d*\.\d+|\d+", text.replace(",", "."))
    if "." in numbers:
        return [float(num) for num in numbers[:2]]
    else:
        return [int(num) for num in numbers]


# Read existing sensors.json file if it exists
try:
    with open("sensors.json", "r") as f:
        sensors_data = json.load(f)
except FileNotFoundError:
    sensors_data = {}


vendor = None
camera = None

blocks = BODY.strip().split("### Name", 1)
## Camera info
camera_info = blocks[0].strip().split("### ")

# Vendor
category, data = cleanup_block(camera_info[2])
if data == "Other":
    category, data = cleanup_block(camera_info[3])
vendor = data
if vendor not in sensors_data:
    sensors_data[vendor] = {}

# Camera
category, data = cleanup_block(camera_info[4])
camera = data
if camera not in sensors_data[vendor]:
    sensors_data[vendor][camera] = {}

# Additional Information
category, data = cleanup_block(camera_info[5])
sensors_data[vendor][camera]["info"] = {}
if data:
    sensors_data[vendor][camera]["info"]["Other"] = data

# Sensor Dimensions
if "sensor dimensions" not in sensors_data[vendor][camera]:
    sensors_data[vendor][camera]["sensor dimensions"] = {}

## All resolution types
for block in blocks[1].split("### Name"):
    mm = None
    inches = None
    # Add back the name category that got removed from the split
    block = f"### Name{block}"

    dim_type = block.strip().split("### ")

    # Name
    category, data = cleanup_block(dim_type[1])
    if data is None:
        continue
    dim_name = data
    sensors_data[vendor][camera]["sensor dimensions"][dim_name] = {}

    # Focal Length
    category, data = cleanup_block(dim_type[2])
    if data:
        sensors_data[vendor][camera]["sensor dimensions"][dim_name]["focal_length"] = (
            extract_single_number(data)
        )
    else:
        sensors_data[vendor][camera]["sensor dimensions"][dim_name]["focal_length"] = ""

    # Resolution
    category, data = cleanup_block(dim_type[3])
    if data:
        res = extract_dual_numbers(data)
        sensors_data[vendor][camera]["sensor dimensions"][dim_name]["resolution"] = {
            "width": res[0],
            "height": res[1],
        }

    # Sensor Size (mm)
    category, data = cleanup_block(dim_type[4])
    if data:
        mm = extract_dual_numbers(data)

    # Sensor Size (inches)
    category, data = cleanup_block(dim_type[5])
    if data:
        inches = extract_dual_numbers(data)

    if not mm and not inches:
        raise AttributeError("You need at least one sensor size")
    elif mm and not inches:
        inches = [mm[0] / 25.4, mm[1] / 25.4]
    elif not mm:
        mm = [inches[0] * 25.4, inches[1] * 25.4]

    mm[0] = round(mm[0], 3)
    mm[1] = round(mm[1], 3)
    inches[0] = round(inches[0], 3)
    inches[1] = round(inches[1], 3)

    sensors_data[vendor][camera]["sensor dimensions"][dim_name]["mm"] = {
        "width": mm[0],
        "height": mm[1],
        "diagonal": round(math.sqrt(mm[0] ** 2 + mm[1] ** 2), 3),
    }
    sensors_data[vendor][camera]["sensor dimensions"][dim_name]["inches"] = {
        "width": inches[0],
        "height": inches[1],
        "diagonal": round(math.sqrt(inches[0] ** 2 + inches[1] ** 2), 3),
    }


# Write the updated dictionary back to sensors.json
if DEBUG:
    pprint(sensors_data)
else:
    with open("sensors.json", "w") as f:
        json.dump(sensors_data, f, indent=2)
