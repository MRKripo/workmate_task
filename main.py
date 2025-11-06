import argparse
import csv
from tabulate import tabulate, tabulate_formats

parser = argparse.ArgumentParser(description='Output the csv files')
parser.add_argument('--files', metavar='files', nargs='*', type=str, help='Input the csv file')
args = parser.parse_args()

files = args.files

data = []
headers = []
# Reading and saving the csv file content to be tabulated later // Читаем и сохраняем содержимое csv файла для будущего сведения в таблицу
for file in files:
    with open(file, newline='') as csvfile:
        reader = csv.reader(csvfile)
        current_headers = next(reader)
        # Saving headers // Сохраняем заголовки
        if not headers:
            headers = current_headers
        # Adding rows // Добавляем строки
        for row in reader:
            data.append(row)

# Making indexes start from 1 instead of 0 // Делаем чтобы индексы начинались с 1 а не 0
rowIDs = range(1, len(data)+1)

# Printing the result into the console // Выводим результат в консоль
print(tabulate(data, headers=headers, showindex=rowIDs, tablefmt="psql"))