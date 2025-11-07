import argparse
import csv
from tabulate import tabulate, tabulate_formats

def data_filtering(data, headers, report):
    if report is None:
        print("WARNING: The report filter was not set")
    else:
        match report:
            case a if report.upper() == "AVERAGE-RATING":
                for row in data:
                    del row[0]
                    del row[1]
                headers = [headers[1], headers[3]]
                new_data = []
                print(data[2][0])
                for i, row in enumerate(data):
                    brand = row[0]
                    print(f"Index: {i}, Item: {row}")
                    for j, element in enumerate(data):
                        if brand == data[j][0]:
                            print(data[j][0])
            case _:
                print("WARNING: The report filter was not found")

    return headers

parser = argparse.ArgumentParser(description='Output the csv files')
parser.add_argument('--files', metavar='files', nargs='*', type=str, help='Input the csv file')
parser.add_argument('--report', metavar='report', type=str, help='Input the report filter')
args = parser.parse_args()

files = args.files
report = args.report

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

# Calling data filtering // Вызываем фильтрацию данных
headers = data_filtering(data, headers, report)

# Making indexes start from 1 instead of 0 // Делаем чтобы индексы начинались с 1 а не 0
rowIDs = range(1, len(data)+1)

# Printing the result into the console // Выводим результат в консоль
print(tabulate(data, headers=headers, showindex=rowIDs, tablefmt="psql"))