from controllers.bot_controller import processar_mensagem

# Testes simulando diferentes mensagens recebidas
mensagens_teste = ["1", "2", "3", "99", ""]

for msg in mensagens_teste:
    resposta = processar_mensagem(msg, "usuário_teste")
    print(f"> Usuário: {msg}")
    print(f"< Bot: {resposta}")
    print("-" * 30)
