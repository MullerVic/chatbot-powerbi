import pywhatkit as kit
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
import pickle
import os


class WhatsAppBot:
    def __init__(self):
      self.driver = None
      self.session_file= 'whatsapp_session.pkl'
      
    def iniciar(self):
      """Abre o navegador e o mantém aberto"""
      opcoes = webdriver.ChromeOptions()
      
      #Métodos para impetir que o navegador itendifique o bot como um bot
      opcoes.add_argument('--disable-blink-features=AutomationControlled')
      opcoes.add_experimental_option("excludeSwitches", ["enable-automation"])
      opcoes.add_experimental_option('useAutomationExtension', False)
      
      #Verifica se já possui algum login realizado
      if os.path.exists(self.session_file):
          opcoes.add_argument(f"user-data-dir=./perfil_whatsapp")
          
      self.driver = webdriver.Chrome(options=opcoes)
      self.driver.get('https://web.whatsap.com')
      
      
      #Fazer o primeiro login
      try:
          self._aguardar_login()
          self._salvar_sessao()
      except Exception() as e:
          print("Erro de login: {e}")
          self.driver.quit()
          return False   
      return True
  
    def _aguardar_login(self):
        if not os.path.exists(self.session_file):
            #escanear QRcode
            WebDriverWait(self.driver, 120).until(
                EC.presence_of_element_located(By.XPATH, "//div[@role='textbox']"))
            print("Login realizado!") 
    
    def _salvar_sessao(self):
        """Salvar os cookies"""
        if not os.path.exists(self.session_file):
            pickle.dump(self.driver.get_cookies(), open(self.session_file, "wb"))
            
                
    def monitorar_mensagem(self):
        """monitora mensagem de novo usuário"""
        print("Monitorando mensagens de novos contatos...")