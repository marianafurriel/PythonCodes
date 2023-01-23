import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

def importa_base():
    tabela = pd.read_csv('advertising.csv') #importar base de dados

    sns.heatmap(tabela.corr(),cmap='Greens',annot=True) #cria o gráfico
    plt.show() #exibe o gráfico
    return tabela