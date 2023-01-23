import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
from sklearn.model_selection import train_test_split 
#importar a inteligencia artificial
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

tabela = pd.read_csv('advertising.csv') #importar base de dados

sns.heatmap(tabela.corr(),cmap='Greens',annot=True) #cria o gráfico
plt.show() #exibe o gráfico

y = tabela["Vendas"]
x = tabela[["TV",'Radio','Jornal']]

x_treino,x_teste,y_treino,y_teste = train_test_split(x,y,test_size=0.3) #separa nossa base de dados em dados de treino e dados de teste

#criar a inteligencia artificial
modelo_regressaolinear = LinearRegression()
modelo_arvoredecisao = RandomForestRegressor()

#treinar a inteligencia artificial
modelo_regressaolinear.fit(x_treino,y_treino)
modelo_arvoredecisao.fit(x_treino,y_treino)
