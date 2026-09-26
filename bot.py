clear from telebot.types import 
InlineKeyboardMarkup, InlineKeyboardButbot = 
telebot.TeleBot(BOT_TOKEN)






















import os
from threading import Thread
from flask import Flask
from telebot import types
import telebot

# ------------------ 1. تهيئة خادم Flask لخدمة Render ------------------
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


# ------------------ 2. تهيئة التوكن والبوت ------------------
TOKEN = os.environ.get(
    "BOT_TOKEN", "8278573609:AAHTK3-kghgQtVB7JAKjLyZtl_LU_3dQPzc"
)
bot = telebot.TeleBot(TOKEN)

# ------------------ 3. القوائم والأزرار التفاعلية ------------------


@bot.message_handler(commands=["start"])
def send_welcome(message):
  markup = types.InlineKeyboardMarkup(row_width=2)

  btn_sim = types.InlineKeyboardButton(
      "🌐 مواقع المحاكاة", callback_data="simulation"
  )
  btn_books = types.InlineKeyboardButton(
      "📚 المراجع والكتب", callback_data="books"
  )
  btn_explain = types.InlineKeyboardButton(
      "🔧 شروحات المكونات", callback_data="components"
  )
  btn_control = types.InlineKeyboardButton(
      "⚙️ أنظمة التحكم", callback_data="control"
  )

  markup.add(btn_sim, btn_books, btn_explain, btn_control)

  welcome_text = (
      "مرحباً بك في منصة الهندسة الإلكترونية الدراسية! ⚡\n\n"
      "هذا البوت مصمم خصيصاً لطلاب ومحبي تكنولوجيا وهندسة الإلكترونيات، "
      "ليجمع لك كل ما تحتاجه في مكان واحد:\n"
      "🌐 أفضل مواقع محاكاة الدوائر (Simulation)\n"
      "📚 المراجع والكتب الدراسية المعتمدة\n"
      "🔧 شروحات تفصيلية للمكونات الإلكترونية وأنظمة التحكم.\n\n"
      "اختر من القائمة أدناه للبدء:"
  )

  bot.reply_to(message, welcome_text, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_listener(call):
  if call.data == "simulation":
    bot.answer_callback_query(call.id)
    bot.send_message(
        call.message.chat.id,
        "🌐 **أبرز مواقع المحاكاة:**\n- EasyEDA\n- EDA Playground\n- Falstad Circuit Simulator",
    )
  elif call.data == "books":
    bot.answer_callback_query(call.id)
    bot.send_message(
        call.message.chat.id,
        "📚 **قسم المراجع:**\nستجد هنا الكتب المعتمدة والحلول.",
    )
  elif call.data == "components":
    bot.answer_callback_query(call.id)
    bot.send_message(
        call.message.chat.id,
        "🔧 **شروحات المكونات:**\n- Transistors (BJT / MOSFET)\n- Operational Amplifiers\n- Voltage Regulators",
    )
  elif call.data == "control":
    bot.answer_callback_query(call.id)
    bot.send_message(
        call.message.chat.id,
        "⚙️ **أنظمة التحكم:**\nشروحات الـ Block Diagrams وحسابات Transfer Functions و Routh-Hurwitz Criterion.",
    )


# ------------------ 4. التشغيل النهائي ------------------
if __name__ == "__main__":
  keep_alive()
  bot.infinity_polling(non_stop=True)









def main_menu():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton("1️⃣ أساسيات الإلكترونيات", callback_data="cat1"),
        InlineKeyboardButton("2️⃣ المحاكاة والتجربة", callback_data="cat2"),
        InlineKeyboardButton("3️⃣ برامج التصميم (PCB)", callback_data="cat3"),
        InlineKeyboardButton("4️⃣ مراجع و داتا شيت", callback_data="cat4")
    )
    return markup

# القوائم الفرعية (5 روابط لكل واحدة)
def menu_cat1():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton("Arduino Docs", url="https://docs.arduino.cc/learn/"),
        InlineKeyboardButton("Electronics Tutorials", url="https://www.electronics-tutorials.ws/"),
        InlineKeyboardButton("All About Circuits", url="https://www.allaboutcircuits.com/textbook/"),
        InlineKeyboardButton("Instructables", url="https://www.instructables.com/circuits/"),
        InlineKeyboardButton("CircuitDigest", url="https://circuitdigest.com/"),
        InlineKeyboardButton("🔙 العودة", callback_data="back_to_main")
    )
    return markup

def menu_cat2():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton("Wokwi", url="https://wokwi.com/"),
        InlineKeyboardButton("LabEx", url="https://labex.io/projects"),
        InlineKeyboardButton("EDA Playground", url="https://www.edaplayground.com/x/A4"),
        InlineKeyboardButton("Tinkercad", url="https://www.tinkercad.com/circuits"),
        InlineKeyboardButton("Falstad", url="https://www.falstad.com/circuit/"),
        InlineKeyboardButton("🔙 العودة", callback_data="back_to_main")
    )
    return markup

def menu_cat3():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton("EasyEDA", url="https://easyeda.com/editor-mobile/"),
        InlineKeyboardButton("KiCad", url="https://www.kicad.org/"),
        InlineKeyboardButton("Altium", url="https://www.altium.com/"),
        InlineKeyboardButton("PCBWay", url="https://www.pcbway.com/"),
        InlineKeyboardButton("JLCPCB", url="https://jlcpcb.com/"),
        InlineKeyboardButton("🔙 العودة", callback_data="back_to_main")
    )
    return markup

def menu_cat4():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton("Electronics Lab", url="https://www.electronics-lab.com/"),
        InlineKeyboardButton("AllDataSheet", url="https://www.alldatasheet.com/"),
        InlineKeyboardButton("Octopart", url="https://octopart.com/"),
        InlineKeyboardButton("DigiKey", url="https://www.digikey.com/en/resources"),
        InlineKeyboardButton("Mouser", url="https://www.mouser.com/"),
        InlineKeyboardButton("🔙 العودة", callback_data="back_to_main")
    )
    return markup

@bot.callback_query_handler(func=lambda call: True)
def callback_listener(call):
    bot.answer_callback_query(call.id)
    if call.data == "cat1": bot.edit_message_text("📘 الأساسيات:", call.message.chat.id, call.message.message_id, reply_markup=menu_cat1())
    elif call.data == "cat2": bot.edit_message_text("🚀 المحاكاة:", call.message.chat.id, call.message.message_id, reply_markup=menu_cat2())
    elif call.data == "cat3": bot.edit_message_text("🖥️ التصميم:", call.message.chat.id, call.message.message_id, reply_markup=menu_cat3())
    elif call.data == "cat4": bot.edit_message_text("🔍 المراجع:", call.message.chat.id, call.message.message_id, reply_markup=menu_cat4())
    elif call.data == "back_to_main": bot.edit_message_text("مرحباً بك! اختر فئة:", call.message.chat.id, call.message.message_id, reply_markup=main_menu())

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "مرحباً بك في منصة الهندسة الإلكترونية الدراسية! ⚡\nاختر فئة للبدء:", reply_markup=main_menu())

bot.infinity_polling()
