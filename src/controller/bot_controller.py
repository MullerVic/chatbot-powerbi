from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from config.settings import TELEGRAM_TOKEN
from controller.chatgpt_controller import gerar_resposta_chatgpt
from telegram import Bot

bot = Bot(token=TELEGRAM_TOKEN)



async def start (update: Update, context: ContextTypes.DEFAULT_TYPE):
  await update.message.reply_text("Bem vindo ao InfoSaúde, o portal oficial da saúde do DF.\n"
        "Aqui você tem acesso as informações sobre a saúde da região por Infográficos\n"
        "Quais informações você deseja obter hoje?\n"
        "Digite: \n"
        "1 - Dengue\n2 - SARG \n3 - Nascimentos \n4 - \n5 Óbitos- Fontes"
        "Ou digite 0 para sair")

async def resumir (update: Update, context: ContextTypes.DEFAULT_TYPE):
  mensagem_usuario = ' '.join(context.args)
  if not mensagem_usuario:
    await update.message.reply_text("Por favor, envie o comando assim: /resumir [sua mensagem]")
    return
  
  await update.message.reply_text("Gerando resumo com o ChatGPT...")
  
  resposta = await gerar_resposta_chatgpt(mensagem_usuario)
  
  await update.message.reply_text(resposta)
def iniciar_bot():
  app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
  
  app.add_handler(CommandHandler("start", start))
  #app.add_handler(CommandHandler("resumir", resumir))
  
  print("Bot iniciado com sucesso!")
  app.run_polling()