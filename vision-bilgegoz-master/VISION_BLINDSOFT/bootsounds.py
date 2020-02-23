######## VISION-Bilgegoz Soundeffects Python Script #########
#
# Author: Ahmet Akif Kaya
# Date: 2/15/19
# Description:
# This program uses aplay function to play various souneffects of the device on boot.
# The audio files are for explaining the device to the blind user.

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

