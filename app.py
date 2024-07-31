print ('ola')
import pyautogui
from time import sleep
for i in range(100):
    pyautogui.moveTo(2532,418, duration=2)
    pyautogui.dragTo(3440,419, duration=5)
    pyautogui.moveTo(3711,959, duration=2)
    pyautogui.leftClick(duration=2)
    pyautogui.moveTo(2764,1051, duration=2)
    pyautogui.leftClick(duration=2) 
