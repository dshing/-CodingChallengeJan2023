import json
from collections import OrderedDict

# find data points that fit f(t-1) > f(t) < f(t+1)
# Assuming the first data point is also included because it matches f(t) < f(t+1)
# or last datapoint matches f(t-1) > f(t)
def method_A(set):

    minima_values = []

    if (len(set) == 1):
        return []

    for key, value in set.items():
        # deal with out of bounds keys
        if (key == 1 and set[key + 1] > value): 
            minima_values.append([value, key])
        elif (key == len(set) and value < set[key - 1]):
            minima_values.append([value, key])
        # f(t-1) > f(t) < f(t+1)
        elif (set[key - 1] > value and value < set[key + 1]):
            minima_values.append([value, key])
    
    return minima_values

# Calculate e(t) = f(t)-f(t-1), check when there is a transition from e<0 to e>0
def method_B(set):
    prev_change = 0

    minima_values = []

    if (len(set) == 1):
        return []

    # want to compare 1 key value to another
    for key, value in set.items():
        if (key > 1):
            # first get the change value
            change = sign_change_B(value, set[key - 1])
            # compare change value with previous (e<0 to e>0)
            if (prev_change < 0 and change > 0):
                minima_values.append([value, key])
            prev_change = change
    return minima_values

# e(t) = f(t)-f(t-1) function
def sign_change_B(current_val, prev_val):
    change = current_val - prev_val

    return change    

time_value = OrderedDict()
# Json parse
file = open("./finding_local_minima/data.json")
data = json.load(file)

for item in data:
    time_value[item["time"]] = item["close"]
file.close


print(f"Method A local minima: {method_A(time_value)}") # [[9614.24, 1], [9620.68, 8], [9640.31, 14]]
print(f"Method B local minima: {method_B(time_value)}") # [[9629.47, 9], [9641.54, 15]]
