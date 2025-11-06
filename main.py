import csv
from tabulate import tabulate, tabulate_formats

# Reading and saving the csv file content to be tabulated later // Читаем и сохраняем содержимое csv файла для будущего сведения в таблицу
with open('products1.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    data = list(reader)

# Making indexes start from 1 instead of 0 // Делаем чтобы индексы начинались с 1 а не 0
rowIDs = range(1, len(data))

# Printing the result into the console // Выводим результат в консоль
print(tabulate(data, headers="firstrow", showindex=rowIDs, tablefmt="psql"))