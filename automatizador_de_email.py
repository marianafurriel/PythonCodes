import pyautogui as pag
import time
import pyperclip

# time.sleep(5)
# print(pag.position())

pag.PAUSE = 1
pag.press('win') #abre o menu windows
pag.write('opera') #procura o navegador
pag.press('enter') #abre o navegador
pyperclip.copy("https://drive.google.com/drive/folders/14oLE59U1RqyRqlBbKpsyymW-mitvbtoh")
pag.hotkey("ctrl","v")
pag.press('enter')
time.sleep(5) #espera a pagina carregar
pag.click(x=-1298, y=340) #seleciona o documento
pag.click(x=-256, y=241) #clica nos 3 pontos
pag.click(x=-498, y=786) #clica em download
time.sleep(2)
pag.click(x=-1266, y=69) #clica na barra de endereço do explorador de arquivos
pag.hotkey('ctrl','c') #copia o endereço onde vai salvar o arquivo
pag.press('enter')
pag.press('enter')
caminho = pyperclip.paste()
print(caminho)