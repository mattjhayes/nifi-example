#!/usr/bin/env python3
"""
Simple Python 3 script that uses HTTP POST
to send data into NiFi at regular intervals
as part of a demo
"""
import os
from pathlib import Path
import json
import requests

URL = 'http://localhost:65432/events'

DIRPATH = 'sample_data/events'

# Sort input files alphabetically:
sorted_files = sorted(Path(DIRPATH).iterdir())

for file_name in sorted_files:
    # Open JSON file:
    files = open(file_name)
    # return JSON dictionary:
    json_data = json.load(files)
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain', 'Content-Disposition': 'attachment', 'filename': file_name.name}
    result = requests.post(URL, json=json_data, headers=headers)

    print("result for", file_name, "was", result.status_code)
