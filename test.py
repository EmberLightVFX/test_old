import re
from collections import defaultdict

# Input string
input_string = """
6016 × 3200       Cinema       23.5 mm × 12.5 mm (0.925 in x 0.492 in)

6016 × 3200       CinemaDNG       23.5 mm × 12.5 mm (0.925 in x 0.492 in)
5760 × 3240       CinemaDNG       22.5 mm × 12.7 mm (0.886 in x 0.500 in)
4096 × 2160       CinemaDNG       23.5 mm × 12.5 mm (0.925 in x 0.492 in)
3944 x 2088       CinemaDNG       15.4 mm × 8.2 mm (0.606 in x 0.323 in)
3840 × 2160       CinemaDNG       22.5 mm × 12.7 mm (0.886 in x 0.500 in)
3712 × 2088       CinemaDNG       14.5 mm × 8.2 mm (0.571 in x 0.323 in)

3840 × 2160       Apple ProRes 4444 XQ       22.5 mm × 12.7 mm (0.886 in x 0.500 in)
2048 × 1080       Apple ProRes 4444 XQ       15.4 mm × 8.2 mm (0.606 in x 0.323 in)
1920 x 1080       Apple ProRes 4444 XQ       14.5 mm × 8.2 mm (0.571 in x 0.323 in)

5280 x 2160       Apple ProRes 422 HQ       23.5 mm × 9.6 mm (0.925 in x 0.378 in)
4096 × 2160       Apple ProRes 422 HQ       23.5 mm × 12.5 mm (0.925 in x 0.492 in)
3840 × 2160       Apple ProRes 422 HQ       22.5 mm × 12.7 mm (0.886 in x 0.500 in)
2704 × 1520       Apple ProRes 422 HQ       14.5 mm × 8.2 mm (0.571 in x 0.323 in)
2048 × 1080       Apple ProRes 422 HQ       15.4 mm × 8.2 mm (0.606 in x 0.323 in)
1920 x 1080       Apple ProRes 422 HQ       14.5 mm × 8.2 mm (0.571 in x 0.323 in)
"""

# Split the input string into lines
lines = input_string.strip().split("\n")


# Define a function to process each line
def process_line(line):
    pattern = re.compile(
        r"(\d+)\s*[×x]\s*(\d+)\s+(.+?)\s+([\d.]+)\s*mm\s*[×x]\s*([\d.]+)\s*mm\s*\(([\d.]+)\s*in\s*x\s*([\d.]+)\s*in\)"
    )
    match = pattern.match(line)

    if match:
        res1 = int(match.group(1))
        res2 = int(match.group(2))
        descriptor = match.group(3).strip()
        mm1 = float(match.group(4))
        mm2 = float(match.group(5))
        in1 = float(match.group(6))
        in2 = float(match.group(7))

        return (res1, res2, descriptor, mm1, mm2, in1, in2)
    else:
        return None


# Process each line and filter out None results
results = [
    result for result in (process_line(line) for line in lines) if result is not None
]

# Group by descriptors to count their occurrences
descriptor_count = defaultdict(int)
for item in results:
    descriptor_count[item[2]] += 1

# Prepare the final results
final_results = []
for item in results:
    res1, res2, descriptor, mm1, mm2, in1, in2 = item
    print(descriptor_count[descriptor])
    if descriptor_count[descriptor] > 1:
        descriptor_with_resolution = f"{descriptor} {res1} × {res2}"
    else:
        descriptor_with_resolution = descriptor
    final_results.append([res1, res2, descriptor_with_resolution, mm1, mm2, in1, in2])


# Print the results
for result in final_results:
    print(result)
