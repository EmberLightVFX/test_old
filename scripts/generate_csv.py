import json
import os
import csv
from typing import Any

data_folder = os.path.join(".", "data")
json_file_path = os.path.join(data_folder, "sensors.json")
csv_file_path = os.path.join(data_folder, "sensors.csv")

with open(json_file_path, "r") as file:
    sensors: dict[str, dict[str, dict[str, Any]]] = json.load(file)

with open(
    csv_file_path,
    "w",
    newline="",
) as csv_file:
    csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_MINIMAL)

    # Base Header
    csv_writer.writerow(
        [
            "Vendor",
            "Camera",
            "Sensor Dimensions Name",
            "Focal Length",
            "Resolution Width",
            "Resolution Height",
            "Sensor mm Width",
            "Sensor mm Height",
            "Sensor mm Diagonal",
            "Sensor Inches Width",
            "Sensor Inches Height",
            "Sensor Inches Diagonal",
            "Info",
        ]
    )

    # Iterate through the JSON data to generate csv info
    for vendor, cameras in sensors.items():
        for camera, data in cameras.items():
            for res_type, res_data in data["sensor dimensions"].items():
                csv_writer.writerow(
                    [
                        vendor,
                        camera,
                        res_type,
                        res_data["focal length"],
                        res_data["resolution"]["width"],
                        res_data["resolution"]["height"],
                        res_data["mm"]["width"],
                        res_data["mm"]["height"],
                        res_data["mm"]["diagonal"],
                        res_data["inches"]["width"],
                        res_data["inches"]["height"],
                        res_data["inches"]["diagonal"],
                        data["info"].get("Other", ""),
                    ]
                )
