import pyautogui as pag
import time
import pyperclip
import pandas as pd

pag.PAUSE = 1
pag.press('win')
pag.write('opera')
pag.press('enter')
pag.write("https://drive.google.com/drive/folders/14oLE59U1RqyRqlBbKpsyymW-mitvbtoh")
pag.press('enter')
#time.sleep(5)
pag.doubleClick(x=-1433, y=356)
