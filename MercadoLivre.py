import pyautogui
from time import sleep
import pyperclip
for i in range(1):
    #copiar titulo anuncio 1
    pyautogui.moveTo(2385,356, duration=1)
    pyautogui.leftClick(duration=0.5)
    #coletando preço
    for i in range(1):
        pyautogui.moveTo(2693,194, duration=1)
        pyautogui.tripleClick(duration=0.5)
        pyautogui.hotkey('ctrl', 'c')
        pyautogui.moveTo(2470,6)
        pyautogui.leftClick(duration=0.5)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('arrowd')
        sleep(10)
    #coletando nome
    for i in range(1):
        pyautogui.moveTo(2280,13, duration=1)
        pyautogui.leftClick(duration=0.5)
        pyautogui.moveTo(2668,263, duration=1)
        pyautogui.tripleClick(duration=1)
        pyautogui.hotkey('ctrl', 'c')
        pyautogui.moveTo(2514,13, duration=1)
        pyautogui.leftClick(duration=0.5)
        pyautogui.moveTo(2348,427, duration=1)
        pyautogui.leftClick(duration=0.5)
        pyautogui.hotkey('ctrl', 'v')
    #coletando link
    for i in range(1):
        pyautogui.moveTo(2284,15, duration=1)
        pyautogui.leftClick(duration=0.5)
        pyautogui.moveTo(2510,47, duration=1)
        pyautogui.leftClick(duration=0.5)
        pyautogui.hotkey('ctrl', 'c')
        pyautogui.moveTo(2486,9, duration=1)
        pyautogui.leftClick(duration=0.5)
        pyautogui.moveTo(2472,436, duration=1)
        pyautogui.leftClick(duration=0.5)
        pyautogui.hotkey('ctrl', 'v')
    #fechando aba
    for i in range(1):
        pyautogui.moveTo(2374,12, duration= 1)
        pyautogui.leftClick(duration=0.5)
        pyautogui.moveTo(2093,5, duration= 1)
        pyautogui.leftClick(duration=0.5)
    
