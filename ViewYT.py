from selenium import webdriver
from time import sleep
import pyautogui
import os

logo = r"""
    ___ ___ ___ _______ ___ ___      ___ ___ _______ 
   |   Y   |   |   _   |   Y   |    |   Y   |       |
   |.  |   |.  |.  1___|.  |   |    |   1   |.|   | |
   |.  |   |.  |.  __)_|. / \  |_____\_   _/`-|.  |-'
   |:  1   |:  |:  1   |:      |______|:  |   |:  |  
    \:.. ./|::.|::.. . |::.|:. |      |::.|   |::.|  
     `---' `---`-------`--- ---'      `---'   `---'  
               -> @Created BY: hypn0thcy <-         
                          #AoGiri
"""

try:
    print(logo)
    print('Para Usar Lembre-Se: Ter o geckodriver.exe na pasta do script;')
    print('\n Ter Baixo as Bibliotecas:')
    print("    pyautogui")
    print("     selenium")
    print("      CASO NÃO TENHA NENHUMA, ESCREVA: (ajuda)!")
    escolha = str(input("\nDeseja Continuar? (APERTE ENTER) (OU DIGITE 'ajuda') -> "))

    if escolha == 'ajuda':
        os.system('cls')
        print(logo)
        print("\nPara Instalar As bibliotecas Abra o CMD e digite:\n pip install pyautogui\n  pip install selenium")
        exit()
    elif escolha == '':
        os.system('cls')    
        print(logo)
        url = str(input("Qual o Video? (URL) -> ")).strip()
        tempo = int(input("\nA cada Quanto Tempo o Refresh? (ABRIR E FECHAR O VIDEO) -> "))
        try:
            while True:
                os.system('cls')
                os.system('color 0a')
                print(logo)
                print(f'Alvo -> {url}')
                print(f'Tempo De Refresh -> {tempo}')
                print("\n  [!] INICIANDO! ...")
                browser = webdriver.Firefox()
                browser.get(url)
                browser.maximize_window()
                sleep(1.5)
                pyautogui.press('k')
                sleep(tempo)
                browser.quit()
        except KeyboardInterrupt:
            ("\n        Até Mais!")
        except Exception as u:
            os.system('color 4')
            print("\nHouve Algum erro Critico -> {}".format(u))
    else:
        print('\n        Por Favor Apenas (ENTER) ou (ajuda) !')
        exit()
except KeyboardInterrupt:
    print('\n        Até Mais!')
except Exception as o:
    os.system('cls')
    os.system('color 4')
    print(logo)
    print("\nHouve Algum erro Critico -> {}".format(o))
    exit()
