######## VISION-Bilgegoz Soundeffects Python Script #########
#
# Author: Ahmet Akif Kaya
# Date: 2/15/19
# Description:
# This program uses aplay function to play various souneffects of the device on boot.
# The audio files are for explaining the device to the blind user.

# This code is specifically written for the Vision-Bilgegoz project by Ahmet Akif Kaya
# and all rights of this program is owned by Ahmet Akif Kaya under MIT open source license. 
# You are automatically accepting the terms of the MIT license by using this code in any way.
# The terms and conditions about this project's MIT license can be found in the file named
# "LICENSE" in the root directory of this repository.

import os

lang = "tr"

os.system("aplay /home/pi/soundeffects/bootsilent.wav $")

if lang == "tr":
    os.system("aplay /home/pi/soundeffects/speaktr/boot1.wav $")
    os.system("aplay /home/pi/soundeffects/speaktr/boot2.wav $")
    os.system("aplay /home/pi/soundeffects/speaktr/boot3.wav $")
elif  lang == "en":
    os.system("aplay /home/pi/soundeffects/speaken/boot1.wav $")
    os.system("aplay /home/pi/soundeffects/speaken/boot2.wav $")
    os.system("aplay /home/pi/soundeffects/speaken/boot3.wav $")
elif lang == "de":
    os.system("aplay /home/pi/soundeffects/speakde/boot1.wav $")
    os.system("aplay /home/pi/soundeffects/speakde/boot2.wav $")
    os.system("aplay /home/pi/soundeffects/speakde/boot3.wav $")
elif lang == "fr":
    os.system("aplay /home/pi/soundeffects/speakfr/boot1.wav $")
    os.system("aplay /home/pi/soundeffects/speakfr/boot2.wav $")
    os.system("aplay /home/pi/soundeffects/speakfr/boot3.wav $")
else:
    print("ERROR: Unknown language, chose another")

