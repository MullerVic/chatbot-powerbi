def enviar_mensagem(contato, texto):
      try:
          campo_pesquisa = driver.find_element(By.XPATH, "//div[@title='Caixa de texto"
                                               "de pesquisa']")
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