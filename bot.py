import os
import telebot
from threading import Thread
from flask import Flask
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# ------------------ 1. خادم Flask لإبقاء البوت نشطاً ------------------
app = Flask("")

@app.route("/")
def home():
    return "Bot is alive and running!"

def run():
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

def keep_alive():
    t = Thread(target=run)
    t.start()

# ------------------ 2. إعداد التوكن البوت ------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

# ------------------ 3. بناء القوائم ------------------
def main_menu():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton("1️⃣ أساسيات الإلكترونيات", callback_data="cat1"),
        InlineKeyboardButton("2️⃣ المحاكاة والتجربة", callback_data="cat2"),
        InlineKeyboardButton("3️⃣ برامج التصميم (PCB)", callback_data="cat3"),
        InlineKeyboardButton("4️⃣ مراجع و داتا شيت", callback_data="cat4")
    )
    return markup

def menu_cat1():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton("Arduino Docs", url="https://docs.arduino.cc"),
        InlineKeyboardButton("Electronics Tutorials", url="https://www.electronics-tutorials.ws"),
        InlineKeyboardButton("All About Circuits", url="https://www.allaboutcircuits.com"),
        InlineKeyboardButton("Instructables", url="https://www.instructables.com"),
        InlineKeyboardButton("CircuitDigest", url="https://circuitdigest.com"),
        InlineKeyboardButton("🔙 العودة للقائمة الرئيسية", callback_data="back_to_main")
    )
    return markup

def menu_cat2():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton("Wokwi", url="https://wokwi.com"),
        InlineKeyboardButton("LabEx", url="https://labex.io"),
        InlineKeyboardButton("EDA Playground", url="https://www.edaplayground.com"),
        InlineKeyboardButton("Tinkercad", url="https://www.tinkercad.com"),
        InlineKeyboardButton("Falstad", url="https://www.falstad.com/circuit"),
        InlineKeyboardButton("🔙 العودة للقائمة الرئيسية", callback_data="back_to_main")
    )
    return markup

def menu_cat3():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton("EasyEDA", url="https://easyeda.com"),
        InlineKeyboardButton("KiCad", url="https://www.kicad.org"),
        InlineKeyboardButton("Altium", url="https://www.altium.com"),
        InlineKeyboardButton("PCBWay", url="https://www.pcbway.com"),
        InlineKeyboardButton("JLCPCB", url="https://jlcpcb.com"),
        InlineKeyboardButton("🔙 العودة للقائمة الرئيسية", callback_data="back_to_main")
    )
    return markup

def menu_cat4():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton("Electronics Lab", url="https://www.electronics-lab.com"),
        InlineKeyboardButton("AllDataSheet", url="https://www.alldatasheet.com"),
        InlineKeyboardButton("Octopart", url="https://octopart.com"),
        InlineKeyboardButton("DigiKey", url="https://www.digikey.com"),
        InlineKeyboardButton("Mouser", url="https://www.mouser.com"),
        InlineKeyboardButton("🔙 العودة للقائمة الرئيسية", callback_data="back_to_main")
    )
    return markup

# ------------------ 4. معالج أمر البداية /start ------------------
@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = (
        "مرحباً بك في منصة الهندسة الإلكترونية الدراسية! ⚡\n\n"
        "هذا البوت مصمم خصيصاً لطلاب ومحبي تكنولوجيا وهندسة الإلكترونيات "
        "ليجمع لك أهم المصادر والمواقع والمراجع في مكان واحد.\n\n"
        "اختر أحد الأقسام من القائمة أدناه للبدء:"
    )
    bot.send_message(message.chat.id, welcome_text, reply_markup=main_menu())

# ------------------ 5. معالج التفاعل مع الأزرار ------------------
@bot.callback_query_handler(func=lambda call: True)
def callback_listener(call):
    bot.answer_callback_query(call.id)
    chat_id = call.message.chat.id
    message_id = call.message.message_id

    if call.data == "cat1":
        bot.edit_message_text("📘 **قسم أساسيات الإلكترونيات:**\nاختر أحد المصادر التالية:", chat_id, message_id, reply_markup=menu_cat1(), parse_mode="Markdown")
    elif call.data == "cat2":
        bot.edit_message_text("🚀 **قسم المحاكاة والتجربة:**\nاختر منصة المحاكاة للبدء:", chat_id, message_id, reply_markup=menu_cat2(), parse_mode="Markdown")
    elif call.data == "cat3":
        bot.edit_message_text("🖥️ **برامج وتصنيع الـ PCB:**\nأبرز الأدوات والشركات:", chat_id, message_id, reply_markup=menu_cat3(), parse_mode="Markdown")
    elif call.data == "cat4":
        bot.edit_message_text("🔍 **المراجع والداتا شيت:**\nالمكتبات والمواقع المعتمدة:", chat_id, message_id, reply_markup=menu_cat4(), parse_mode="Markdown")
    elif call.data == "back_to_main":
        bot.edit_message_text("⚡ **القائمة الرئيسية:**\nاختر أحد الأقسام للبدء:", chat_id, message_id, reply_markup=main_menu(), parse_mode="Markdown")

# ------------------ 6. التشغيل النهائي ------------------
if __name__ == "__main__":
    keep_alive()
    bot.infinity_polling(non_stop=True)
