import os
import mozg

def removing():
    os.remove("/Users/makar/Documents/Programming/AI/Trash/v 3.0.0/image_to_train.jpg")
    
def predicting():
    mozg.predict()
    
def run():
    predicting()
    removing()
def check():
    f = open('btn.txt', 'r')
    btn = str(f.read())
    f.close()
    if btn == "1":
        run()
        f = open('btn.txt', 'w')
        f.write("0")
        f.close()
    if btn == "2":
        break
while True:
    check()