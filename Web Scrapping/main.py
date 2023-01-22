from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

navegador = webdriver.Chrome() #cria o navegador controlado pelo selenium
navegador.get("https://www.google.com")#pegando cotação do dólar
navegador.find_element('xpath','/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação dólar')
navegador.find_element('xpath','/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
time.sleep(10)