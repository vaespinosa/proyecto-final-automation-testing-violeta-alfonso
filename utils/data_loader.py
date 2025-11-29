import csv
import json
import os

def read_csv(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return [row for row in reader]

def read_json(file_path):
    with open(file_path, encoding='utf-8') as jsonfile:
        return json.load(jsonfile)
