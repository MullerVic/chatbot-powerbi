from selenium import webdriver
from selenium.webdriver.common.by import By
from controllers.bot_controller import processar_mensagem
import time

driver = webdriver.Chrome()


class WhatsAppBot:
  def __init__(self):
        self.driver = webdriver.Chrome()
        self.session_file = 'whatsapp_session.pkl'

  def iniciar_whatsapp():
      driver.get("https://web.whatsapp.com")
      print("✅ Escaneie o QR Code para logar no WhatsApp...")
      time.sleep(20)

  def buscar_novas_mensagens():
    novas = []
    try:
        # Encontrar conversas com mensagens não lidas (círculo verde)
        elementos = driver.find_elements(By.CLASS_NAME, "_1pJ9J")  # classe que indica mensagens novas
        for el in elementos:
            el.click()
            time.sleep(2)

            # Encontrar a última mensagem recebida
            mensagens = driver.find_elements(By.CSS_SELECTOR, "div.message-in")
            ultima_msg = mensagens[-1].text

            # Pegar o nome do contato
            nome_contato = driver.find_element(By.XPATH, '//header//span[@dir="auto"]').text
            #Salva o nome/numero no array
            novas.append((nome_contato, ultima_msg))
    except NoSuchElementException:
        pass

    return novas

  def enviar_mensagem(contato, texto):
      try:
          campo_pesquisa = driver.find_element(By.XPATH, "//div[@title='Caixa de texto de pesquisa']")
          campo_pesquisa.clear()
          campo_pesquisa.send_keys(contato)
          time.sleep(2)

          contato_encontrado = driver.find_element(By.XPATH, f"//span[@title='{contato}']")
          contato_encontrado.click()
          time.sleep(1)

          campo_mensagem = driver.find_element(By.XPATH, "//div[@title='Digite uma mensagem']")
          campo_mensagem.send_keys(texto)
          campo_mensagem.send_keys(u'\ue007')  # tecla ENTER

          print(f"📤 Mensagem enviada para {contato}")
      except Exception as e:
          print(f"Erro ao enviar mensagem: {e}")
          
  def executar(self):
        self.iniciar_whatsapp()
        while True:
            novas = self.buscar_novas_mensagens()
            for contato, mensagem in novas:
                resposta = processar_mensagem(mensagem, contato)
                self.enviar_mensagem(contato, resposta)
            time.sleep(5)
  def monitorar_mensagens_loop():
    while True:
        contatos_e_mensagens = buscar_novas_mensagens() 
        for contato, mensagem in contatos_e_mensagens:
            resposta = processar_mensagem(mensagem, contato)
            enviar_mensagem(contato, resposta)
        time.sleep(5)
