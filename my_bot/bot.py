import telebot
import sqlite3
import os

# تحديد المسار ليصبح في مجلد التنزيلات (Downloads)
db_path = "/sdcard/Download/my_database.db"

# الاتصال بقاعدة البيانات
conn = sqlite3.connect(db_path, check_same_thread=False)
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY)')
conn.commit()

TOKEN = "8278573609:AAHAXRsqPZZiw7zzvqJ9vFIqG-Fnk3UiCYs"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.chat.id
    cursor.execute('INSERT OR IGNORE INTO users (id) VALUES (?)', (user_id,))
    conn.commit()
    bot.reply_to(message, "تم حفظ بياناتك في قاعدة البيانات الموجودة في مجلد التحميلات!")

print("البوت يعمل الآن...")
bot.polling()

