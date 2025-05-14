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
        self.session_file = 'whatsapp_session.pkl'

    def iniciar(self):
        """Abre o navegador e o mantém aberto"""
        opcoes = webdriver.ChromeOptions()

        # Métodos para impetir que o navegador itendifique o bot como um bot
        opcoes.add_argument('--disable-blink-features=AutomationControlled')
        opcoes.add_experimental_option(
            "excludeSwitches", ["enable-automation"])
        opcoes.add_experimental_option('useAutomationExtension', False)

        # Verifica se já possui algum login realizado
        if os.path.exists(self.session_file):
            opcoes.add_argument(f"user-data-dir=./perfil_whatsapp")

        self.driver = webdriver.Chrome(options=opcoes)
        self.driver.get('https://web.whatsap.com')

        # Fazer o primeiro login
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
            # escanear QRcode
            WebDriverWait(self.driver, 120).until(
                EC.presence_of_element_located(By.XPATH, "//div[@role='textbox']"))
            print("Login realizado!")

    def _salvar_sessao(self):
        """Salvar os cookies"""
        if not os.path.exists(self.session_file):
            pickle.dump(sel .driver.get_cookies(),
                        open(self.session_file, "wb"))

    def monitorar_mensagem(self, numero_telefone):
        print("Monitorando mensagens...")

    while True:
        try:
            # Acha a última conversa com mensagem não lida
            nao_lidas = self.driver.find_elements(
                By.XPATH, '//div[@aria-label="Lista de conversas"]//span[@data-testid="icon-unread"]')

            for span in nao_lidas:
                # Clica na conversa
                span.click()
                time.sleep(1)

                # Captura a última mensagem recebida
                mensagens = self.driver.find_elements(
                    By.XPATH, '//div[contains(@class, "message-in")]//span[@dir="ltr"]')
                if mensagens:
                    ultima_msg = mensagens[-1].text.strip()
                    print(f"Mensagem recebida: {ultima_msg}")

                    if ultima_msg == "1":
                        self._responder(
                            "Acesse: https://minsaude.gov.br/fonte")
                    elif ultima_msg == "2":
                        self._responder("Gerando painel da dengue...")
                        # self._abrir_painel("dengue")
                    elif ultima_msg == "3":
                        self._responder("Gerando painel da covid...")
                        # self._abrir_painel("covid")
                    else:
                        self._responder("Comando inválido. Digite 1, 2 ou 3.")

                time.sleep(5)
        except Exception as e:
            print(f"Erro no monitoramento: {e}")
            time.sleep(5)

    def _responder(self, texto):
        try:
            caixa = self.driver.find_element(
                By.XPATH, "//div[@title='Digite uma mensagem']")
            caixa.click()
            caixa.send_keys(texto + Keys.ENTER)
        except Exception as e:
            print(f"Erro ao responder: {e}")

    def _abrir_painel(self, tipo):
        if tipo == "dengue":
            os.system("start https://meupainel.com/dengue")
        elif tipo == "covid":
            os.system("start https://meupainel.com/covid")
