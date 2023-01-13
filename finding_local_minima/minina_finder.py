import json

# Basic iterate through all to find the lowest 
# Very slow time complexity on large databases O(n)
# Should opt for better algorithms like random access...
# or others that reduce the amount of data point
def method_A(set):
    lowest = 0.0
    key_idx = 0
    first = True

    for key, value in set.items():
        if (first):
            lowest = value
            key_idx = key
            first = False
            # Add the first key value pair, because unordered dict ...
            # I don't know if time = 1 is first
        if (value < lowest):
            lowest = value
            key_idx = key
    return [lowest, key_idx]

# Assuming it is to detect the largest drop between two values in a dataset
def method_B(set):
    lowest_change = 0
    lowest_val = 0
    key_lowest = 0
    # want to compare 1 key value to another
    for key, value in set.items():
        if (key > 1):
            prev_val = set[key - 1]
            change = value - prev_val
            if (change < lowest_change):
                lowest_change = change
                lowest_val = value
                key_lowest = key
    print(f"Lowest change is from {key_lowest} to {key_lowest - 1}: {lowest_change}")
    return [lowest_val, key_lowest]

time_value = {}
# Json parse
file = open("./finding_local_minima/data.json")
data = json.load(file)

for item in data:
    time_value[item["time"]] = item["close"]
file.close

print(method_A(time_value))
print(method_B(time_value))
