from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

#importar a inteligencia artificial
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

def inteligencia_artificial(tabela):
    y = tabela["Vendas"]
    x = tabela[["TV",'Radio','Jornal']] #ou x = tabela.drop("Vendas")

    x_treino,x_teste,y_treino,y_teste = train_test_split(x,y,test_size=0.3) #separa nossa base de dados em dados de treino e dados de teste

    #criar a inteligencia artificial
    modelo_regressaolinear = LinearRegression()
    modelo_arvoredecisao = RandomForestRegressor()

    #treinar a inteligencia artificial
    modelo_regressaolinear.fit(x_treino,y_treino)
    modelo_arvoredecisao.fit(x_treino,y_treino)

    previsao_regressaolinear = modelo_regressaolinear.predict(x_teste)
    previsao_arvoredecisao = modelo_arvoredecisao.predict(x_teste)
    # print("regressao linear:" ,r2_score(y_teste,previsao_regressaolinear))
    # print("arvore de decisao:",r2_score(y_teste,previsao_arvoredecisao))
    return modelo_arvoredecisao