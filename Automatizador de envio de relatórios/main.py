import download_da_planilha as ddp
import calculando_indicadores as ci
import enviar_email as ee
import time
import pyautogui as pag
def main():
   ddp.download() #faz o download da planilha
   faturamento,quantidade = ci.calcular_indicadores()
   ee.enviar_email(faturamento,quantidade)
   
if __name__ == '__main__':
   main()