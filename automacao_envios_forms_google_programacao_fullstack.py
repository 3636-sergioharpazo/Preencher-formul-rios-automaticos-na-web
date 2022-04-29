
import pandas as pd
from selenium import webdriver
import time 
from selenium.webdriver.common.keys import Keys
#from webdriver_manager.chrome import ChromeDriverManager

#driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(r"C:/Program Files/Google/Chrome/Application/chromedriver.exe")
#navegador = webdriver.Chrome()



tabela = pd.read_excel("enquete.xlsx")
#display(tabela)

for i, nome in enumerate(tabela['NOME']):
    cpf = tabela.loc[i, 'CPF']
    telefone = tabela.loc[i, 'TELEFONE']
    endereco = tabela.loc[i, 'ENDEREÇO']
    texto = tabela.loc[i, 'TEXTO']
  
    driver.get("https://forms.gle/KTaiJqmrwnL23dE69")
    # preencher com nome
    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(nome)
    # preencher 
    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(str(cpf))
    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(str(telefone))
    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea').send_keys(endereco)
    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div[2]/textarea').send_keys(texto)
  
    
    #clicar no botao
    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span').click()
    time.sleep(2)