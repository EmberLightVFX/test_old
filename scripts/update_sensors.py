import sys
import json

# Read input from stdin (provided via shell script)
print("-------------------")
print(sys.argv[1])
print("------------------")
exit(1)
#VENDOR = sys.argv[1]
#CAMERA = sys.argv[2]
#TYPE = sys.argv[3]

VENDOR = "Canon"
CAMERA = "C300 Mark II"
TYPE = """- Type: All
  Focal Length (optional): 
  Resolution: 4096 x 2160
  mm: 24.6 x 13.8
  inch: 0.968 x 0.543
- Type: All2
  Focal Length (optional): 
  Resolution: 4096 x 2160
  mm: 24.6 x 13.8
  inch: 0.968 x 0.543"""

# Read existing sensors.json file if it exists
try:
    with open('sensors.json', 'r') as f:
        sensors_data = json.load(f)
except FileNotFoundError:
    sensors_data = {}

# Ensure the necessary keys exist in the dictionary
if VENDOR not in sensors_data:
    sensors_data[VENDOR] = {}
if CAMERA not in sensors_data[VENDOR]:
    sensors_data[VENDOR][CAMERA] = {}

resolutions = []
for block in TYPE.strip().split('\n-'):
    print("Block:", block)
    resolution = {}
    for line in block.strip().split('\\n'):
        if ':' in line:
            key, value = [x.strip() for x in line.split(':', 1)]
            #print("key:", key, " ------ val:", value)
            if key.lower() in ['resolution', 'mm', 'inch']:
                width, height = [float(x) for x in value.split('x')]
                resolution[key.lower()] = {'width': width, 'height': height}
            elif key.lower() == 'type':
                resolution['type'] = value
            else:
                resolution[key.lower().replace(' ', '_')] = value
    resolutions.append(resolution)

#print(resolutions)

# Update the dictionary with the new resolution data
for resolution in resolutions:
    type_name = resolution['type']
    sensors_data[VENDOR][CAMERA][type_name] = resolution

# Write the updated dictionary back to sensors.json
with open('sensors.json', 'w') as f:
    json.dump(sensors_data, f, indent=2)
