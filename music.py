# Fetches Youtube API music and displays from text array
import random

file_map = {}
def fetchLine(filename):
    global file_map
    if not (filename in file_map.keys()):
        with open(filename, 'r') as f:
            file_map[filename] = f.readlines()
    return random.choice(file_map[filename])