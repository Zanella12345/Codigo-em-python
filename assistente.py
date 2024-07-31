import pyautogui
from time import sleep
#abrir mouseinfo
import pyperclip 
respAssis = pyautogui.confirm(
    text='O que quer fazer agr?', 
    title='Assistente', 
    buttons=['Jogar', 'PythonProgram', 'cancelar']
)
if respAssis == ('PythonProgram'):
    for i in range(1):
        pyautogui.moveTo(722,1053, duration=1)
        pyautogui.leftClick(duration=0.5)
        pyautogui.typewrite('cmd')
        pyautogui.moveTo(1040,565, duration=1)
        pyautogui.press('enter')
        sleep(1)
        pyautogui.leftClick(duration=0.5)
        pyautogui.typewrite('python')
        pyautogui.press('enter')
        sleep(2)
        pyautogui.typewrite('from mouseinfo import mouseInfo')
        pyautogui.press('enter')
        sleep(2)
        pyautogui.typewrite('mouseInfo()')
        pyautogui.press('enter')
        pyautogui.hotkey('win', 'd')
        sleep(1)
        pyautogui.press('win')
        sleep(2)
        pyautogui.typewrite('opera')
        sleep(1)
        pyautogui.press('enter')
    #abrir spotfy
    for i in range(1):
        pyautogui.moveTo(722,1053, duration=1)
        pyautogui.leftClick(duration=0.5)
        pyautogui.typewrite('spotify')
        pyautogui.moveTo(1040,565, duration=1)
        pyautogui.press('enter')
        sleep(2)
        pyautogui.moveTo(2237,387, duration=1)
        pyautogui.leftClick(duration=0.5)
        pyautogui.moveTo(2318,407, duration=1)
        pyautogui.leftClick(duration=0.5)
        pyautogui.moveTo(2893,95, duration=1)
        pyautogui.leftClick(duration=0.5)
        #abri o planilhas
        for i in range(1):
            pyautogui.moveTo(3600,0, duration=1)
            pyautogui.leftClick(duration=0.5)
            pyautogui.hotkey('ctrl', 't')
            pyautogui.leftClick(duration=0.5)
            pyautogui.moveTo(2677,149, duration=1)
            pyautogui.typewrite('drive')
            pyautogui.press('enter')
            pyautogui.moveTo(3743,127, duration=1)
            pyautogui.leftClick(duration=0.5)
            pyautogui.moveTo(3520, 496, duration=1)
            pyautogui.leftClick(duration=0.5)
            sleep(3)
            pyautogui.moveTo(2543,323, duration=1)
            pyautogui.leftClick(duration=0.5)
            pyautogui.typewrite('trabalho')
            pyautogui.press('enter')
            pyautogui.moveTo(2337,381, duration=0.5)
            sleep(4)
            pyautogui.leftClick(duration=0.5)
            sleep(2)
            pyautogui.tripleClick(duration=1)
            sleep(3)
        #cria um nova linha
        for i in range(1):
            for i in range(2):
                pyautogui.moveTo(1997,380, duration=1)
                sleep(2)
                pyautogui.rightClick(duration=0.5)
                sleep(2)
                pyautogui.moveTo(2100,431, duration=1)
                sleep(2)
                pyautogui.leftClick(duration=0.5)
                sleep(1)
            for i in range(1):
                pyautogui.moveTo(2063,366, duration=1)
                pyautogui.leftClick(duration=0.5)
                pyautogui.typewrite('1')
                pyautogui.press('tab')
                pyautogui.hotkey('ctrl', 't')
                sleep(2)
                pyautogui.typewrite('Que horas sao?')
                sleep(3)
                pyautogui.press('enter')
                sleep(3)
                pyautogui.press('f5')
                sleep(2)
                pyautogui.moveTo(2235,244, duration=1)
                sleep(1)
                pyautogui.tripleClick(duration=1)
                pyautogui.hotkey('ctrl', 'c')
                pyautogui.hotkey('ctrl', 'w')
                pyautogui.hotkey('ctrl', 'v')
                pyautogui.press('tab')
                pyautogui.hotkey('ctrl', 't')
                pyautogui.typewrite('Que dia e hoje?')
                pyautogui.press('enter')
                pyautogui.moveTo(2257,295, duration=1)
                sleep(2)
                pyautogui.tripleClick(duration=1)
                pyautogui.hotkey('ctrl', 'c')
                pyautogui.hotkey('ctrl', 'w')
                pyautogui.moveTo(2321,358, duration=1)
                pyautogui.leftClick(duration=0.5)
                pyautogui.hotkey('ctrl', 'v')
                #formatação das letras
            for i in range(1):
                pyautogui.moveTo(1997,296, duration=1)
                pyautogui.leftClick(duration=0.5)
                pyautogui.moveTo(2836,195, duration=1)
                pyautogui.leftClick(duration=0.5)
                pyautogui.typewrite('10')
                pyautogui.press('enter')
                pyautogui.moveTo(3084,194, duration=1)
                pyautogui.leftClick(duration=0.5)
                pyautogui.moveTo(3085,301, duration=1)
                pyautogui.leftClick(duration=1)
                pyautogui.moveTo(3139,191, duration=0.5)
                pyautogui.leftClick(duration=0.5)
                pyautogui.moveTo(3444,302, duration=0.5)
                pyautogui.leftClick(duration=0.5)
                pyautogui.moveTo(2082,334, duration=1)
                pyautogui.leftClick(duration=0.5)
    
elif respAssis == ('Jogar'):
    respJogo = pyautogui.confirm(text = 'Escolha o jogo',title = 'assistente', buttons=['Banana', 'csgo', 'outros', 'cancelar'])
    if respJogo == 'Banana':
        #entrando na steam
        pyautogui.hotkey('win', 'd')
        sleep(1)
        pyautogui.press('win')
        sleep(1)
        pyautogui.typewrite('steam')
        sleep(3)
        pyautogui.press('enter')
        sleep(10)
        #escolhendo o jogo da banana
        pyautogui.moveTo(191,44, duration=1)
        pyautogui.leftClick(duration=0.5)
        sleep(1)
        pyautogui.moveTo(94,271, duration=1)
        pyautogui.leftClick(duration=0.5)
        sleep(1)
        pyautogui.moveTo(358,427, duration=1)
        pyautogui.leftClick(duration=0.5)
        respNumeroCliques = pyautogui.confirm(text = 'Escolha o numero de cliques', title = 'assistente', buttons=['100','1000','10000', '1000000'])
        pyautogui.moveTo(313,377, duration=0.5)
        if respNumeroCliques == '100':
            for i in range(100):
                pyautogui.click(clicks=1,interval=0.06,button='left')
        elif respNumeroCliques == '1000':
            for i in range(1000):
                pyautogui.click(clicks=1,interval=0.06,button='left')
        elif respNumeroCliques == '10000':
            for i in range(10000):
                pyautogui.click(clicks=1,interval=0.06,button='left')
        else:
            for i in range(1000000):
                pyautogui.click(clicks=1,interval=0.06,button='left')
    elif respJogo == 'csgo':
        pyautogui.alert(text = 'em desemvolvimento')
    elif respJogo == 'outros':
        pyautogui.alert(text = 'em desemvolvimento')
    else: 
        pyautogui.alert(text = 'em desemvolvimento')
else: pyautogui.alert(text= 'cancelado com sucesso')
