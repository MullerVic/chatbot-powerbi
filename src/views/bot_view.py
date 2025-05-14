from selenium import webdriver
from selenium.webdriver.common.by import By
from controllers.bot_controller import processar_mensagem
from selenium.common.exceptions import NoSuchElementException
import time
from util.mensagem_util import enviar_mensagem

class WhatsAppBot:
  def __init__(self):
        self.driver = webdriver.Chrome()
        self.session_file = 'whatsapp_session.pkl'

  def iniciar_whatsapp(self):
      self.driver.get("https://web.whatsapp.com")
      print("[ok] Escaneie o QR Code para logar no WhatsApp...")
      time.sleep(20)

  def buscar_novas_mensagens(self):
    novas = []
    try:
        # Encontrar conversas com mensagens não lidas (círculo verde)
        elementos = self.driver.find_elements(By.CLASS_NAME, "_ahlk")  # classe que indica mensagens novas
        for el in elementos:
            el.click()
            time.sleep(2)

            # Encontrar a última mensagem recebida
            mensagens = self.driver.find_elements(By.CSS_SELECTOR, "div.message-in")
            ultima_msg = mensagens[-1].text

            # Pegar o nome do contato
            nome_contato = self.driver.find_element(By.XPATH, '//header//span[@dir="auto"]').text
            #Salva o nome/numero no array
            novas.append((nome_contato, ultima_msg))
    except NoSuchElementException:
        pass

    return novas

  def executar(self):
        self.iniciar_whatsapp()
        while True:
            novas = self.buscar_novas_mensagens()
            for contato, mensagem in novas:
                resposta = processar_mensagem(mensagem, contato)
                self.enviar_mensagem(contato, resposta)
            time.sleep(5)
  def monitorar_mensagens_loop(self):
    while True:
        contatos_e_mensagens = self.buscar_novas_mensagens() 
        for contato, mensagem in contatos_e_mensagens:
            resposta = processar_mensagem(mensagem, contato)
            enviar_mensagem(contato, resposta)
        time.sleep(5)
