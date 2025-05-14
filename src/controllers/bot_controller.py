#from controllers.painel_controller import abrir_painel
from views.bot_view import enviar_mensagem


def processar_mensagem(mensagem, numero):
    comando = mensagem.strip()

    if comando == "1":
        #enviar_mensagem(numero, "Acesse as fontes: https://meupainel.com/fontes")
        print("acesse as fontes")
    elif comando == "2":
        #abrir_painel("dengue", numero)
        print("dengue")
    elif comando == "3":
        #abrir_painel("covid", numero)
        print("covid")
    else:
        #enviar_mensagem(numero, "Comando inválido. Digite:\n1 - Fontes\n2 - Painel Dengue\n3 - Painel Covid")
        print("erro")
