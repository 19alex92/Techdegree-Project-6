import json
import os

from catalog import models

filepath = os.path.dirname(__file__)
file_path = os.path.join(filepath, 'catalog/static/catalog/json/minerals.json')

with open(file_path, encoding="utf8") as json_file:
    data = json.load(json_file)
    for value in data:
        print(value['name'])