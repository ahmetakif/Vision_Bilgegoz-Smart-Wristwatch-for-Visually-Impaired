######## USB Camera Object Detection Using Tensorflow Classifier for VISION-Bilgegoz #########
#
# Author: Ahmet Akif Kaya
# Date: 2/10/19
# Description:
# This program uses a TensorFlow classifier to perform object detection.
# For detecting the objects in the frame of the camera to be said vocally to the blind user.
# It loads the classifier uses it to perform object detection on a USB Camera feed.
# It draws boxes and scores around the objects of interest in each frame from
# the USB Camera. It also can be used with a Picamera.

## Some of the code is copied from EjdeElectronics Tensorflow on Raspiberry Pi Library at
## https://github.com/EdjeElectronics/TensorFlow-Object-Detection-on-the-Raspberry-Pi

## and some of the code is copied from Google's example at
## https://github.com/tensorflow/models/blob/master/research/object_detection/object_detection_tutorial.ipynb

## and some is copied from Dat Tran's example at
## https://github.com/datitran/object_detector_app/blob/master/object_detection_app.py

# This code is specifically written for the Vision-Bilgegoz project by Ahmet Akif Kaya
# and all rights of this program is owned by Ahmet Akif Kaya under APACHE open source license. 
# You are automatically accepting the terms of the APACHE license by using this code in any way.
# The terms and conditions about this project's APACHE license can be found in the file named
# "LICENSE" in the root directory of this repository.

# Copyright 2020 Ahmet Akif Kaya
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. 
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an 
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific 
# language governing permissions and limitations under the License.

# Import packages
import os
import cv2
import numpy as np
from picamera.array import PiRGBArray
from picamera import PiCamera
import tensorflow as tf
import argparse
import sys

# ADDITIONS FOR LANGUAGE SELECTION FROM EN/DE/TR/FR
lang = "tr"

# ADDITIONS FOR THE BLINDSOFT-OBJECT BY AHMET AKIF KAYA
from BLINDSOFT_TRANSFUSION import classtransfer

# ADDITIONS FOR THE BLINDSOFT-OCR BY AHMET AKIF KAYA
import subprocess
import shlex
from BLINDSOFT_TRANSFUSION import ocrread

# ADDITIONS FOR THE BLINDSOFT-MODESWITCH BY AHMET AKIF KAYA
modesw = 0
swpin = 5
import RPi.GPIO as gpio
def gpiosetup():
    gpio.setmode(gpio.BCM)
    gpio.setwarnings(False)
    gpio.setup(swpin,gpio.IN)
gpiosetup()

# Set up camera constants
#IM_WIDTH = 1280
#IM_HEIGHT = 720
IM_WIDTH = 640    #Use smaller resolution for
IM_HEIGHT = 480   #slightly faster framerate

# Select camera type (if user enters --picamera when calling this script,
# picamera will be used)
camera_type = 'usb'
parser = argparse.ArgumentParser()
parser.add_argument('--picamera', help='Use picamera instead of a USB webcam',
                    action='store_true')
args = parser.parse_args()
if args.picamera:
    camera_type = 'picamera'

# This is needed since the working directory is the object_detection folder.
sys.path.append('..')

# Import utilites
from utils import label_map_util
from utils import visualization_utils as vis_util

# Name of the directory containing the object detection module we're using
MODEL_NAME = 'ssdlite_mobilenet_v2_coco_2018_05_09'

# Grab path to current working directory
CWD_PATH = os.getcwd()

# Path to frozen detection graph .pb file, which contains the model that is used
# for object detection.
PATH_TO_CKPT = os.path.join(CWD_PATH,MODEL_NAME,'frozen_inference_graph.pb')

# Path to label map file
PATH_TO_LABELS = os.path.join(CWD_PATH,'data','mscoco_label_map.pbtxt')

# Number of classes the object detector can identify
NUM_CLASSES = 90

## Load the label map.
# Label maps map indices to category names, so that when the convolution
# network predicts `5`, we know that this corresponds to `airplane`.
# Here we use internal utility functions, but anything that returns a
# dictionary mapping integers to appropriate string labels would be fine
label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
category_index = label_map_util.create_category_index(categories)

# Load the Tensorflow model into memory.
detection_graph = tf.Graph()
with detection_graph.as_default():
    od_graph_def = tf.GraphDef()
    with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
        serialized_graph = fid.read()
        od_graph_def.ParseFromString(serialized_graph)
        tf.import_graph_def(od_graph_def, name='')

    sess = tf.Session(graph=detection_graph)


# Define input and output tensors (i.e. data) for the object detection classifier

# Input tensor is the image
image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')

# Output tensors are the detection boxes, scores, and classes
# Each box represents a part of the image where a particular object was detected
detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')

# Each score represents level of confidence for each of the objects.
# The score is shown on the result image, together with the class label.
detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')

# Number of objects detected
num_detections = detection_graph.get_tensor_by_name('num_detections:0')

# Initialize frame rate calculation
frame_rate_calc = 1
freq = cv2.getTickFrequency()
font = cv2.FONT_HERSHEY_SIMPLEX

# Initialize camera and perform object detection.
# The camera has to be set up and used differently depending on if it's a
# Picamera or USB webcam.

# I know this is ugly, but I basically copy+pasted the code for the object
# detection loop twice, and made one work for Picamera and the other work
# for USB.

