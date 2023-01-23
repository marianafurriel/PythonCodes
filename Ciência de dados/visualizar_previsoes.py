import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

def visualizar_previsoes(y_teste, previsao_arvoredecisao, previsao_regressaolinear):
    #gera a tabela com y de teste e as previsoes
    tabela_auxiliar = pd.DataFrame()
    tabela_auxiliar["y_teste"] = y_teste
    tabela_auxiliar["Previsao Arvore Decisao"] = previsao_arvoredecisao
    tabela_auxiliar["Previsao RegressaoLinear"] = previsao_regressaolinear
    sns.lineplot(data=tabela_auxiliar) #gera o grafico
    plt.show() #exibe o grafico