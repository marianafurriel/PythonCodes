import pandas as pd

def atualiza_tabela(cotacao_dolar,cotacao_euro,cotacao_ouro):
    tabela = pd.read_excel('Produtos.xlsx')    
    print(tabela)
    #atualiza cotacoes
    tabela.loc[tabela['Moeda'] == "Dólar",'Cotação'] = float(cotacao_dolar)
    tabela.loc[tabela['Moeda'] == "Euro",'Cotação'] = float(cotacao_euro)
    tabela.loc[tabela['Moeda'] == "Ouro",'Cotação'] = float(cotacao_ouro)
    
    #atualiza preços
    tabela["Preço de Compra"] = tabela["Cotação"] * tabela["Preço Original"]
    tabela["Preço de Venda"] = tabela["Preço de Compra"] * tabela["Margem"]

    #exportar a base de dados atualizada
    tabela.to_excel("Produtos Novo.xlsx",index=False)
    print(tabela)
