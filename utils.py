import json

FILE = 'operations.json'


def main():
    with open(FILE, 'r', encoding='utf-8') as file:
        data = json.load(file)