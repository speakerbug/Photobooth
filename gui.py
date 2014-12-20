#!/usr/bin/python
 
from Tkinter import * #Note Tkinter for python 2.*, tkinter for python 3+
# if you are using Python 3, comment out the previous line
# and uncomment the following line
# from tkinter import *

from time import sleep
import picamera
 
#Set display sizes
WINDOW_W = 500
WINDOW_H = 100
def createDisplay():
    global tk
    # create the tk window - within which
    # everything else will be built.
    tk = Tk()
    #Add a canvas area ready for drawing on
    canvas = Canvas(tk, width=WINDOW_W, height=WINDOW_H)
    canvas.pack()
    #Add an exit button
    btn = Button(tk, text="Exit", command=terminate)
    btn.pack()
    picBtn = Button(tk, text="Take a Picture", command=takeAPic)
    picBtn.pack()
    # Start the tk main-loop (this updates the tk display)
    tk.mainloop()
    
def terminate():
    global tk
    tk.destroy()
    
def takeAPic():
    with picamera.PiCamera() as camera:
        camera.hflip=True
        camera.start_preview()
        sleep(2)
        camera.capture('/home/pi/Desktop/Photobooth/image.jpg')
        camera.stop_preview()
        
        #upload online
        from poster.encode import multipart_encode
        from poster.streaminghttp import register_openers
        import urllib2
        
        # Register the streaming http handlers with urllib2
        register   _openers()
        
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