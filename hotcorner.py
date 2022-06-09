from pyautogui import position, press, hold
from os import platform
from time import sleep
import pyautogui
pyautogui.FAILSAFE = False
while True:
    x,y = position()
    sleep(0.01)
    if (x<=0 or x <=2) and (y<=0 or y<=2):
        if platform == 'Linux':
            press('win')
         else:
            with hold('win'):
                press('tab')
        sleep(1)
