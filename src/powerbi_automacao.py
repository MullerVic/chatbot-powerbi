import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def obter_dados_powerbi():
    df = pd.read_csv()
    
    return df.to_string()

#abrir o navegador
navegador = webdriver.Chrome()
#maximizar a tela
navegador.maximize_window()
#escolher o site
navegador.get("https://info.saude.df.gov.br/transparencia-e-prestacao-de-contas/dados-abertos/")
#espera implícita
navegador.implicitly_wait(10)

links_paineis_infograficos = navegador.find_elements(By.TAG_NAME, "a")

for link in links:
    href = link.get_attribute("href")
    if href and "#elementor-action%3Aaction%3Dpopup%3Aopen%26settings%3DeyJpZCI6IjQzNyIsInRvZ2dsZSI6ZmFsc2V9" href:
    link.click()
    break
else:
    print("Botão 'Transparência' não encontrado")
    
time.sleep(15)
navegador.quit()


