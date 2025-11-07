import argparse
import csv
from tabulate import tabulate, tabulate_formats

def data_filtering(data, headers, report):
    if report is None:
        print("WARNING: The report filter was not set.")
    else:
        try:
            match report:
                case a if report.upper() == "AVERAGE-RATING": # Using this for those people with Caps Lock problem // Делаем это для людей у которых проблемы с капс локом
                    for row in data:
                        del row[0]
                        del row[1]
                    headers = [headers[1], headers[3]]

                    new_data = []
                    filtered_brands = [] # Using this method not to error out // Используем этот метод чтобы не получить ошибку

                    for i, row in enumerate(data):
                        if row[0] not in filtered_brands:
                            brand = row[0]
                            avb_numbers = []
                            for j, element in enumerate(data):
                                if brand == data[j][0]:
                                    avb_numbers.append(float(data[j][1]))
                            avb = round(sum(avb_numbers) / len(avb_numbers), 2)
                            filtered_brands.append(brand)
                            new_data.append([brand, avb])

                    data = new_data
                case _:
                    print("WARNING: The report filter was not found.")
        except:
            print("ERROR: Something went wrong during report filtration.")
            exit(0)
    
    return headers, data

parser = argparse.ArgumentParser(description='Output the csv files')
parser.add_argument('--files', metavar='files', nargs='*', type=str, help='Input the csv file')
parser.add_argument('--report', metavar='report', type=str, help='Input the report filter')
args = parser.parse_args()

files = args.files
report = args.report

data = []
headers = []
# Reading and saving the csv file content to be tabulated later // Читаем и сохраняем содержимое csv файла для будущего сведения в таблицу
if files is None:
    print(f"WARNING: Please run the script with at least 1 specified file.")
    exit(0)
else:
    for file in files:
        try:
            with open(file, newline='') as csvfile:
                reader = csv.reader(csvfile)
                current_headers = next(reader)
                # Saving headers // Сохраняем заголовки
                if not headers:
                    headers = current_headers
                # Adding rows // Добавляем строки
                for row in reader:
                    data.append(row)
        except:
            print(f"ERROR: During the attempt to open {file}, the script encountered the problem.\nPlease check for it being vaild file/filepath.")
            exit(0)

# Calling data filtering // Вызываем фильтрацию данных
headers, data = data_filtering(data, headers, report)

# Making indexes start from 1 instead of 0 // Делаем чтобы индексы начинались с 1 а не 0
rowIDs = range(1, len(data)+1)

# Printing the result into the console // Выводим результат в консоль
print(tabulate(data, headers=headers, showindex=rowIDs, tablefmt="psql"))