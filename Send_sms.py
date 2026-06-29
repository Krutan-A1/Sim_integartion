import serial
import time

ser = serial.Serial('/dev/ttyUSB2',115200,timeout=1)

ser.write(b'AT+CMGF=1\r')
time.sleep(1)

ser.write(b'AT+CMGS="+911234567890"\r')
time.sleep(1)

ser.write(b'Hello from M2M SIM')
ser.write(bytes([26]))

time.sleep(5)

print(ser.read_all().decode())