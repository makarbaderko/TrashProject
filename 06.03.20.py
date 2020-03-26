import serial
import time
ad = '/dev/tty.wchusbserialfd120'

def init():
    global ad
    arduino = serial.Serial(ad, 9600)
    return arduino
def stop(arduino):
    arduino.close()
def lin(arduino):
    inpu = str(arduino.readline().decode('utf-8'))
    return inpu 
def answer(arduino, ans):
    arduino.write(str(ans).encode())
def logics(inpu):
    if inpu == "0":
        a = "0"
    else:
        a = "1"
    return a
def main():
    arduino = init()
    line = lin(arduino)
    ans = logics(line)
    answer(arduino, ans)
    time.sleep(1.5)
    stop(arduino)
    print(line, ans)
while True:
    main()