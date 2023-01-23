import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
from sklearn.model_selection import train_test_split

tabela = pd.read_csv('advertising.csv')

sns.heatmap(tabela.corr(),cmap='Greens',annot=True) #cria o gráfico
plt.show() #exibe o gráfico

y = tabela["Vendas"]
x = tabela[["TV",'Radio','Jornal']]

x_treino,x_teste,y_treino,y_teste = train_test_split(x,y) #separa nossa base de dados em dados de treino e dados de teste

