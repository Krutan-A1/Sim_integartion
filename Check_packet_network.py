import serial
import time

ser = serial.Serial('/dev/ttyUSB2',115200,timeout=1)

ser.write(b'AT+CGATT?\r')

time.sleep(1)

print(ser.read_all().decode())