def objectdetection():
    gpiosetup()
    ### Picamera ###
    if camera_type == 'picamera':
        # Initialize Picamera and grab reference to the raw capture
        camera = PiCamera()
        camera.resolution = (IM_WIDTH,IM_HEIGHT)
        camera.framerate = 10
        rawCapture = PiRGBArray(camera, size=(IM_WIDTH,IM_HEIGHT))
        rawCapture.truncate(0)

        for frame1 in camera.capture_continuous(rawCapture, format="bgr",use_video_port=True):

            t1 = cv2.getTickCount()

            # Acquire frame and expand frame dimensions to have shape: [1, None, None, 3]
            # i.e. a single-column array, where each item in the column has the pixel RGB value
            frame = frame1.array
            frame.setflags(write=1)
            frame_expanded = np.expand_dims(frame, axis=0)

            # Perform the actual detection by running the model with the image as input
            (boxes, scores, classes, num) = sess.run(
                [detection_boxes, detection_scores, detection_classes, num_detections],
                feed_dict={image_tensor: frame_expanded})

            # Draw the results of the detection (aka 'visulaize the results')
            vis_util.visualize_boxes_and_labels_on_image_array(
                frame,
                np.squeeze(boxes),
                np.squeeze(classes).astype(np.int32),
                np.squeeze(scores),
                category_index,
                use_normalized_coordinates=True,
                line_thickness=8,
                min_score_thresh=0.40)

            classtransfer(classes,boxes,IM_WIDTH,IM_HEIGHT,lang)
            #cv2.putText(frame,"FPS: {0:.2f}".format(frame_rate_calc),(30,50),font,1,(255,255,0),2,cv2.LINE_AA)

            # All the results have been drawn on the frame, so it's time to display it.
            #cv2.imshow('Object detector', frame)

            t2 = cv2.getTickCount()
            time1 = (t2-t1)/freq
            frame_rate_calc = 1/time1

            # Press 'q' to quit
            if cv2.waitKey(1) == ord('q'):
                break

            rawCapture.truncate(0)

        camera.close()

    ### USB webcam ###
    elif camera_type == 'usb':
        # Initialize USB webcam feed
        camera = cv2.VideoCapture(0)
        ret = camera.set(3,IM_WIDTH)
        ret = camera.set(4,IM_HEIGHT)
        os.system("aplay /home/pi/soundeffects/nintendomode.wav $")
        if lang == "tr":
            os.system("aplay /home/pi/soundeffects/speaktr/objectrecognitionmode.wav $")
        elif lang == "en":
            os.system("aplay /home/pi/soundeffects/speaken/objectrecognitionmode.wav $")
        elif lang == "de":
            os.system("aplay /home/pi/soundeffects/speakde/objectrecognitionmode.wav $")
        elif lang == "fr":
            os.system("aplay /home/pi/soundeffects/speakfr/objectrecognitionmode.wav $")
        else:
            print("ERROR: Uknown language, choose another")
        global modesw
        while(modesw == 0):
            modesw = gpio.input(swpin)
            print(modesw)

            t1 = cv2.getTickCount()

            # Acquire frame and expand frame dimensions to have shape: [1, None, None, 3]
            # i.e. a single-column array, where each item in the column has the pixel RGB value
            ret, frame = camera.read()
            frame_expanded = np.expand_dims(frame, axis=0)

            # Perform the actual detection by running the model with the image as input
            (boxes, scores, classes, num) = sess.run(
                [detection_boxes, detection_scores, detection_classes, num_detections],
                feed_dict={image_tensor: frame_expanded})

            # Draw the results of the detection (aka 'visulaize the results')
            vis_util.visualize_boxes_and_labels_on_image_array(
                frame,
                np.squeeze(boxes),
                np.squeeze(classes).astype(np.int32),
                np.squeeze(scores),
                category_index,
                use_normalized_coordinates=True,
                line_thickness=8,
                min_score_thresh=0.85)

            classtransfer(classes,boxes,IM_WIDTH,IM_HEIGHT,lang)
            #cv2.putText(frame,"FPS: {0:.2f}".format(frame_rate_calc),(30,50),font,1,(255,255,0),2,cv2.LINE_AA)

            # All the results have been drawn on the frame, so it's time to display it.
            #cv2.imshow('Object detector', frame)

            t2 = cv2.getTickCount()
            time1 = (t2-t1)/freq
            frame_rate_calc = 1/time1

            # Press 'q' to quit
            if cv2.waitKey(1) == ord('q'):
                break

def ocr():
    os.system("aplay /home/pi/soundeffects/nintendomode.wav $")
    if lang == "tr":
        os.system("aplay /home/pi/soundeffects/speaktr/ocrmode.wav $")
    elif lang == "en":
        os.system("aplay /home/pi/soundeffects/speaken/ocrmode.wav $")
    elif lang == "de":
        os.system("aplay /home/pi/soundeffects/speakde/ocrmode.wav $")
    elif lang == "fr":
        os.system("aplay /home/pi/soundeffects/speakfr/ocrmode.wav $")
    else:
        print("ERROR: Uknown language, choose another")
    gpiosetup()
    global modesw
    while(modesw == 1):
        modesw = gpio.input(swpin)
        print(modesw)
        cam = cv2.VideoCapture(0)
        ret, image = cam.read()
        if ret:
            cv2.imwrite("/home/pi/ocr/images/1.jpg", image)
        cam.release()
        command = shlex.split("tesseract /home/pi/ocr/images/1.jpg stdout")
        process = subprocess.Popen(command, stdout=subprocess.PIPE)
        output, err = process.communicate()
        ocrread(output,lang)

while True:
    modesw = gpio.input(swpin)
    print("Selected Mode:")
    print(modesw)
    if(modesw == 0):
        objectdetection()
    else:
        ocr()


