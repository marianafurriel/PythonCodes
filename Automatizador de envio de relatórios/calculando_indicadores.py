import pandas as pd
# import numpy as np
# import openpyxl as opx

def calcular_indicadores(): #queremos o faturamento e a quantidade de produtos vendidos
    tabela = pd.read_excel(r"C:\Users\maria\Downloads\Vendas - Dez.xlsx")
    faturamento = tabela['Valor Final'].sum()
    quantidade = tabela['Quantidade'].sum()
    return faturamento,quantidade