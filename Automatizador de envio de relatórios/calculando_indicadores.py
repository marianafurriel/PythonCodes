import pandas as ps
import numpy as np
import openpyxl as opx

def calcular_indicadores():
    nome_user = 'maria'
    tabela = ps.read_excel(r"C:\Users\maria\Downloads\Vendas - Dez.xlsx")