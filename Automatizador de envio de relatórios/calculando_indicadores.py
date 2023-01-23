import pandas as pd

def calcular_indicadores(): #queremos o faturamento e a quantidade de produtos vendidos
    tabela = pd.read_excel(r"C:\Users\maria\Downloads\Vendas - Dez.xlsx")
    faturamento = tabela['Valor Final'].sum()
    quantidade = tabela['Quantidade'].sum()
    return faturamento,quantidade