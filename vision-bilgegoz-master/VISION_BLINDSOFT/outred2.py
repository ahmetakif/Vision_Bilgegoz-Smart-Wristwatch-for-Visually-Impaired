#run command on terminal libraries
import subprocess
import shlex
#opencv
import cv2

#looper
while True:
#initialize the camera
    cam = cv2.VideoCapture(0)
    ret, image = cam.read()
    if ret:
        cv2.imwrite("/home/pi/ocr/images/1.jpg", image)
    cam.release()
    command = shlex.split("tesseract /home/pi/ocr/images/1.jpg stdout")
    process = subprocess.Popen(command, stdout=subprocess.PIPE)
    output, err = process.communicate()
    print (output)
