import pyautogui as pag
import time
import pyperclip

# time.sleep(5)
# print(pag.position())

pag.PAUSE = 1
def download():
    pag.press('win') #abre o menu windows
    pag.write('opera') #procura o navegador
    pag.press('enter') #abre o navegador
    #pag.click(x=-1428, y=67)
    pag.hotkey('ctrl','e')
    pyperclip.copy("https://drive.google.com/drive/u/1/folders/14jtkjefPVFcWH9IT0SkvYo-oy5TNMT3c")
    pag.hotkey("ctrl","v")
    pag.press('enter')
    time.sleep(5) #espera a pagina carregar
    pag.click(x=-1298, y=340) #seleciona o documento
    pag.click(x=-255, y=191) #clica nos 3 pontos
    pag.click(x=-428, y=660) #clica em download
    time.sleep(2)
    pag.press('enter')