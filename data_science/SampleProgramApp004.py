path = "data_files/short_story_01.txt"

with open(path, "r") as f:
    content = f.read()
    print(content)

print("1 => =================")

with open(path, "r") as f:
    for i, line in enumerate(f):
        if line.strip():
            print(f"Line {i}: ", line.strip())

print("2 => =================")

with open(path, "r") as f:
    lst = [line.strip() for line in f if line.strip()]

print(len(lst))
print(lst)

print("3 => =================")
import csv
path_csv_01 = "data_files/cars.csv"

with open(path_csv_01, "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    cars = []
    for row in csv_reader:
        cars.append(dict(row))
print(cars)

print("4 => =================")
path_csv_02 = "data_files/cars.csv"
with open(path_csv_02, "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    cars = []
    for row in csv_reader:
        cars.append(row)
print(cars)

print("5 => =================")
print("Двоичный файл ========")

image_path = "data_files/1111.jpg"
with open(image_path, "rb") as image_file:
    content = image_file.read()
print(len(content))


print("6 => =================")
print("Экспортирование данных в файл ========")

for row in cars:
    print(list(row.values()))

to_update = ['1999', 'Chevy', 'Venture']
new_price = '4500.00'

path_to_save = "data_files/to/cars_new.csv"

with open(path_to_save, "w") as csv_file:
    fieldnames = cars[0].keys()
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    for row in cars:
        if set(to_update).issubset(set(row.values())):
            row['Price'] = new_price
        writer.writerow(row)





























