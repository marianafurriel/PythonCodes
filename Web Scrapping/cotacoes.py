from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def cotacoes():
    navegador = webdriver.Chrome() #cria o navegador controlado pelo selenium
    #cotação do dolar
    navegador.get("https://www.google.com")
    navegador.find_element('xpath','/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação dólar') #digita cotação dolar na barra de pesquisa
    navegador.find_element('xpath','/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER) #pressionar enter
    cotacao_dolar = navegador.find_element('xpath','//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value') #salva a cotação dólar na variável

    #cotação euro
    navegador.get("https://www.google.com")
    navegador.find_element('xpath','/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação euro') #digita cotação dolar na barra de pesquisa
    navegador.find_element('xpath','/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER) #pressionar enter
    cotacao_euro = navegador.find_element('xpath','//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value') #salva a cotação dólar na variável


    #cotação ouro
    navegador.get("https://www.melhorcambio.com/ouro-hoje")
    cotacao_ouro = navegador.find_element('xpath','//*[@id="comercial"]').get_attribute('value') #salva a cotação dólar na variável
    cotacao_ouro = cotacao_ouro.replace(',','.')

    navegador.quit()
    return cotacao_dolar,cotacao_euro,cotacao_ouro
