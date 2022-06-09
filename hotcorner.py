from pyautogui import position, press
from time import sleep
import pyautogui
pyautogui.FAILSAFE = False
while True:
    x,y = position()
    sleep(0.01)
    if (x<=0 or x <=2) and (y<=0 or y<=2):
        press('win')
        sleep(1)
