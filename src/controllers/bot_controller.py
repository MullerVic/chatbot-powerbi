#from controllers.painel_controller import abrir_painel
from util.mensagem_util import enviar_mensagem


def processar_mensagem(mensagem, numero):
    comando = mensagem.strip()

    if comando == "1":
        enviar_mensagem("Acesse as fontes: https://meupainel.com/fontes", numero)
        #print("acesse as fontes")
    elif comando == "2":
        abrir_painel("dengue", numero)
        #print("dengue")
    elif comando == "3":
        abrir_painel("covid", numero)
        #print("covid")
    else:
        enviar_mensagem("Comando inválido. Digite:\n" 
                        "1- Fontes\n2 - Painel Dengue\n"
                        "3 - Painel Covid", numero)
        #print("erro")
