import os
import threading
from flask import Flask
import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

BOT_TOKEN = '8278573609:AAHAXRsqPZZiw7zzvqJ9vFIqG-Fnk3UiCYs'
bot = telebot.TeleBot(BOT_TOKEN)

# إعداد خادم Flask بسيط جداً لإبقاء المنصة نشطة
app = Flask(__name__)


@app.route('/')
def index():
  return 'Bot is running!'


def run_flask():
  port = int(os.environ.get('PORT', 8080))
  app.run(host='0.0.0.0', port=port)


# تشغيل الخادم في خيط منفصل
threading.Thread(target=run_flask, daemon=True).start()


# القوائم والأزرار
def main_menu():
  markup = InlineKeyboardMarkup()
  markup.add(
      InlineKeyboardButton('1️⃣ أساسيات الإلكترونيات', callback_data='cat1')
  )
  markup.add(InlineKeyboardButton('2️⃣ المحاكاة والتجربة', callback_data='cat2'))
  markup.add(InlineKeyboardButton('3️⃣ برامج التصميم (PCB)', callback_data='cat3'))
  markup.add(InlineKeyboardButton('4️⃣ مراجع و داتا شيت', callback_data='cat4'))
  return markup


@bot.message_handler(commands=['start'])
def send_welcome(message):
  try:
    bot.send_message(
        message.chat.id,
        'مرحباً بك في منصة الهندسة الإلكترونية الدراسية! ⚡\nاختر فئة للبدء:',
        reply_markup=main_menu(),
    )
  except Exception as e:
    print(f'Error in start: {e}')


@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
  try:
    bot.answer_callback_query(call.id)
    if call.data == 'cat1':
      bot.send_message(
          call.message.chat.id,
          '📚 روابط أساسيات الإلكترونيات:\nhttps://www.electronics-tutorials.ws/',
      )
    elif call.data == 'cat2':
      bot.send_message(
          call.message.chat.id,
          '🚀 روابط المحاكاة:\nhttps://wokwi.com/\nhttps://www.falstad.com/circuit/',
      )
    elif call.data == 'cat3':
      bot.send_message(
          call.message.chat.id,
          '🖥️ برامج التصميم:\nhttps://easyeda.com/\nhttps://www.kicad.org/',
      )
    elif call.data == 'cat4':
      bot.send_message(
          call.message.chat.id,
          '🔍 المراجع والداتا شيت:\nhttps://www.alldatasheet.com/',
      )
  except Exception as e:
    print(f'Error in callback: {e}')


if __name__ == '__main__':
  print('Bot starting...')
  bot.remove_webhook()
  bot.infinity_polling(skip_pending=True)
