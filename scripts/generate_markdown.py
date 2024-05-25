import json
import os
import re
from typing import Any
from tabulate import tabulate

data_folder = os.path.join(".", "data")
json_file_path = os.path.join(data_folder, "sensors.json")
docs_folder = os.path.join(data_folder, "markdown")
sidebar_file_path = os.path.join(docs_folder, "_sidebar.md")

with open(json_file_path, "r") as file:
    sensors: dict[str, dict[str, dict[str, Any]]] = json.load(file)

# Create docs directory if it doesn't exist
os.makedirs(docs_folder, exist_ok=True)

def create_filename(name: str) -> str:
    return re.sub(r'[^a-zA-Z0-9]', '', name.lower().replace(" ", "_"))

def create_markdown_table(res: list[list[str]]) -> str:
    return tabulate(tabular_data=res[1:], headers=res[0], tablefmt='github')


def generate_markdown(vendor: str, camera: str, info: dict[str, str] | None , res: list[list[str]]):
    content = f"# {vendor} - {camera}\n\n"

    has_info = False
    if info:
        for key, val in info.items():
            if val:
                if not has_info:
                    has_info = True
                    content = content + "## Info\n\n"
                # Code for future info keys
                # content = f"{content}### {key}\n\n{val}\n\n"
                content = f"{content}{val}\n\n"
    content = f"{content}## Resolution Dimensions\n\n"
    return content + create_markdown_table(res)


nav_entries = []

# Iterate through the JSON data to generate markdown files
for vendor, cameras in sensors.items():
    vendor_dir = os.path.join(docs_folder, create_filename(vendor))
    os.makedirs(vendor_dir, exist_ok=True)
    nav_cam:list[dict[str, str]] = []
    for camera, data in cameras.items():
        filename = f"{create_filename(camera)}.md"
        filepath = os.path.join(vendor_dir, filename)
        nav_cam.append({"name": camera, "filepath": filepath.replace("\\", "/")})

        entries: list[list[str]] = [
            ["Name", "Focal Length", "Resolution", "Sensor mm", "Sensor inches"],
        ]

        for res_type, res_data in data["sensor dimensions"].items():
            entries.append([])
            i = len(entries) - 1
            entries[i].append(res_type)
            entries[i].append(res_data.get("focal length"))
            entries[i].append(f"{res_data["resolution"]["width"]} x {res_data["resolution"]["height"]}")
            entries[i].append(f"{res_data["mm"]["width"]} x {res_data["mm"]["height"]} ({res_data["mm"]["diagonal"]} diagonal)")
            entries[i].append(f"{res_data["inches"]["width"]} x {res_data["inches"]["height"]} ({res_data["inches"]["diagonal"]} diagonal)")

        # Check if there are any focal length in the entry
        found_fl = any(entry[1] for entry in entries[1:])
        if not found_fl:
            for entry in entries:
                entry.pop(1)
            
            
        markdown_content = generate_markdown(vendor, camera, data.get("info", None), entries)

        with open(filepath, "w") as md_file:
            md_file.write(markdown_content)

    nav_entries.append({"vendor": vendor, "nav_cam": nav_cam})

# Write sidebar file
with open(sidebar_file_path, "w") as file:
    for entry in nav_entries:
        file.write(f'- [{entry["vendor"]}](//)\n')
        for camera in entry["nav_cam"]:
            file.write(f'  - [{camera["name"]}]({camera["filepath"]})\n')
        file.write("\n")
