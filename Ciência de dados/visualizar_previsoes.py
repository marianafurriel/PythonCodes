import pandas as pd

def visualizar_previsoes(y_teste, previsao_arvoredecisao, previsao_regressaolinear):
    tabela_auxiliar = pd.DataFrame()
    tabela_auxiliar["y_teste"] = y_teste
    tabela_auxiliar["Previsao Arvore Decisao"] = previsao_arvoredecisao
    tabela_auxiliar["Previsao RegressaoLinear"] = previsao_regressaolinear