import os

# os.chdir(os.path.dirname(os.path.abspath(__file__)))


def read_price():
    filepath = 'price1.txt'
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

print(read_price())