import serial
import time

ser = serial.Serial('/dev/ttyUSB2',115200,timeout=1)

ser.write(b'AT+CSQ\r')

time.sleep(1)

print(ser.read_all().decode())