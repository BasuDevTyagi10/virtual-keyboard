from utils import *
from cvzone.HandTrackingModule import HandDetector
from time import sleep
from pynput.keyboard import Controller, Key
import sys

from pygame import mixer
mixer.init() 
sound=mixer.Sound(SELECT_SOUND_FILE)

videoCapture = cv2.VideoCapture(WEB_CAM_INDEX)
videoCapture.set(3,1280)
videoCapture.set(4,720)

handDetector = HandDetector(detectionCon=0.8,maxHands=2)
keyboardController = Controller()

toggleKeyboard = False

def findIndexFingerPosition(img,listOfAllButtons,textScale):
    for buttonList in listOfAllButtons:
        global toggleKeyboard
        for button in buttonList:
            x,y = button.position
            w,h = button.size

            if x < lmList[8][0] < x+w and y < lmList[8][1] < y+h:
                if button.text == 'EXIT':
                    cv2.rectangle(img, button.position, (x+w,y+h), (0, 0, 175), cv2.FILLED)
                else:
                    cv2.rectangle(img, button.position, (x+w,y+h), (175, 0, 0), cv2.FILLED)
                cv2.putText(img, button.text, (x+10, y+70), cv2.FONT_HERSHEY_PLAIN, textScale, (255, 255, 255), 2)

                length, _ = handDetector.findDistance(lmList[8], lmList[4])  # pylint: disable=unbalanced-tuple-unpacking
                print(length)

                if length<20:
                    cv2.rectangle(img, button.position, (x+w, y+h), (0, 255, 0), cv2.FILLED)
                    cv2.putText(img, button.text, (x+10, y+75), cv2.FONT_HERSHEY_PLAIN, textScale, (0, 0, 0), 2)
                    try:
                        sound.play()
                    except:
                        print("sound error!")
                    
                    keypress = ""
                    specialKeys = {
                        'ESC' : Key.esc,
                        'HOME' : Key.home,
                        'DEL' : Key.delete,
                        'BACK' : Key.backspace,
                        'TAB' : Key.tab,
                        'ENTER' : Key.enter,
                        'SPACE' : Key.space,
                        'UP' : Key.up,
                        'DOWN' : Key.down,
                        'LEFT' : Key.left,
                        'RIGHT' : Key.right
                    }

                    try:
                        if button.text == 'TOG':
                            toggleKeyboard = not toggleKeyboard
                            break
                        elif button.text == 'EXIT':
                            sys.exit(0)
                        else:
                            keypress = specialKeys[button.text]
                    except KeyError:
                        keypress = button.text

                    keyboardController.press(keypress)
                    
                    sleep(0.2) 

try:
    while True:
        success, img = videoCapture.read()
        hands, img = handDetector.findHands(img,flipType=False)
        img = drawKeyboard(img,toggle=toggleKeyboard)

        if hands:
            hand = hands[0]
            lmList = hand['lmList']
            bboxInfo = hand['bbox']

            findIndexFingerPosition(img,[specialKeysButtonList,arrowKeysButtonList],1)

            if not toggleKeyboard:
                findIndexFingerPosition(img,[keys1ButtonList],2)
            else:
                findIndexFingerPosition(img,[keys2ButtonList],2)
        
        cv2.imshow("WebCam {}".format(WEB_CAM_INDEX),img)
        cv2.waitKey(1)

except Exception as e:
    print(e) 