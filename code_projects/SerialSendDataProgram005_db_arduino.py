import sqlite3
import struct

import serial
import time

ard = serial.Serial("COM3", 9600)

base = sqlite3.connect('pyard.db')
cursor = base.cursor()

data = 'SELECT * FROM LED'
while True:
    cursor.execute(data)
    themes = {}
    for x in cursor.fetchall():
        themes[x[0]] = x[1]
    led = themes['LED']
    print(led)
    if led == 0:
        ard.write(str.encode('0'))
    elif led == 1:
        ard.write(str.encode('1'))





# Пример работы
#https://www.youtube.com/watch?v=IdQ6-SDsorY