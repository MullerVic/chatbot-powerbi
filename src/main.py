#from gpt_analise import analisar_texto
#from powerbi_automacao import obter_dados_powerbi
#from whatsap_bot import enviar_mensagem
from views.bot_view import WhatsAppBot
from controllers.bot_controller import processar_mensagem
#def executar_chatbot():
 ##   dados = obter_dados_powerbi()
   # analise = analisar_texto(dados)
    #enviar_mensagem(analise)


if __name__ == "__main__":
    bot = WhatsAppBot()
    bot.iniciar_whatsapp()
    bot.monitorar_mensagens_loop()

    