import pyautogui as pag
import time
import pyperclip

pag.PAUSE = 1
def enviar_email(faturamento, quantidade):
    # pag.press('win') #abre o menu windows
    # pag.write('opera') #procura o navegador
    # pag.press('enter') #abre o navegador
    # pag.click(x=-1428, y=67)
    pag.hotkey('ctrl','t')
    pag.hotkey('ctrl','e')
    pag.write('gmail.com')
    pag.press('enter')
    time.sleep(5)
    pag.click(x=-1832, y=212) #clica em escrever
    pag.write("testesde389@gmail.com") 
    pag.press('tab',presses=2)
    pyperclip.copy("Relatório de vendas")
    pag.hotkey('ctrl','v')
    pag.press('tab')
    texto = f"""Prezados, bom dia!
O faturamento do último mês foi de: R${faturamento:,.2f}.
A quantidade de produtos vendida foi: {quantidade:,}.
Abraços,
Mariana."""
    pyperclip.copy(texto)
    pag.hotkey('ctrl','v')
    time.sleep(10)
    pag.hotkey('ctrl','enter')
    pag.click(x=-1533, y=953)