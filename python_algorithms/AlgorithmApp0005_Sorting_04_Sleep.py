import threading
from time import sleep

def sleep_sort(i):
    sleep(i)
    global sortedlist

    sortedlist.append(i)
    return (i)

items = [2, 4, 5, 2, 1, 7]
sortedlist = []
ignore_result = [threading.Thread(target=sleep_sort, args=(i,)).start() for i in items]

print(sortedlist)