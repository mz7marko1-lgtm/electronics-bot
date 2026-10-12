import os
import telebot
from threading import Thread
from flask import Flask
from telebot import types

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

keep_alive()

BOT_TOKEN = os.environ.get(
    "BOT_TOKEN", "8991048500:AAFM5WEVgiYHXmVztYVRqm7A4p37vFgaxIw"
)

bot = telebot.TeleBot(BOT_TOKEN)

# ------------------ القائمة الرئيسية (5 أقسام شاملة) ------------------
def main_menu():
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("1️⃣ أساسيات الإلكترونيات", callback_data="cat1"),
        types.InlineKeyboardButton("2️⃣ المحاكاة والتجربة", callback_data="cat2"),
        types.InlineKeyboardButton("3️⃣ برامج التصميم (PCB)", callback_data="cat3"),
        types.InlineKeyboardButton("4️⃣ مراجع و داتا شيت", callback_data="cat4"),
        types.InlineKeyboardButton("5️⃣ شبكات سيسكو (Cisco & Networks)", callback_data="cat5")
    )
    return markup

# القوائم الفرعية مع الروابط التعليمية المتميزة
def menu_cat1():
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("Arduino Docs", url="https://www.arduino.cc/"),
        types.InlineKeyboardButton("Electronics Tutorials", url="https://www.electronics-tutorials.ws/"),
        types.InlineKeyboardButton("All About Circuits", url="https://www.allaboutcircuits.com/"),
        types.InlineKeyboardButton("Instructables", url="https://www.instructables.com/"),
        types.InlineKeyboardButton("CircuitDigest", url="https://circuitdigest.com/"),
        types.InlineKeyboardButton("🔙 العودة للقائمة الرئيسية", callback_data="back_to_main")
    )
    return markup

def menu_cat2():
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("Wokwi", url="https://wokwi.com/"),
        types.InlineKeyboardButton("LabEx", url="https://labex.io/"),
        types.InlineKeyboardButton("EDA Playground", url="https://www.edaplayground.com/"),
        types.InlineKeyboardButton("Tinkercad", url="https://www.tinkercad.com/"),
        types.InlineKeyboardButton("Falstad", url="https://www.falstad.com/circuit/"),
        types.InlineKeyboardButton("🔙 العودة للقائمة الرئيسية", callback_data="back_to_main")
    )
    return markup

def menu_cat3():
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("EasyEDA", url="https://easyeda.com/"),
        types.InlineKeyboardButton("KiCad", url="https://www.kicad.org/"),
        types.InlineKeyboardButton("Altium", url="https://www.altium.com/"),
        types.InlineKeyboardButton("PCBWay", url="https://www.pcbway.com/"),
        types.InlineKeyboardButton("JLCPCB", url="https://jlcpcb.com/"),
        types.InlineKeyboardButton("🔙 العودة للقائمة الرئيسية", callback_data="back_to_main")
    )
    return markup

def menu_cat4():
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("Electronics Lab", url="https://www.electronicslab.com/"),
        types.InlineKeyboardButton("AllDataSheet", url="https://www.alldatasheet.com/"),
        types.InlineKeyboardButton("Octopart", url="https://octopart.com/"),
        types.InlineKeyboardButton("DigiKey", url="https://www.digikey.com/"),
        types.InlineKeyboardButton("Mouser", url="https://www.mouser.com/"),
        types.InlineKeyboardButton("🔙 العودة للقائمة الرئيسية", callback_data="back_to_main")
    )
    return markup

def menu_cat5():
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("Cisco Networks Guide", url="https://www.tutorialspoint.com/cisco-networks/index.htm"),
        types.InlineKeyboardButton("Cisco Networking Academy", url="https://www.netacad.com/"),
        types.InlineKeyboardButton("Packet Tracer Overview", url="https://www.netacad.com/courses/packet-tracer"),
        types.InlineKeyboardButton("🔙 العودة للقائمة الرئيسية", callback_data="back_to_main")
    )
    return markup

@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = (
        "مرحباً بك في منصة الهندسة الإلكترونية والشبكات الدراسية! ⚡\n"
        "هذا البوت مصمم خصيصاً لطلاب ومحبي تكنولوجيا والهندسة لجمع كافة المصادر والمراجع العلمية.\n"
        "اختر أحد الأقسام أدناه للبدء:"
    )
    bot.send_message(message.chat.id, welcome_text, reply_markup=main_menu())

@bot.callback_query_handler(func=lambda call: True)
def callback_listener(call):
    bot.answer_callback_query(call.id)
    if call.data == "cat1":
        bot.edit_message_text("📘 **قسم أساسيات الإلكترونيات:**\nاختر المرجع أو الموقع المناسب لدراستك:", call.message.chat.id, call.message.message_id, reply_markup=menu_cat1(), parse_mode="Markdown")
    elif call.data == "cat2":
        bot.edit_message_text("🚀 **قسم المحاكاة والتجربة:**\nأفضل منصات محاكاة الدوائر والأنظمة:", call.message.chat.id, call.message.message_id, reply_markup=menu_cat2(), parse_mode="Markdown")
    elif call.data == "cat3":
        bot.edit_message_text("🖥️ **قسم برامج التصميم (PCB):**\nبرامج تصميم وتصنيع اللوحات الإلكترونية المطبوعة:", call.message.chat.id, call.message.message_id, reply_markup=menu_cat3(), parse_mode="Markdown")
    elif call.data == "cat4":
        bot.edit_message_text("🔍 **قسم المراجع وداتا شيت:**\nللبحث عن خصائص القطع والمكونات الإلكترونية:", call.message.chat.id, call.message.message_id, reply_markup=menu_cat4(), parse_mode="Markdown")
    elif call.data == "cat5":
        bot.edit_message_text("🌐 **قسم شبكات سيسكو (Cisco Networks):**\nأهم مصادر ومناهج تعلم شبكات الحاسب وسيسكو:", call.message.chat.id, call.message.message_id, reply_markup=menu_cat5(), parse_mode="Markdown")
    elif call.data == "back_to_main":
        welcome_text = (
            "مرحباً بك في منصة الهندسة الإلكترونية والشبكات الدراسية! ⚡\n"
            "هذا البوت مصمم خصيصاً لطلاب ومحبي تكنولوجيا والهندسة لجمع كافة المصادر والمراجع العلمية.\n"
            "اختر أحد الأقسام أدناه للبدء:"
        )
        bot.edit_message_text(welcome_text, call.message.chat.id, call.message.message_id, reply_markup=main_menu(), parse_mode="Markdown")

if __name__ == "__main__":
    bot.infinity_polling(non_stop=True)

