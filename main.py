 import xos
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
  t.daemon = True
  t.start()


# ------------------ 2. تهيئة التوكن والبوت ------------------
TOKEN = os.environ.get(
    "BOT_TOKEN", "8991048500:AAFM5WEVgiYHXmVztYVRqm7A4p37vFgaxIw"
)
bot = telebot.TeleBot(TOKEN)

# ------------------ 3. إضافة زر القائمة (Menu) الدائم بجانب الكتابة ------------------
bot.set_my_commands([
    telebot.types.BotCommand("start", "إعادة تشغيل البوت وقائمة الخيارات")
])


# ------------------ 4. القوائم والأزرار التفاعلية ------------------
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
      "*مرحباً بك في منصة الهندسة الإلكترونية الدراسية!* ⚡\n\n"
      "اختر من القائمة أدناه للوصول إلى المواقع، الكتب، وشروحات المكونات مباشرة عبر الأزرار التفاعلية:"
  )

  bot.reply_to(message, welcome_text, reply_markup=markup, parse_mode="Markdown")


@bot.callback_query_handler(func=lambda call: True)
def callback_listener(call):
  bot.answer_callback_query(call.id)

  if call.data == "simulation":
    sim_markup = types.InlineKeyboardMarkup(row_width=1)
    sim_markup.add(
        types.InlineKeyboardButton(
            "⚡ EasyEDA (تصميم PCB ومحاكاة)", url="https://easyeda.com"
        ),
        types.InlineKeyboardButton(
            "🔌 Falstad Circuit Simulator",
            url="https://www.falstad.com/circuit/",
        ),
        types.InlineKeyboardButton(
            "💻 EDA Playground (VHDL / Verilog)",
            url="https://www.edaplayground.com",
        ),
        types.InlineKeyboardButton(
            "🤖 Wokwi (Arduino & ESP32)", url="https://wokwi.com"
        ),
    )
    bot.send_message(
        call.message.chat.id,
        "🌐 *أبرز مواقع المحاكاة والتصميم الإلكتروني:*",
        reply_markup=sim_markup,
        parse_mode="Markdown",
    )

  elif call.data == "books":
    books_markup = types.InlineKeyboardMarkup(row_width=1)
    books_markup.add(
        types.InlineKeyboardButton(
            "📖 Boylestad - Electronic Devices",
            url="https://www.google.com/search?q=Boylestad+Electronic+Devices+pdf",
        ),
        types.InlineKeyboardButton(
            "📘 Sedra & Smith - Microelectronic Circuits",
            url="https://www.google.com/search?q=Sedra+Smith+Microelectronic+Circuits+pdf",
        ),
        types.InlineKeyboardButton(
            "📗 Free Range VHDL (Free Textbook)",
            url="http://www.freerangevhdl.org/",
        ),
    )
    bot.send_message(
        call.message.chat.id,
        "📚 *المراجع والكتب الدراسية المعتمدة:*",
        reply_markup=books_markup,
        parse_mode="Markdown",
    )

  elif call.data == "components":
    comp_markup = types.InlineKeyboardMarkup(row_width=1)
    comp_markup.add(
        types.InlineKeyboardButton(
            "⚡ BJT & MOSFET Transistors",
            url="https://www.electronics-tutorials.ws/transistor/tran_1.html",
        ),
        types.InlineKeyboardButton(
            "📈 Operational Amplifiers (Op-Amps)",
            url="https://www.electronics-tutorials.ws/opamp/opamp_1.html",
        ),
        types.InlineKeyboardButton(
            "🔋 Linear Voltage Regulators",
            url="https://www.electronics-tutorials.ws/diode/diode_7.html",
        ),
    )
    bot.send_message(
        call.message.chat.id,
        "🔧 *شروحات المكونات الإلكترونية الأساسية:*",
        reply_markup=comp_markup,
        parse_mode="Markdown",
    )

  elif call.data == "control":
    ctrl_markup = types.InlineKeyboardMarkup(row_width=1)
    ctrl_markup.add(
        types.InlineKeyboardButton(
            "📊 Block Diagrams & Signal Flow",
            url="https://www.tutorialspoint.com/control_systems/control_systems_block_diagram_reduction.htm",
        ),
        types.InlineKeyboardButton(
            "🔄 Transfer Functions & Laplace",
            url="https://www.tutorialspoint.com/control_systems/control_systems_laplace_transform.htm",
        ),
        types.InlineKeyboardButton(
            "⚖️ Routh-Hurwitz Stability Criterion",
            url="https://www.tutorialspoint.com/control_systems/control_systems_routh_hurwitz_stability.htm",
        ),
    )
    bot.send_message(
        call.message.chat.id,
        "⚙️ *شروحات ومواضيع أنظمة التحكم (Control Systems):*",
        reply_markup=ctrl_markup,
        parse_mode="Markdown",
    )


# ------------------ 5. التشغيل النهائي ------------------
if __name__ == "__main__":
  keep_alive()
  print("Bot is running...")
  bot.infinity_polling()
