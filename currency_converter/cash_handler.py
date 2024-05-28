import os
import json

CACHE_FILE = 'cache.json'


def load_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, 'r') as cache_file:
            return json.load(cache_file)
    return {}


def save_cache(cache):
    with open(CACHE_FILE, 'w') as cache_file:
        json.dump(cache, cache_file)
