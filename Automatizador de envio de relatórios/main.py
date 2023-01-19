import download_da_planilha as ddp
import calculando_indicadores as ci

def main():
   ddp.download() #faz o download da planilha
   ci.calcular_indicadores()

if __name__ == '__main__':
    main()