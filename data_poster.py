#
"""
Send forecast data into NiFi
"""

import json
import requests

url = 'http://localhost:65432/forecast'

file_name = "sample_data/cloud-dine-forecast-20230815.txt"

# Open JSON file:
f = open(file_name)
# return JSON dictionary:
json_data = json.load(f)

result = requests.post(url, json = json_data)

print(result.text)
