######## VISION-Bilgegoz BLINDSOFT_TRANSFUSION #########
#
# Author: Ahmet Akif Kaya
# Date: 2/25/19
# Description:
# This program is the main script of the Vision-Bilgegoz project
# which does almost everything for the device.

# This code is specifically written for the Vision-Bilgegoz project by Ahmet Akif Kaya
# and all rights of this program is owned by Ahmet Akif Kaya under MIT open source license. 
# You are automatically accepting the terms of the MIT license by using this code in any way.
# The terms and conditions about this project's MIT license can be found in the file named
# "LICENSE" in the root directory of this repository.

import os

def classtransfer(classtotransfer,boxtotransfer,width,height,lang):
    object0 = classtotransfer[0]
    object1 = object0[0]
    widthmid = width/2
    heightmid = height/2
    ymin = boxtotransfer[0][0][0]*height
    xmin = boxtotransfer[0][0][1]*width
    ymax = boxtotransfer[0][0][2]*height
    xmax = boxtotransfer[0][0][3]*width
    xmid = (xmin + xmax) / 2
    ymid = (ymin + ymax) / 2
    Xo = 50
    if xmid < widthmid - width / 15:
        if ymid < heightmid - height / 15:
            directionen = "innorthwest"
            directionde = "imnordwesten"
            directiontr = "kuzeybatida"
            directionfr = "nordouest"
        elif ymid > heightmid + height / 15:
            directionen = "insouthwest"
            directionde = "imsudwesten"
            directiontr = "guneybatida"
            directionfr = "danslesudouest"
        else:
            directionen = "inwest"
            directionde = "imwesten"
            directiontr = "batida"
            directionfr = "àl'ouest"
    elif xmid > widthmid + width / 15:
        if ymid < heightmid - height / 15:
            directionen = "innortheast"
            directionde = "imnordosten"
            directiontr = "kuzeydoguda"
            directionfr = "nordest"
        elif ymid > heightmid + height / 15:
            directionen = "insoutheast"
            directionde = "imsudosten"
            directiontr = "guneydoguda"
            directionfr = "danslesudest"
        else:
            directionen = "ineast"
            directionde = "imosten"
            directiontr = "doguda"
            directionfr = "àl'est"
    else:
        if ymid < heightmid - height / 15:
            directionen = "innorth"
            directionde = "imnorden"
            directiontr = "kuzeyde"
            directionfr = "aunord"
        elif ymid > heightmid + height / 15:
            directionen = "insouth"
            directionde = "imsuden"
            directiontr = "guneyde"
            directionfr = "ausud"
        else:
            directionen = "centered"
            directionde = "zentriert"
            directiontr = "ortali"
            directionfr = "centré"
    if object1 == 1:
        objecten = "person"
        objectde = "person"
        objecttr = "insan"
        objectfr = "homme"
        Xo = 50
    elif object1 == 2:
        objecten = "bicycle"
        objectde = "fahrrad"
        objecttr = "bisiklet"
        objectfr = "vélo"
        Xo = 100
    elif object1 == 3:
        objecten = "car"
        objectde = "auto"
        objecttr = "araba"
        objectfr = "voiture"
        Xo = 380
    elif object1 == 4:
        objecten = "motorcycle"
        objectde = "motorrad"
        objecttr = "motorsiklet"
        objectfr = "motos"
        Xo = 150
    elif object1 == 5:
        objecten = "airplane"
        objectde = "flugzeug"
        objecttr = "ucak"
        objectfr = "avion"
        Xo = 2000
    elif object1 == 6:
        objecten = "bus"
        objectde = "bus"
        objecttr = "otobus"
        objectfr = "bus"
        Xo = 500
    elif object1 == 7:
        objecten = "train"
        objectde = "zug"
        objecttr = "tren"
        objectfr = "train"
        Xo = 2500
    elif object1 == 8:
        objecten = "truck"
        objectde = "lkw"
        objecttr = "kamyon"
        objectfr = "camion"
        Xo = 450
    elif object1 == 9:
        objecten = "boat"
        objectde = "boot"
        objecttr = "bot"
        objectfr = "bottes"
        Xo = 400
    elif object1 == 10:
        objecten = "trafficlight"
        objectde = "ampel"
        objecttr = "trafikisigi"
        objectfr = "feudecirculation"
        Xo = 50
    elif object1 == 11:
        objecten = "firehydrant"
        objectde = "feuerhydrant"
        objecttr = "yanginmuslugu"
        objectfr = "bouched'incendie"
        Xo = 40
    elif object1 == 13:
        objecten = "stopsign"
        objectde = "stopsschild"
        objecttr = "durisareti"
        objectfr = "panneaustop"
        Xo = 55
    elif object1 == 14:
        objecten = "parkingmeter"
        objectde = "parkuhr"
        objecttr = "parkmetre"
        objectfr = "parcmètre"
        Xo = 10
    elif object1 == 15:
        objecten = "bench"
        objectde = "bank"
        objecttr = "bank"
        objectfr = "banc"
        Xo = 180
    elif object1 == 16:
        objecten = "bird"
        objectde = "vogel"
        objecttr = "kus"
        objectfr = "oiseau"
        Xo = 15
    elif object1 == 17:
        objecten = "cat"
        objectde = "katze"
        objecttr = "kedi"
        objectfr = "chatte"
        Xo = 25
    elif object1 == 18:
        objecten = "dog"
        objectde = "hund"
        objecttr = "kopek"
        objectfr = "chien"
        Xo = 40
    elif object1 == 19:
        objecten = "horse"
        objectde = "pferd"
        objecttr = "at"
        objectfr = "cheval"
        Xo = 150
    elif object1 == 20:
        objecten = "sheep"
        objectde = "schaf"
        objecttr = "koyun"
        objectfr = "brebis"
        Xo = 100
    elif object1 == 21:
        objecten = "cow"
        objectde = "kuh"
        objecttr = "inek"
        objectfr = "vache"
        Xo = 130
    elif object1 == 22:
        objecten = "elephant"
        objectde = "elefant"
        objecttr = "fil"
        objectfr = "l'éléphant"
        Xo = 450
    elif object1 == 23:
        objecten = "bear"
        objectde = "bar"
        objecttr = "ayi"
        objectfr = "ours"
        Xo = 200
    elif object1 == 24:
        objecten = "zebra"
        objectde = "zebra"
        objecttr = "zebra"
        objectfr = "zébresse"
        Xo = 140
    elif object1 == 25:
        objecten = "giraffe"
        objectde = "giraffe"
        objecttr = "zurafa"
        objectfr = "girafe"
        Xo = 160
    elif object1 == 27:
        objecten = "backpack"
        objectde = "rucksack"
        objecttr = "sirtcantasi"
        objectfr = "sacàdos"
        Xo = 35
    elif object1 == 28:
        objecten = "umbrella"
        objectde = "regenschirm"
        objecttr = "semsiye"
        objectfr = "parapluie"
        Xo = 85
    elif object1 == 31:
        objecten = "handbag"
        objectde = "handtasche"
        objecttr = "elcantasi"
        objectfr = "Sacàmain"
        Xo = 25
    elif object1 == 32:
        objecten = "tie"
        objectde = "krawatte"
        objecttr = "kiravat"
        objectfr = "attacher"
        Xo = 15
    elif object1 == 33:
        objecten = "suitcase"
        objectde = "koffer"
        objecttr = "bavul"
        objectfr = "valise"
        Xo = 95
    elif object1 == 34:
        objecten = "frisbee"
        objectde = "frisbeescheibe"
        objecttr = "frizbi"
        objectfr = "frisbee"
        Xo = 25
    elif object1 == 35:
        objecten = "skis"
        objectde = "ski"
        objecttr = "kayaktahtalari"
        objectfr = "desskis"
        Xo = 75
    elif object1 == 36:
        objecten = "snowboard"
        objectde = "snowboard"
        objecttr = "snowboard"
        objectfr = "snowboard"
        Xo = 65
    elif object1 == 37:
        objecten = "sportsball"
        objectde = "sportball"
        objecttr = "spor topu"
        objectfr = "balledesport"
        Xo = 35
    elif object1 == 38:
        objecten = "kite"
        objectde = "drachen"
        objecttr = "ucurtma"
        objectfr = "cerfvolant"
        Xo = 85
    elif object1 == 39:
        objecten = "baseballbat"
        objectde = "baseballschlager"
        objecttr = "beyzbolsopasi"
        objectfr = "battedebaseball"
        Xo = 12
    elif object1 == 40:
        objecten = "baseballglove"
        objectde = "baseballhandschuh"
        objecttr = "beyzboleldiveni"
        objectfr = "gantdebaseball"
        Xo = 27
    elif object1 == 41:
        objecten = "skateboard"
        objectde = "skateboard"
        objecttr = "kaykay"
        objectfr = "plancheàroulette"
        Xo = 57
    elif object1 == 42:
        objecten = "surfboard"
        objectde = "surfbrett"
        objecttr = "sorftahtasi"
        objectfr = "planchedesurf"
        Xo = 187
    elif object1 == 43:
        objecten = "tennisracket"
        objectde = "tennisschlager"
        objecttr = "tenisraketi"
        objectfr = "raquettedetennis"
        Xo = 25
    elif object1 == 44:
        objecten = "bottle"
        objectde = "flasche"
        objecttr = "sise"
        objectfr = "bouteille"
        Xo = 15
    elif object1 == 46:
        objecten = "wineglass"
        objectde = "weinglas"
        objecttr = "sarapbardagi"
        objectfr = "verredevin"
        Xo = 10
    elif object1 == 47:
        objecten = "cup"
        objectde = "tasse"
        objecttr = "fincan"
        objectfr = "tasse"
        Xo = 10
    elif object1 == 48:
        objecten = "fork"
        objectde = "gabel"
        objecttr = "catal"
        objectfr = "fourchette"
        Xo = 8
    elif object1 == 49:
        objecten = "knife"
        objectde = "messer"
        objecttr = "bicak"
        objectfr = "couteau"
        Xo = 13
    elif object1 == 50:
        objecten = "spoon"
        objectde = "loffel"
        objecttr = "kasik"
        objectfr = "cuillère"
        Xo = 14
    elif object1 == 51:
        objecten = "bowl"
        objectde = "schüssel"
        objecttr = "kase"
        objectfr = "bol"
        Xo = 17
    elif object1 == 52:
        objecten = "banana"
        objectde = "banane"
        objecttr = "muz"
        objectfr = "banane"
        Xo = 20
    elif object1 == 53:
        objecten = "apple"
        objectde = "apfel"
        objecttr = "elma"
        objectfr = "Pomme"
        Xo = 15
    elif object1 == 54:
        objecten = "sandwich"
        objectde = "sandwich"
        objecttr = "sandvic"
        objectfr = "sandwich"
        Xo = 19
    elif object1 == 55:
        objecten = "orange"
        objectde = "orange"
        objecttr = "portakal"
        objectfr = "Orange"
        Xo = 16
    elif object1 == 56:
        objecten = "broccoli"
        objectde = "brokkoli"
        objecttr = "brokoli"
        objectfr = "brocoli"
        Xo = 4
    elif object1 == 57:
        objecten = "carrot"
        objectde = "karotte"
        objecttr = "havuc"
        objectfr = "carotte"
        Xo = 9
    elif object1 == 58:
        objecten = "hotdog"
        objectde = ""
        objecttr = "sosislisandvic"
        objectfr = "hotdog"
        Xo = 14
    elif object1 == 59:
        objecten = "pizza"
        objectde = "pizza"
        objecttr = "pizza"
        objectfr = "pizza"
        Xo = 30
    elif object1 == 60:
        objecten = "donut"
        objectde = "krapfen"
        objecttr = "tatlicorek"
        objectfr = "donut"
        Xo = 15
    elif object1 == 61:
        objecten = "cake"
        objectde = "kuchen"
        objecttr = "kek"
        objectfr = "gâteau"
        Xo = 10
    elif object1 == 62:
        objecten = "chair"
        objectde = "stuhl"
        objecttr = "sandalye"
        objectfr = "chaise"
        Xo = 55
    elif object1 == 63:
        objecten = "couch"
        objectde = "couch"
        objecttr = "kanepe"
        objectfr = "canapé"
        Xo = 200
    elif object1 == 64:
        objecten = "pottedplant"
        objectde = "topfpflanze"
        objecttr = "saksibitkisi"
        objectfr = "planteenpot"
        Xo = 25
    elif object1 == 65:
        objecten = "bed"
        objectde = "bett"
        objecttr = "yatak"
        objectfr = "lit"
        Xo = 220
    elif object1 == 67:
        objecten = "diningtable"
        objectde = "esstisch"
        objecttr = "yemekmasasi"
        objectfr = "tableàmanger"
        Xo = 180
    elif object1 == 70:
        objecten = "toilet"
        objectde = "toilette"
        objecttr = "tuvalet"
        objectfr = "toilette"
        Xo = 70
    elif object1 == 72:
        objecten = "tv"
        objectde = "fernseher"
        objecttr = "televizyon"
        objectfr = "latélé"
        Xo = 110
    elif object1 == 73:
        objecten = "laptop"
        objectde = "laptop"
        objecttr = "laptop"
        objectfr = "portable"
        Xo = 35
    elif object1 == 74:
        objecten = "mouse"
        objectde = "maus"
        objecttr = "fare"
        objectfr = "Souris"
        Xo = 11
    elif object1 == 75:
        objecten = "remote"
        objectde = "fernbedienung"
        objecttr = "kumanda"
        objectfr = "éloigné"
        Xo = 16
    elif object1 == 76:
        objecten = "keyboard"
        objectde = "tastatur"
        objecttr = "klavye"
        objectfr = "clavier"
        Xo = 35
    elif object1 == 77:
        objecten = "cellphone"
        objectde = "handy"
        objecttr = "ceptelefonu"
        objectfr = "téléphoneportable"
        Xo = 10
    elif object1 == 78:
        objecten = "microwave"
        objectde = "mikrowelle"
        objecttr = "mikrodalga"
        objectfr = "fourmicroonde"
        Xo = 40
    elif object1 == 79:
        objecten = "oven"
        objectde = "ofen"
        objecttr = "firin"
        objectfr = "four"
        Xo = 55
    elif object1 == 80:
        objecten = "toaster"
        objectde = "toaster"
        objecttr = "tostmakinesi"
        objectfr = "grillepain"
        Xo = 28
    elif object1 == 81:
        objecten = "sink"
        objectde = "sinken"
        objecttr = "lavabo"
        objectfr = "évier"
        Xo = 53
    elif object1 == 82:
        objecten = "refigerator"
        objectde = "kuhlschrank"
        objecttr = "buzdolabi"
        objectfr = "réfrigérateur"
        Xo = 100
    elif object1 == 84:
        objecten = "book"
        objectde = "buch"
        objecttr = "kitap"
        objectfr = "livre"
        Xo = 20
    elif object1 == 85:
        objecten = "clock"
        objectde = "uhr"
        objecttr = "saat"
        objectfr = "l'horloge"
        Xo = 30
    elif object1 == 86:
        objecten = "vase"
        objectde = "vase"
        objecttr = "vazo"
        objectfr = "vase"
        Xo = 35
    elif object1 == 87:
        objecten = "scissors"
        objectde = "schere"
        objecttr = "makas"
        objectfr = "lesciseaux"
        Xo = 12
    elif object1 == 88:
        objecten = "teddybear"
        objectde = "teddybar"
        objecttr = "oyuncakayi"
        objectfr = "oursenpeluche"
        Xo = 29
    elif object1 == 89:
        objecten = "hairdrier"
        objectde = "haartrockner"
        objecttr = "sackurutmamakinesi"
        objectfr = "sèchecheveux"
        Xo = 26
    elif object1 == 90:
        objecten = "toothbrush"
        objectde = "zahnburste"
        objecttr = "disfircasi"
        objectfr = "brosseàdents"
        Xo = 6
    d = distancetoobject(width, xmax, xmin, Xo, widthmid)
    if d > 9999999 or d < 0.00000001:
        if lang == "en":
            dstr = "unknown"
        elif lang == "de":
            dstr = "unbekannt"
        elif lang == "tr":
            dstr = "bilinmeyen"
        elif lang == "fr":
            dstr = "inconnu"
        else:
            print ("ERROR: Unidentified Language")
    else:
        dstr = str(d)
    if lang == "en":
        print("I see a " + objecten + ".")
        print("In " + dstr + " meters.")
        print("And this " + objecten + ", is " + directionen)
        os.system("espeak -a 200 -ven-us " + "I" + " 2>/dev/null")
        os.system("espeak -a 200 -ven-us " + "see" + " 2>/dev/null")
        os.system("espeak -a 200 -ven-us " + "a" + " 2>/dev/null")
        os.system("espeak -a 200 -ven-us " + objecten + " 2>/dev/null")
        os.system("espeak -a 200 -ven-us " + "In" + " 2>/dev/null")
        os.system("espeak -a 200 -ven-us " + dstr + " 2>/dev/null")
        os.system("espeak -a 200 -ven-us " + "meters," + " 2>/dev/null")
        os.system("espeak -a 200 -ven-us " + "And this" + " 2>/dev/null")
        os.system("espeak -a 200 -ven-us " + objecten + " 2>/dev/null")
        os.system("espeak -a 200 -ven-us " + "is" + " 2>/dev/null")
        os.system("espeak -a 200 -ven-us " + directionen + " 2>/dev/null")
    elif lang == "de":
        print("Ich sehe ein " + objectde + ".")
        print("In " + dstr + " metern.")
        print("Und das " + objectde + ", ist " + directionen)
        os.system("espeak -a 200 -vde " + "Ich" + " 2>/dev/null")
        os.system("espeak -a 200 -vde " + "sehe" + " 2>/dev/null")
        os.system("espeak -a 200 -vde " + "ein" + " 2>/dev/null")
        os.system("espeak -a 200 -vde " + objectde + " 2>/dev/null")
        os.system("espeak -a 200 -vde " + "In" + " 2>/dev/null")
        os.system("espeak -a 200 -vde " + dstr + " 2>/dev/null")
        os.system("espeak -a 200 -vde " + "metern," + " 2>/dev/null")
        os.system("espeak -a 200 -vde " + "Und das" + " 2>/dev/null")
        os.system("espeak -a 200 -vde " + objectde + " 2>/dev/null")
        os.system("espeak -a 200 -vde " + "ist" + " 2>/dev/null")
        os.system("espeak -a 200 -vde " + directionde + " 2>/dev/null")
    elif lang == "tr":
        print(dstr + "metre uzakta")
        print("Bir " + objecttr + " goruyorum.")
        print("Ve bu " + objecttr + ", " + directiontr)
        os.system("espeak -a 200 -vtr " + dstr + " 2>/dev/null")
        os.system("espeak -a 200 -vtr " + "metre" + " 2>/dev/null")
        os.system("espeak -a 200 -vtr " + "uzakta" + " 2>/dev/null")
        os.system("espeak -a 200 -vtr " + "Bir" + " 2>/dev/null")
        os.system("espeak -a 200 -vtr " + objecttr + " 2>/dev/null")
        os.system("espeak -a 200 -vtr " + "görüyorum," + " 2>/dev/null")
        os.system("espeak -a 200 -vtr " + "Ve" + " 2>/dev/null")
        os.system("espeak -a 200 -vtr " + "bu" + " 2>/dev/null")
        os.system("espeak -a 200 -vtr " + objecttr + " 2>/dev/null")
        os.system("espeak -a 200 -vtr " + directiontr + " 2>/dev/null")
    elif lang == "fr":
        print("Je vois")
        print("une" + objectfr)
        print("à" + dstr + "mètres")
        os.system("espeak -a 200 -vfr " + "Je" + " 2>/dev/null")
        os.system("espeak -a 200 -vfr " + "vois" + " 2>/dev/null")
        os.system("espeak -a 200 -vfr " + "une" + " 2>/dev/null")
        os.system("espeak -a 200 -vfr " + objectfr + " 2>/dev/null")
        os.system("espeak -a 200 -vfr " + "à" + " 2>/dev/null")
        os.system("espeak -a 200 -vfr " + dstr + " 2>/dev/null")
        os.system("espeak -a 200 -vfr " + "mètres" + " 2>/dev/null")
    else:
        print ("ERROR: Unidentified Language")
def ocrread(output,lang):
    if lang == "en":
        output = str(output)
        print(output)
        os.system("espeak -a 200 -ven-us " + output + " 2>/dev/null")
    elif lang == "de":
        output = str(output)
        print(output)
        os.system("espeak -a 200 -vde " + output + " 2>/dev/null")
    elif lang == "tr":
        output = str(output)
        print(output)
        os.system("espeak -a 200 -vtr " + output + " 2>/dev/null")
    elif lang == "fr":
        output = str(output)
        print(output)
        os.system("espeak -a 200 -vfr " + output + " 2>/dev/null")
    else:
        print ("ERROR: Unidentified Language")

def distancetoobject(width, xmax, xmin, Xo, widthmid):
    # Vision object distance measurement
    Wx = (xmax + xmin)/2
    Wo = abs(xmax - xmin)
    Wa = width
    tanof39 = 0.809
    Xa = (Wa*Xo)/Wo
    W1 = abs(Wx - widthmid)
    X1 = (W1*Xo)/Wo
    d = Xa*0.5*tanof39
    dosquare = d**2 + X1**2
    do = dosquare**0.5
    dinmeters = do/100
    dinmeters = round(dinmeters, 2)
    return dinmeters

