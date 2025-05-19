import csv
import json
import os

# Початковий код Денисенка Дениса для створення файлів та запису початкових даних
# Імена файлів
csv_file = "danycsv.csv"
json_file = "danyjson.json"

# Дані для запису
dany = [
    {"Ім'я": "Денис", "Предмет": "Вища математика", "Оцінка": 100},
    {"Ім'я": "Денис", "Предмет": "Дискретна математика", "Оцінка": 100},
    {"Ім'я": "Денис", "Предмет": "Програмування", "Оцінка": 100},
]

# Створення CSV-файлу
try:
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["Ім'я", "Предмет", "Оцінка"])
        writer.writeheader()
        writer.writerows(dany)
    print(f"CSV файл створено")
except:
    print(f"Помилка при записуванні у CSV файл")

# Читання з CSV файлу та створення і запис у JSON файл
try:
    with open(csv_file, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        rows = list(reader)
    try:
        with open(json_file, mode='w', encoding='utf-8') as file:
            json.dump(rows, file, indent=4, ensure_ascii=False)
        print(f"JSON файл створено")
    except:
        print(f"Помилка при записуванні у JSON файл")
except FileNotFoundError:
    print("CSV файл не знайдено")

# Кінець коду Денисенка Дениса