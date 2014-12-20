from time import sleep
import picamera

with picamera.PiCamera() as camera:
	camera.hflip = True
        camera.start_preview()
	sleep(2)
        camera.capture('/home/pi/Desktop/Photobooth/image.jpg')
        camera.stop_preview()

# test_client.py
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

