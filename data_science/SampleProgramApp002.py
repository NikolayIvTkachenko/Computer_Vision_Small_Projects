

#=======================================================================================================================================================

print("======= Словари. Преобразование JSON в словарь ======")

d = {
    "PONumber"              : 2608,
    "ShippingInstructions"  : {
        "name"      : "John Silver",
        "Address"   : {
            "street"    : "426 Light Street",
            "city"      : "South San Francisco",
            "state"     : "CA",
            "zipCode"   : 99237,
            "country"   : "United States of America"
        },
        "Phone"         : [{"type":  "Office", "number":  "809-123-9309"},
                           {"type":  "Mobile", "number":  "417-123-4567"}
        ]
    }
}

import json

# Сохраняем в файл json
with open("po.json", "w") as outfile:
    json.dump(d, outfile)

# Читаем из файла
with open("po.json") as fp:
    dd = json.load(fp)

print(dd)


#=======================================================================================================================================================

print("======= Множества ======")

mm = {'London', 'New York', 'Paris'}

lst = ['John Silver', 'Tim Jemison', 'John Silver', 'Maya Smith']
print(lst)
lst = list(set(lst))
print(lst)

# сохраняем порядок списка
lst01 = ['John Silver', 'Tim Jemison', 'John Silver', 'Maya Smith']
print(lst01)
lst01 = list(sorted(set(lst01), key=lst01.index))
print(lst01)


#=======================================================================================================================================================

print("======= Множества пересечения ======")

photo1_tags = {'coffee', 'breakfast', 'drink', 'table', 'tableware', 'cup', 'food'}
photo2_tags = {'food', 'dish', 'meat', 'meal', 'tableware', 'dinner', 'vegetable'}

intersection = photo1_tags.intersection(photo2_tags)

if len(intersection) >= 2:
    print("The photos contain similar objects.")
print("photo1_tags")
print(photo1_tags)
print("photo2_tags")
print(photo2_tags)
print("intersection")
print(intersection)




























