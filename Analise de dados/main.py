import pandas as pd

#importando a base de dados
tabela = pd.read_csv('telecom_users.csv') 

#retirando colunas desnecessarias
tabela = tabela.drop('Unnamed: 0', axis = 1) #se axis == 0 -> linha, se axis == 1 -> coluna

#analisando tipos de dados e se temos valores nulos
print(tabela.info())

#consertar colunas reconhecidas como tipo errado
tabela['TotalGasto'] = pd.to_numeric(tabela['TotalGasto'],errors="coerce") #coluna TotalGasto está como texto mas queremos como números #errors="coerce" força o texto a virar número, onde for texto mesmo (não for numero) vai ficar vazio
print(tabela.info()) #checando se a conversao funcionou

tabela = tabela.dropna(how="all",axis= 1) #excluindo colunas que tem todos os valores vazios #dropna exclui o que é vazio de acordo com o axis #how=all -> todos os valores vazios 
tabela = tabela.dropna(how="any",axis=0) #excluindo linhas que tem algum valor vazio #how=any -> pelo menos um valor vazio
print(tabela.info()) #checando se as exclusoes funcionaram
