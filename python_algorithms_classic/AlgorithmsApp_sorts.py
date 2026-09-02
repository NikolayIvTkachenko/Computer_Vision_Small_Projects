# алгоритмы сортировки

# сортировка пузырьком (bubble sort)
# сртировка вставками (insertion sort)
# сортировка слиянием (merge sort)
# сортирвка Шелла (shell sort)
# сортировка выбором (selection sort)

# ==========================================================================================

# Bubble Sort
listTest = [5, 8, 3, 1, 9, 2, 4]

def sortTest(list):
    lastElementIndex = len(list) - 1
    print(0, list)
    for idx in range(lastElementIndex):
        if list[idx] > list[idx+1]:
            list[idx], list[idx+1] = list[idx+1], list[idx]
    print(idx+1, list)

def sortBubble(list):
    lastElementIndex = len(list) - 1
    for passNo in range(lastElementIndex, 0, -1):
        for idx in range(passNo):
            if list[idx] > list[idx+1]:
                list[idx], list[idx+1] = list[idx+1], list[idx]
    return list



# Isertion Sort

def sortInsertion(list):
    for i in range(1, len(list)):
        j = i - 1
        element_next = list[i]

        while(list[j] > element_next) and (j >= 0):
            list[j + 1] = list[j]
            j = j - 1
        list[j + 1] = element_next
    return list

# Merge Sort

# Псевдо код
# def sortMerge(list, start, end):
#    if (start < end)
#       midPoint = (end - start) / 2 + start
#
#

def sortMerge(list):
    if len(list) > 1:
        mid = len(list) // 2
        left = list[:mid]
        right = list[mid:]

        sortMerge(left)
        sortMerge(right)

        a = 0
        b = 0
        c = 0

        while a < len(left) and b < len(right):
            if left[a] < right[b]:
                list[c] = left[a]
                a = a + 1
            else:
                list[c] = right[b]
                b = b + 1
            c = c + 1

        while a < len(left):
            list[c] = left[a]
            a = a + 1
            c = c + 1

        while b < len(right):
            list[c] = right[b]
            b = b + 1
            c = c + 1
    return list

# Shell Sort

def sortShell(list):
    distance = len(list) // 2
    while distance > 0:
        for i in range(distance, len(list)):
            temp = list[i]
            j = i
            while j >= distance and list[j - distance] > temp:
                list[j] = list[j - distance]
                j = j - distance
            list[j] = temp
        distance = distance // 2
    return list

# Selection Sort

def sortSelection(list):
    for fill_slot in range(len(list) - 1, 0, -1):
        max_index = 0
        for location in range(1, fill_slot + 1):
            if list[location] > list[max_index]:
                max_index = location
        list[fill_slot], list[max_index] = list[max_index], list[fill_slot]
    return list

# Search algorithm
# Linear Search
def linearSearch(list, item):
    index = 0
    found = False
    while index < len(list) and found is False:
        if list[index] == item:
            found = True
    else:
        index = index + 1
    return found
# Binary Search


print("====  Test Algorithms ====")
print()
print("====  Bubble Sort  ====")
print(sortBubble(listTest))
print()

print("====  Insertion Sort  ====")
print(sortInsertion(listTest))
print()

print("====  Merge Sort  ====")
print(sortMerge(listTest))
print()

print("====  Shell Sort  ====")
print(sortShell(listTest))
print()

print("====  Selection Sort  ====")
print(sortSelection(listTest))
print()

# Search algorithm
print("====  Linear Search  ====")
print(linearSearch(listTest, 1))
print()

print("====  Binary Search  ====")
print(linearSearch(listTest, 1))
print()

