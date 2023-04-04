import json
from utils import filter_sort, format_data

FILE = 'operations.json'


def main():
    with open(FILE, 'r', encoding='utf-8') as file:
        data = json.load(file)

    data = filter_sort(data)

    for i in range(5):
        print(format_data(data[i]))
        print()


if __name__ == '__main__':
    main()
