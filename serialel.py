import datetime
import time
import serial
import json
cels = '°C'
oldtemp = '0'
oldtime = 0
time.sleep(1);

ser = serial.Serial()
ser.baudrate = 9600
ser.port='COM3'
    

try:
    ser.open()
except Exception: 
    print("error open serial port: ")
    exit()

if ser.isOpen():
    ser.flushInput()
    ser.flushOutput()
    print('Opening serial...')
else:
    print("Cannot open serial port")

print(ser.name)
while ser.is_open == True:
    serTemp = ser.readlines(1)
    temp = ''.join(str(e) for e in serTemp) 
    time.sleep(1)
    ser.flushInput() 

    if(oldtemp != temp):
        
        times = time.strftime('%H:%M:%S')
        #convert time to seconds
        h,m,s = times.split(":")
        currsecs = int(datetime.timedelta(hours=int(h),minutes=int(m),seconds=int(s)).total_seconds())
        timediff = currsecs - oldtime
        str1 = '+' + str(timediff) +'s '
        print(str1)
        
        #when if, count the time difference between times and put +smth
        str2 = temp[2:7]
        print(str2)
        str3 = "{"
        str4 = "}"
        str5 = str3 + str1 + ", " + str2 + str4
        str6 = '"' + str5 + '"'
        vals = str6
        data = json.loads(vals)

        with open('./temps.json', 'a') as outfile:
            json.dump(data, outfile, indent= 2 )
            outfile.write(', \n')
        oldtime = currsecs
    else:
        None
    oldtemp = temp
else:
    time.sleep(1)

