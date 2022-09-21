import pyautogui
import pytesseract
import time




me234 = list(pyautogui.locateAllOnScreen('BuxImage.png', confidence = 0.75))

print (me234)
custom_oem=r'eng --oem 1 --psm 11 -c tessedit_char_whitelist=0123456789kM.'
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
time.sleep(3)
def getmin1():
    im = pyautogui.screenshot(region=( 1570 , 982 , 231 , 74 ))
    im.save('ValueReading1.png')
    im = pytesseract.image_to_string(("ValueReading1.png"), config =custom_oem  )
    print(im)
    time.sleep(1)
    #os.remove('ValueReading1.png')
def getgas1():
    im = pyautogui.screenshot(region=( 5 , 404 , 76 , 30 )) # region=( 4 , 408 , 77 , 21 )) region=( 6 , 405 , 73 , 28 )
    im.save('ValueReading2.png')
    im = pytesseract.image_to_string(("ValueReading2.png"), config =custom_oem )
    print(im)
    #os.remove('ValueReading2.png')

getmin1()
getgas1()
region=( 1673 , 352 , 133 , 69 )
                                           #x value is 1737 y value is 392  (ALL FIRST BOX VALUE)
 