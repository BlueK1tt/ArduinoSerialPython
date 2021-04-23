import datetime
import time
import serial #need to download pyserial
import json
cels = '°C'
oldtemp = '0'
oldtime = 0
i = 0
br = "\n"
time.sleep(1.5);

#attributes for serial
ser = serial.Serial()
ser.baudrate = 9600
ser.port='COM3'

#try to open serial    
try:
    ser.open()
except Exception: 
    print("error open serial port: ")
    exit()

#after opening serial, remove all data in serial buffer
if ser.isOpen():
    ser.flushInput()
    ser.flushOutput()
    print('Opening serial...')
else:
    print("Cannot open serial port")

print(ser.name) #print the name of the serial port
print(time.strftime('%H:%M:%S')); #print the current time of date


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
        str1 = 'Time:' + '+' + str(timediff) +'s'
        print(str1)
        
        #when if, count the time difference between times and put +smth
        str2 = temp[2:7] #cut the input data from 2 to 7 position of letters, could have problem if temperature goes over 100 or under 0
        print(str2)

        dataTime = str1
        dataTemp = "Temp:" + str2 

        str3 = "{"
        str4 = "}"
        str5 = str3 + dataTime + ", " + dataTemp + str4
        strF = '"' + str5 + '"'
        vals = strF
        data = json.loads(vals)

        with open('./temps.json', 'a') as outfile:
            if (i == 0):
                outfile.write(times)
                outfile.write(': \n');
            json.dump(data, outfile, indent= 2 )
            outfile.write(', \n')
            i += 1
            print(i);
        oldtime = currsecs
    else:
        None
    oldtemp = temp
else:
    time.sleep(0.5)
