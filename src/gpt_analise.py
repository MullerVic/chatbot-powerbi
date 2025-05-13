import openai
import os
from dotenv import load_dotenv


load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def analisar_texto(texto: str) -> str:
    response = openai.ChatCompletion.create(
      model = "gpt-3.5",
      messages = [{"funcao": "usuario", "conteudo": texto}]
    )
    
    return response['escolhas'][0]['mensagem']['conteudo']