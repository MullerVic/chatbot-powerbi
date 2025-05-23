from telegram import Bot
from config.settings import TELEGRAM_TOKEN  

bot = Bot(token=TELEGRAM_TOKEN)
bot.delete_webhook()
print("Webhook removido com sucesso!")