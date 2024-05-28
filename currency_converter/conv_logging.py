import os
import json


LOG_FILE = 'conversions.json'


def save_conversion_log(log_entry):
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'r') as log_file:
            log = json.load(log_file)
    else:
        log = []

    log.append(log_entry)

    with open(LOG_FILE, 'w') as log_file:
        json.dump(log, log_file)
