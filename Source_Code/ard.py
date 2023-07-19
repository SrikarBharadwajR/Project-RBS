# import serial

# ser = serial.Serial('COM5', 9600) 

# while True:
#     data = ser.readline().decode('utf-8').rstrip()
#     print(data)
import serial
import time

arduino=serial.Serial('COM5', 9600)
time.sleep(2)

print("Enter 1 to turn ON LED and 0 to turn OFF LED")


while 1:
    
    datafromUser=[0, 0, 0, 0, 1, 0]
    
    if datafromUser[0]==1:
        arduino.write(b'1')
        
    if datafromUser[1] == 1:
        arduino.write(b'2')
        
    if datafromUser[2] == 1:
        arduino.write(b'3')
    
    if datafromUser[3]==1:
        arduino.write(b'4')
        
    if datafromUser[4] == 1:
        arduino.write(b'5')
        
    if datafromUser[5] == 1:
        arduino.write(b'6')
    
    arduino.close()
    


