import openai
from config.settings import OPEN_AI_KEY

openai.api_key = OPEN_AI_KEY


async def gerar_resposta_chatgpt(mensagem_usuario: str) -> str:
  try:
    resposta = await openai.ChatCompletions.acreate(
      model = "gpt-3.5-turbo",
      messages =[
        {"role": "system", "content": "Você é um assistente que resume dados de dashboards sobre a área da saúde do Distrito Federal em forma de texto"},
        {"role": "user", "content": mensagem_usuario}
      ],
      temperature = 0.5,
      max_tokens = 500
    )
    print(resposta)
    return resposta.choices[0].message["content"]
  
  except Exception as e:
    print("Erro API chatgpt")
    return f"Erro ao gerar resposta: {str(e)}"