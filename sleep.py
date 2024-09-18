import serial
import time
#Send time and sound frequencies to two csv files and clean it
ser = serial.Serial()
ser.baudrate = 115200
ser.port = 'COM4'
ser.open()
fsound = open("sound.csv", "a", encoding = "utf-8")
ftime = open("time.csv", "a", encoding = "utf-8")
on = True
while True:
    data = str(ser.readline())
    data = data.replace("b","")
    data = data.replace("'","")
    data = data.replace(" ","")
    data = data.replace("\\r\\n","")
    if len(data) <= 3:
        print (data)
        fsound.write(data+",")
        t = time.localtime()
        current_time = time.strftime ("%H:%M:%S",t)
        ftime.write(current_time+",")
        print (current_time)
#Stop when button A is pressed
    if data == "999":
        break
fsound.close()
ftime.close()
print ("______\n")
#change the csv data to a list and get rid of any non int elements and "999"
filename= "sound.csv"
with open(filename) as file_object:
    for line in file_object:
        soundf=line.split(",")
        soundf = [item.replace(" ","") for item in soundf]
        soundf = [item.replace("999", "") for item in soundf]
        soundf = [item.replace("\\n", "") for item in soundf]
        soundf_updated = [value for value in soundf if value != ""]
        
        #print (max(soundf_updated))
print (soundf_updated)
#Print the index of the loudest noise        
print ("Sound",soundf_updated.index(max(soundf_updated))+1,"is highest.")
#change the time file into a list and get rid of empty elements so they match the sound levels      
timefile= "time.csv"
with open(timefile) as time_object:
    for time in time_object:
        timelist=time.split(",")
        timelist_updated = [value for value in timelist if value != ""]
print (timelist_updated)

#Print time of the loudest noise
print ("The time of the loudest noise was:",timelist[(soundf.index(max(soundf)))+1])
