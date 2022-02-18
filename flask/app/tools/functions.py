import telegram
from app import app




def send_telegram(message):
  token = app.config['TELEGRAM_API_TOKEN']
  chatid = app.config['TELEGRAM_CHAT_ID']

  bot = telegram.Bot(token=token)
  bot.send_message(text=message, chat_id=chatid)








