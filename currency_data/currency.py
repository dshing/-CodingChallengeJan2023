import requests
import time
import csv
import os
from datetime import datetime

# user defined variables
file_name = "data.csv"
api_url = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USDT&e=Binance"
currency_required = "USDT"
value_to_add = 9.999999

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 
full_path = os.path.join(desktop, file_name)

# Subtask 1 - I am assuming it only wants to print once
def subtask1(number_value):
    new_value = number_value + value_to_add
    print(new_value)

def requester(url):
    try:
        response = requests.get(api_url)
    except requests.ConnectionError as e:
        print(e)
    return response

first_loop = True

print("Press ctrl + c to stop program.")
try:
    while (True):
        
        req = requester(api_url)
        if (req and req.status_code == 200):
            curr_value = req.json()[currency_required]
            if (first_loop):
                subtask1(curr_value)
                first_loop = False
        else:
            # i'm assuming we dont want empty data points, so ignore if there is an error
            continue
        now = datetime.now()
        # subtask 2 write to csv with timestamp, assuming only value is wanted so USDT is not added
        with open(full_path, "a", newline='') as file:
            writer = csv.writer(file)      
            writer.writerow([now, curr_value])

        time.sleep(0.1)
except (KeyboardInterrupt):
    pass

