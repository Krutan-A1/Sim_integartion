import serial
import time

ser = serial.Serial('/dev/ttyUSB2',115200,timeout=1)

def send(cmd):
    ser.write((cmd+"\r").encode())
    time.sleep(1)
    print(ser.read_all().decode(errors="ignore"))

send("AT")
send("AT+CREG?")
send("AT+COPS?")