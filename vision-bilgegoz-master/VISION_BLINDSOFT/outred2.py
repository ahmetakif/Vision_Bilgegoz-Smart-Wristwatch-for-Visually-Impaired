######## VISION-Bilgegoz Image Capturing for Optical Character Recognition with Tesseract OCR #########
#
# Author: Ahmet Akif Kaya
# Date: 2/25/19
# Description:
# This program captures instant image from camera with OpenCV 
# and transfers that image to Tesseract OCR library with command line
# in order to make Optical Character Recognition and read texts for blind people.

# This code is specifically written for the Vision-Bilgegoz project by Ahmet Akif Kaya
# and all rights of this program is owned by Ahmet Akif Kaya under MIT open source license. 
# You are automatically accepting the terms of the MIT license by using this code in any way.
# The terms and conditions about this project's MIT license can be found the the file named
# "LICENSE" in the root directory of this repository.

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
