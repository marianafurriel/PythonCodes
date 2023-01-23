import importa_base as ib
import inteligencia_artificial as ia
import visualizar_previsoes as vp
import previsao as pr
import pandas as pd

def main():
    tabela = ib.importa_base()
    nova_tabela = pd.read_csv("novos.csv")
    modelo = ia.inteligencia_artificial(tabela)
    previsao = modelo.predict(nova_tabela)
    print(previsao)
    
if __name__ == '__main__':
   main()