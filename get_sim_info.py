import serial
import time

ser = serial.Serial('/dev/ttyUSB2',115200,timeout=1)

commands = [
    "AT+CCID",
    "AT+CIMI",
    "AT+CNUM",
    "AT+CGSN"
]

for c in commands:
    ser.write((c+"\r").encode())
    time.sleep(1)
    print(ser.read_all().decode())