import serial
import csv
import time
from datetime import datetime

ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)

with open('ta.csv', 'a', newline='') as f:
    writer = csv.writer(f)

    while True:
        ser.write(b"rx\n")
        time.sleep(10)
        line = ser.readline().decode('utf-8').strip()
        if line:
            timestamp = datetime.now().isoformat()
            writer.writerow([timestamp, line])
            print(timestamp, line)
