#!/usr/bin/python
 
from Tkinter import * #Note Tkinter for python 2.*, tkinter for python 3+
# if you are using Python 3, comment out the previous line
# and uncomment the following line
# from tkinter import *

from time import sleep
import picamera
import os
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.OUT)

#Set display sizes
WINDOW_W = 500
WINDOW_H = 100

def createDisplay():
    global tk
    global v
    global textlabel
    # create the tk window - within which
    # everything else will be built.
    tk = Tk()
    tk.attributes('-fullscreen', True)
    v = StringVar()
    v.set("Click the button below to take a picture!")
    textlabel = Label(tk, textvariable=v, bg="green", fg="black", font=("Helvetica", 45))
    textlabel.pack(fill=X)
    picBtn = Button(tk, text="Take a Picture", command=takeAPic)
    picBtn.pack(fill=X)
    #Add an exit button
    btn = Button(tk, text="Exit", command=terminate)
    btn.pack(fill=X)
    # Start the tk main-loop (this updates the tk display)
    checkForButton()
    
def terminate():
    global tk
    tk.destroy()

def checkForButton():
    global tk
    notPressed = True
    while notPressed:
        input_state = GPIO.input(18)
        tk.update()
        if input_state == False:
            notPressed = False
    takeAPic()
    
def takeAPic():
    global v
    global textlabel
    global tk
    v.set("Taking picture in 3 seconds...")
    tk.update()
    sleep(1)
    v.set("Taking picture in 2 seconds...")
    tk.update()
    sleep(1)
    v.set("Taking picture in 1 second...")
    tk.update()
    sleep(1)
    whiteLED()
    v.set("Smile and freeze! It takes about a second to capture an image!")
    tk.update()
    os.system("raspistill -ex antishake -o image.jpg -p 300,220,1300,744")
    tk.update()
    v.set("Uploading picture online...")
    tk.update()
    uploadPic()
    v.set("Click the button below to take a picture!")
    tk.update()
    checkForButton()
        
def updateText(newV):
    global v
    v.set(newV)
    
def delayMicroseconds(microseconds):
    seconds = microseconds / float(1000000)  # divide microseconds by 1 million for seconds
    sleep(seconds)
    
def whiteLED():   
    delayMicroseconds(408);
    pulseIR(8820);
    delayMicroseconds(4360);
    pulseIR(640);
    delayMicroseconds(480);
    pulseIR(560);
    delayMicroseconds(520);
    pulseIR(560);
    delayMicroseconds(520);
    pulseIR(580);
    delayMicroseconds(520);
    pulseIR(580);
    delayMicroseconds(520);
    pulseIR(560);
    delayMicroseconds(520);
    pulseIR(580);
    delayMicroseconds(520);
    pulseIR(580);
    delayMicroseconds(520);
    pulseIR(560);
    delayMicroseconds(1620);
    pulseIR(580);
    delayMicroseconds(1600);
    pulseIR(640);
    delayMicroseconds(1560);
    pulseIR(620);
    delayMicroseconds(1580);
    pulseIR(580);
    delayMicroseconds(1600);
    pulseIR(640);
    delayMicroseconds(1560);
    pulseIR(620);
    delayMicroseconds(1560);
    pulseIR(600);
    delayMicroseconds(1580);
    pulseIR(660);
    delayMicroseconds(440);
    pulseIR(600);
    delayMicroseconds(520);
    pulseIR(560);
    delayMicroseconds(1620);
    pulseIR(580);
    delayMicroseconds(520);
    pulseIR(560);
    delayMicroseconds(520);
    pulseIR(580);
    delayMicroseconds(520);
    pulseIR(580);
    delayMicroseconds(1600);
    pulseIR(640);
    delayMicroseconds(460);
    pulseIR(580);
    delayMicroseconds(1600);
    pulseIR(640);
    delayMicroseconds(1560);
    pulseIR(620);
    delayMicroseconds(460);
    pulseIR(580);
    delayMicroseconds(1640);
    pulseIR(620);
    delayMicroseconds(1560);
    pulseIR(580);
    delayMicroseconds(1600);
    pulseIR(640);
    delayMicroseconds(460);
    pulseIR(580);
    delayMicroseconds(1600);
    pulseIR(640);
    delayMicroseconds(38920);
    pulseIR(8820);
    delayMicroseconds(2160);
    pulseIR(580);
    
def pulseIR(microsecs):
    while microsecs > 0:
        # 38 kHz is about 13 microseconds high and 13 microseconds low
        GPIO.output(17,GPIO.HIGH)  # this takes about 3 microseconds to happen
        delayMicroseconds(10);         # hang out for 10 microseconds
        GPIO.output(17,GPIO.LOW)   # this also takes about 3 microseconds
        delayMicroseconds(10);         # hang out for 10 microseconds
 
        # so 26 microseconds altogether
        microsecs -= 26;
 
def uploadPic():
    #upload online
    from poster.encode import multipart_encode
    from poster.streaminghttp import register_openers
    import urllib2
    # Register the streaming http handlers with urllib2
    register_openers()
    
    # Start the multipart/form-data encoding of the file "DSC0001.jpg"
    # "image1" is the name of the parameter, which is normally set
    # via the "name" parameter of the HTML <input> tag.
    
    # headers contains the necessary Content-Type and Content-Length
    # datagen is a generator object that yields the encoded parameters
    datagen, headers = multipart_encode({"image": open("image.jpg", "rb")})
    
    # Create the Request object
    request = urllib2.Request("http://henrysaniuk.com/upload/index.php", datagen, headers)
    # Actually do the request, and get the response
    print urllib2.urlopen(request).read()
    
def main():
    createDisplay()
 
if __name__ == '__main__':
    main()
