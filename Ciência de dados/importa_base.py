import pandas as pd


def importa_base():
    tabela = pd.read_csv('advertising.csv') #importar base de dados
    return tabela