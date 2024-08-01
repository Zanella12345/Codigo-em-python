import pyautogui
from time import sleep
import pyperclip
import time
#copiar nome
numeroClientes = 55
#não mexa em NADA apartir daqui
import webbrowser
respPlanilha = pyautogui.confirm(title = 'RoboZanella', text = 'Iniciar automação', buttons=['sim', 'não'])
if respPlanilha == 'sim':
    pyautogui.alert(text = 'abra uma aba vazia do opera no segundo monitor')
    webbrowser.open_new('https://docs.google.com/spreadsheets/d/1tYRE7QEmxyqR_kWvRlXQUHpyFC7XxicyKIzlQUpxMW0/edit?gid=0#gid=0')
    webbrowser.open('https://docs.google.com/spreadsheets/d/1tYRE7QEmxyqR_kWvRlXQUHpyFC7XxicyKIzlQUpxMW0/edit?gid=956754206#gid=956754206')
    sleep(8)
    pyautogui.moveTo(2364,1002, duration=1)
    pyautogui.leftClick(duration=0.5)
    pyautogui.moveTo(2090,9, duration=1)
    pyautogui.leftClick(duration=0.5)
    pyautogui.moveTo(2214,1003, duration=1)
    pyautogui.leftClick(duration=0.5)
    sleep(3)
    respColeta1 = pyautogui.confirm(title = 'RoboZanella', text = 'Menu', buttons=['Coleta1', 'Coleta2', 'TodasColetas', 'cancelar'])
    if respColeta1 == 'Coleta1':
        for i in range(1):
            webbrowser.open('https://docs.google.com/spreadsheets/u/0/')
            pyautogui.moveTo(2329,344, duration=1)
            pyautogui.leftClick(duration=0.5)
            pyautogui.moveTo(2283,13, duration=1)
            pyautogui.leftClick(duration=0.5)
            sleep(10)
            pyautogui.alert(text = 'iniciando a tranferencia de dados')
            for i in range(numeroClientes):
                for i in range(1):
                    pyautogui.moveTo(3356,368, duration=1)
                    pyautogui.leftClick(duration=0.5)
                    pyautogui.hotkey('ctrl', 'c')
                for i in range(1):
                    def coletarNome() :
                        return pyperclip.paste()
                    nomeInteiro = coletarNome()
                #tirar nome do meio
                for i in range(1):
                    def removerNomedomeio(nome):
                        partes = nome.split()
                        if len(partes) == 3:
                            return f"{partes[0], partes[2]}"
                        elif len(partes) == 4:
                            return f"{partes[0], partes[3]}"
                        elif len(partes) == 5:
                            return f"{partes[0], partes[4]}"
                        elif len(partes) == 6:
                            return f"{partes[0], partes[5]}"
                        elif len(partes) == 7:
                            return f"{partes[0], partes[6]}"
                        elif len(partes) == 8:
                            return f"{partes[0], partes[7]}"
                        elif len(partes) == 9:
                            return f"{partes[0], partes[8]}"
                        else: return nomeInteiro
                    nome = nomeInteiro
                    nomeDividido = removerNomedomeio(nome)
                    nomeFinal = ''.join(nomeDividido)
                for i in range(1):
                    pyautogui.moveTo(2470,11, duration=1)
                    pyautogui.leftClick(duration=0.5)
                    pyautogui.moveTo(2099,332, duration=1)
                    pyautogui.leftClick(duration=0.5)
                    pyautogui.typewrite(nomeFinal)
                    pyautogui.moveTo(2406,327, duration=1)
                    pyautogui.leftClick(duration=0.5)
                    pyautogui.typewrite(r'=REGEXREPLACE(A1; "[\(\)\'\,]" ; "")')
                    sleep(1)
                    pyautogui.moveTo(3105,334, duration=0.5)
                    pyautogui.leftClick(duration=0.5)
                #adicionar valores
                for i in range(1):
                    pyautogui.moveTo(2305,9, duration=1)
                    pyautogui.leftClick(duration=0.5)
                    pyautogui.moveTo(3518,365, duration=1)
                    pyautogui.leftClick(duration=0.5)
                    pyautogui.hotkey('ctrl', 'c')
                    pyautogui.moveTo(2495,6, duration=1)
                    pyautogui.leftClick(duration=0.5)
                    pyautogui.moveTo(2557,333, duration=0.5)
                    pyautogui.leftClick(duration=0.5)
                    pyautogui.hotkey('ctrl', 'v')
                #criar nova linha
                for i in range(1):
                    pyautogui.moveTo(2000,331, duration=1)
                    pyautogui.rightClick(duration=0.5)
                    pyautogui.moveTo(2197,490, duration=1)
                    pyautogui.leftClick(duration=1)
                    pyautogui.moveTo(2289,13, duration=0.5)
                    pyautogui.leftClick(duration=0.5)
                for i in range(1):
                    pyautogui.moveTo(2039,363, duration=0.5)
                    sleep(0.5)
                    pyautogui.rightClick(duration=0.5)
                    pyautogui.moveTo(2365,984, duration=1)
                    sleep(1)
                    pyautogui.moveTo(2595,989, duration=1)
                    pyautogui.moveTo(2656,826, duration=1)
                    pyautogui.leftClick(duration=0.5)
                    #fechar linha
                    pyautogui.moveTo(1978,332, duration=1)
                    pyautogui.leftClick(duration=0.5)
    elif respColeta1 == 'Coleta2': pyautogui.alert(text = 'em desemvolvimento')
    elif respColeta1 == 'TodasColetas': pyautogui.alert(text = 'em desemvolvimento')
    else : pyautogui.alert(text = 'cancelado com sucesso')
else: print('canelado')