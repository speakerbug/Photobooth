#!/usr/bin/python
 
from Tkinter import * #Note Tkinter for python 2.*, tkinter for python 3+
# if you are using Python 3, comment out the previous line
# and uncomment the following line
# from tkinter import *

from time import sleep
import picamera
import os
import RPi.GPIO as GPIO

right_button = 3
left_button = 5

GPIO.setup(3, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(5, GPIO.IN, GPIO.PUD_UP)

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
    #tk.attributes('-fullscreen', True)
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
    tk.mainloop()
    
    while GPIO.input(left_button) and GPIO.input(right_button):
        pass
        if GPIO.input(left_button) == False:
            print("Left button pressed")
        if GPIO.input(right_button) == False:
            print("Right button pressed")
    
def terminate():
    global tk
    tk.destroy()
    
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
    v.set("Smile and freeze! It takes about a second to capture an image!")
    tk.update()
    os.system("raspistill -ex antishake -o image.jpg -p 300,220,1300,744")
    tk.update()
    v.set("Click the button below to take a picture!")
    tk.update()
        
def updateText(newV):
    global v
    v.set(newV)
 
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
