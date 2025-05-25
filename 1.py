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

# Код Кубуши Олексія (Зчитування JSON файлу Дениса, додавання нових рядків та запис у новий CSV файл)
# Імена файлів
csv_file1 = "kubcsv.csv"
json_file1 = "danyjson.json"

# Дані для запису
dany1 = [
    {"Ім'я": "Кубуша", "Предмет": "Вища математика", "Оцінка": 92},
    {"Ім'я": "Кубуша", "Предмет": "Дискретна математика", "Оцінка": 100},
    {"Ім'я": "Кубуша", "Предмет": "Програмування", "Оцінка": 98},
]

# Читання з JSON файлу
try:
    with open(json_file1, mode='r', encoding='utf-8') as file:
        rows = json.load(file)
except FileNotFoundError:
    print("JSON файл Дениса не знайдено")
    rows = []

# Додаємо нові рядки
rows.extend(dany1)
print(f"Нові рядки додано")

# Запис у CSV файл
try:
    with open(csv_file1, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["Ім'я", "Предмет", "Оцінка"])
        writer.writeheader()
        writer.writerows(rows)
    print("CSV файл Кубуши створено")
except Exception as e:
    print(f"Помилка при записуванні у CSV файл: {e}")

# Кінець коду Кубуши Олексія