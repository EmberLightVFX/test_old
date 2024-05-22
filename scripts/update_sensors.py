import math
import re
import sys
import json

# Read input from stdin (provided via shell script)
BODY = sys.argv[1]


def cleanup_block(text: str) -> tuple[str, str | None]:
    print("cleanup_block Text:", text)
    lines = text.splitlines()
    print("cleanup_block lines:", lines)
    category = str(lines[0])
    body = None
    if str(lines[2]) != "_No response_":
        body = "\n".join(lines[2:]).strip()
    return (category, body)


# Function to extract and convert the first number to a numeric type
def extract_single_number(text: str) -> float:
    number: list[str] = re.findall(r"\d*\.\d+|\d+", text.replace(",", "."))
    return float(number[0])


def extract_dual_numbers(text: str) -> list[float]:
    numbers = re.findall(r"\d*\.\d+|\d+", text.replace(",", "."))
    return [float(num) for num in numbers[:2]]


# Read existing sensors.json file if it exists
try:
    with open("sensors.json", "r") as f:
        sensors_data = json.load(f)
except FileNotFoundError:
    sensors_data = {}


resolutions = []
vendor = None
camera = None

blocks = BODY.strip().split("### Name", 1)

# Camera info
for block in blocks[0].strip().split("### "):
    category, body = cleanup_block(block)
    if category == "Vendor":
        vendor = body
        if vendor not in sensors_data:
            sensors_data[vendor] = {}

    elif category == "Camera":
        camera = body
        if camera not in sensors_data[vendor]:
            sensors_data[vendor][camera] = {}

    elif category == "Additional Information" and body:
        sensors_data[vendor][camera]["info"] = body

# All resolution types
for block in blocks[1:]:
    mm = None
    inches = None

    # Add back the name category that got removed from the first split
    block = f"### Name{block}"
    res_type = block.strip().split("### ")

    # Name
    category, body = cleanup_block(res_type[0])
    if body is None:
        continue
    res_name = body
    sensors_data[vendor][camera][res_name] = {}

    # Focal Length
    category, body = cleanup_block(res_type[1])
    if body:
        sensors_data[vendor][camera][res_name]["focal_length"] = extract_single_number(
            body
        )

    # Resolution
    category, body = cleanup_block(res_type[2])
    if body:
        res = extract_dual_numbers(body)
        sensors_data[vendor][camera][res_name]["resolution"] = {
            "width": res[0],
            "height": res[1],
        }

    # Sensor Size (mm)
    category, body = cleanup_block(res_type[3])
    if body:
        mm = extract_dual_numbers(body)

    # Sensor Size (inches)
    category, body = cleanup_block(res_type[4])
    if body:
        inches = extract_dual_numbers(body)

    if not mm and not inches:
        raise AttributeError("You need at least one sensor size")
    elif mm and not inches:
        inches = [mm[0] / 25.4, mm[1] / 25.4]
    elif not mm:
        mm = [inches[0] * 25.4, inches[1] * 25.4]

    sensors_data[vendor][camera][res_name]["mm"] = {
        "width": mm[0],
        "height": mm[1],
        "diagonal": math.sqrt(mm[0] ** 2 + mm[1] ** 2),
    }
    sensors_data[vendor][camera][res_name]["inches"] = {
        "width": inches[0],
        "height": inches[1],
        "diagonal": math.sqrt(inches[0] ** 2 + inches[1] ** 2),
    }


# Write the updated dictionary back to sensors.json
with open("sensors.json", "w") as f:
    json.dump(sensors_data, f, indent=2)
