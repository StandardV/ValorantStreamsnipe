import pyautogui
import pytesseract
import time
import keyboard
import requests




custom_oem=r'eng --oem 2 --psm 11 '
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
time.sleep(3)
def Tes():
    im = pyautogui.screenshot(region=( 630 , 567 , 215 , 172 ))
    im.save("D:\Largecodefile\Tesseract\Tesseract.png")
    im = pytesseract.image_to_string(("D:\Largecodefile\Tesseract\Tesseract.png"), config =custom_oem  )
    return str(im)

def checkstat():
    a="https://www.twitch.tv/"
    b = ""
    global mimimi
    mimimi=Tes().replace(" ","").split()
    for i in range (0, len(mimimi)):
        b= "".join([a,mimimi[i]])
        print(b, end= "")
        getstatus(b,mimimi[i])

def spacelen(name):
    s=""
    h=30-len(name)
    for i in range(0,h):
        s=s+y
    return s

def getstatus(b,name):
    URL = b
    contents = requests.get(URL).content.decode('utf-8')
    x=spacelen(name)
    if 'isLiveBroadcast' in contents:
        print(f'{x}Online')
    else:
        print(f'{x}Unavailable')

while True:
    y=(" ")
    mimimi = []
    if keyboard.is_pressed('-'):
        print('Opponent streamer propability:')
        checkstat()
        break


