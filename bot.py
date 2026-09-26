import os
from flask import Flask, request
import telebot

BOT_TOKEN = '8278573609:AAHAXRsqPZZiw7zzvqJ9vFIqG-Fnk3UiCYs'
bot = telebot.TeleBot(BOT_TOKEN)

app = Flask(__name__)


@app.route('/')
def index():
  return 'Bot is running!'


# استقبال التحديثات عبر الـ Webhook (الطريقة الرسمية المستقرة على Render)
@app.route(f'/{BOT_TOKEN}', methods=['POST'])
def webhook():
  if request.headers.get('content-type') == 'application/json':
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return '', 200
  else:
    return 'Forbidden', 403


if __name__ == '__main__':
  # ربط الـ Webhook تلقائياً عند التشغيل
  app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
