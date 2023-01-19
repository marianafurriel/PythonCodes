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
    pag.click(x=-1428, y=67)
    pyperclip.copy("https://drive.google.com/drive/folders/14oLE59U1RqyRqlBbKpsyymW-mitvbtoh")
    pag.hotkey("ctrl","v")
    pag.press('enter')
    time.sleep(5) #espera a pagina carregar
    pag.click(x=-1298, y=340) #seleciona o documento
    pag.click(x=-258, y=190) #clica nos 3 pontos
    pag.click(x=-554, y=708) #clica em download
    time.sleep(2)
    pag.click(x=-1275, y=60) #clica na barra de endereço do explorador de arquivos
    pag.press('enter')