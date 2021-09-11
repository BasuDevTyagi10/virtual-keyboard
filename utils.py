from cv2 import cv2
import numpy as np
import cvzone

WEB_CAM_INDEX = 1
SELECT_SOUND_FILE = "select.mp3"

specialKeys = [
    ['EXIT','TOG','DEL','BACK','TAB','ENTER'],
    ['ESC','HOME','SPACE']
]

arrowKeys = [
    ['UP'],
    ['LEFT','DOWN','RIGHT']
]

keys1 = [
    ['`','1','2','3','4','5','6','7','8','9','0','-'],
    ['q','w','e','r','t','y','u','i','o','p','[',']'],
    ['a','s','d','f','g','h','j','k','l',';','\'','='],
    ['z','x','c','v','b','n','m',',','.','/','\\']
]

keys2 = [
    ['~','!','@','#','$','%','^','&','*','(',')','_'],
    ['Q','W','E','R','T','Y','U','I','O','P','{','}'],
    ['A','S','D','F','G','H','J','K','L',':','\"','+'],
    ['Z','X','C','V','B','N','M','<','>','?','|'],
]

class Button:
    def __init__(self,position,text,size=[100,80]):
        self.position = position
        self.text = text
        self.size = size

specialKeysButtonList = list()
for i in range(len(specialKeys)):
    for j,key in enumerate(specialKeys[i]):
        if key == 'SPACE':
            specialKeysButtonList.append(Button([110*j+100,90*i+100],key,[430,80]))
        else:
            specialKeysButtonList.append(Button([110*j+100,90*i+100],key))

arrowKeysButtonList = list()
for i in range(len(arrowKeys)):
    for j,key in enumerate(arrowKeys[i]):
        if key == 'UP':
            arrowKeysButtonList.append(Button([780+100*j+100,90*i+100],key,[80,80]))
        else:
            arrowKeysButtonList.append(Button([680+100*j+100,90*i+100],key,[80,80]))

keys1ButtonList = list()
for i in range(len(keys1)):
    for j,key in enumerate(keys1[i]):
        keys1ButtonList.append(Button([90*j+100,180+90*i+100],key,[80,80]))

keys2ButtonList = list()
for i in range(len(keys2)):
    for j,key in enumerate(keys2[i]):
        keys2ButtonList.append(Button([90*j+100,180+90*i+100],key,[80,80]))

def drawKeys(img,buttonList,textScale):
    for button in buttonList:
        x,y = button.position
        w,h = button.size
        cvzone.cornerRect(img,(x,y,w,h),20,rt=0)
        if button.text == 'EXIT':
            cv2.rectangle(img,button.position,(x+w,y+h),(0,0,255),cv2.FILLED)
        else:
            cv2.rectangle(img,button.position,(x+w,y+h),(255,0,0),cv2.FILLED)
        cv2.putText(img, button.text, (x+10, y+70), cv2.FONT_HERSHEY_PLAIN, textScale, (255, 255, 255), 2)
    return img

def drawKeyboard(img,toggle = False):
    imgNew = np.zeros_like(img,np.uint8)
    imgNew = drawKeys(imgNew,specialKeysButtonList,1)
    imgNew = drawKeys(imgNew,arrowKeysButtonList,1)
    imgNew = drawKeys(imgNew,keys2ButtonList,2) if toggle else drawKeys(imgNew,keys1ButtonList,2)

    imgOutput = img.copy()
    alpha = 0
    mask = imgNew.astype(bool)
    imgOutput[mask] = cv2.addWeighted(img, alpha, imgNew, 1 - alpha, 0)[mask]
    return imgOutput