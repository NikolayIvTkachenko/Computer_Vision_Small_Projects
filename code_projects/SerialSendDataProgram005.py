# Подключение Ардуино через питон
import time

import serial

ard = serial.Serial("COM3", 9600)

# Иногда не передает данные через последовательный пот, надо пекредавать много  раз в цикле
for x in range(500):
    ard.write(str.encode('0'))

time.sleep(1)
for x in range(500):
    ard.write(str.encode('1'))



