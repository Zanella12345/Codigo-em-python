import pyautogui
from time import sleep
import pyperclip
def escrever_frase(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('ctrl','v')
for i in range(20):
    pyautogui.moveTo(2831,976, duration=0.1)
    pyautogui.leftClick(duration=0.1)
    escrever_frase('fala rapaziada')
    pyautogui.moveTo(3713,984, duration=0.1)
    pyautogui.leftClick(duration=0.1)
