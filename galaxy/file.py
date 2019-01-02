# Fetches Youtube API music and displays from text array
import random

file_map = {}
def fetch_line(file_name):
    global file_map
    if not (file_name in file_map.keys()):
        with open(file_name, 'r') as f:
            file_map[file_name] = f.readlines()
    return random.choice(file_map[file_name])