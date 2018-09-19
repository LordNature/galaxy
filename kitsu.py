# Kitsu API wrapper by Nature
import json
from pprint import pprint

with open('data.json') as f:
    data = json.load(f)

pprint(data)
