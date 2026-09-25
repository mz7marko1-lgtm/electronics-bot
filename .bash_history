rm -f bot.py
nano bot.py
python bot.py
pkg update && pkg upgrade
termux-setup-storage
pkg install python
،  
python bot.py
pkg install python -y
pkg update -y
pkg install python -y
python bot.py
pkg install python -y
pip install pyTelegramBotAPI
python bot.py
nano bot.py
cat << 'EOF' > bot.py
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = '8278573609:AAHAXRsqPZZiw7zzvqJ9vFIqG-Fnk3UiCYs'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton("🌐 مواقع محاكاة الدوائر (Simulation)", callback_data="simulation")
    button2 = InlineKeyboardButton("📚 كتب ومراجع إلكترونية", callback_data="books")
    button3 = InlineKeyboardButton("🛠️ شروحات المكونات (MOSFET, JFET...)", callback_data="components")
    markup.add(button1)
    markup.add(button2)
    markup.add(button3)
    bot.reply_to(message, "مرحباً بك في منصة الهندسة الإلكترونية الدراسية! ⚡\nالرجاء اختيار القسم الذي تريد تصفحه من الأسفل:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "simulation":
        text = (
            "📌 **أفضل مواقع محاكاة الدوائر الإلكترونية:**\n\n"
            "1️⃣ **Falstad Circuit Simulator**\n"
            "🔗 الرابط: http://www.falstad.com/circuit/\n\n"
            "2️⃣ **Tinkercad Circuits**\n"
            "🔗 الرابط: https://www.tinkercad.com/\n\n"
            "3️⃣ **EasyEDA**\n"
            "🔗 الرابط: https://easyeda.com/"
        )
        bot.send_message(call.message.chat.id, text, parse_mode="Markdown")
    elif call.data == "books":
        bot.send_message(call.message.chat.id, "📚 هذا القسم سيحتوي على روابط كتب ومراجع الهندسة الإلكترونية المقررة قريباً.")
    elif call.data == "components":
        bot.send_message(call.message.chat.id, "🛠️ هذا القسم سيحتوي على شروحات مفصلة للمكونات مثل الـ MOSFET والـ JFET وأنظمة التحكم قريباً.")

print("البوت يعمل الآن بنجاح...")
bot.infinity_polling()
EOF

python bot.py
cd bot-folder
pm2 start main.py --name "my-bot"
ls
nano bot.py
ls
pm2 delete all
pm2 start bot.py
pm2 logs
nano bot.py
ls
pm2 delete all
pm2 start bot.py
pm2 logs
pkg install apache2
y
pkg install apache2
apachectl start
echo "<h1>مرحباً بك في موقعي الشخصي على هاتف Realme!</h1>" > $PREFIX/share/apache2/default-site/htdocs/index.html
nano $PREFIX/share/apache2/default-site/htdocs/index.html
apachectl restart
nano $PREFIX/share/apache2/default-site/htdocs/index.html
nano $PREFIX/share/apache2/default-site/htdocs/manifest.json
nano $PREFIX/share/apache2/default-site/htdocs/index.html
apachectl restart
body { animation: colorchange 10s infinite; }
@keyframes colorchange {
}
nano $PREFIX/share/apache2/default-site/htdocs/index.html
apachectl restart
nano $PREFIX/share/apache2/default-site/htdocs/index.html
apachectl restart
nano $PREFIX/share/apache2/default-site/htdocs/index.html
apachectl restart
nano $PREFIX/share/apache2/default-site/htdocs/index.html
apachectl restartnano $PREFIX/share/apache2/default-site/htdocs/index.html
nano $PREFIX/share/apache2/default-site/htdocs/index.html
pkg update && pkg upgrade
sv-enable apache
apachectl start 
pkg install termux-services
sv-enable apache
apachectl restart
nano $PREFIX/share/apache2/default-site/htdocs/index.html
ping -c 4 google.com
pkg update && pkg upgrade
y
# ضبط اسم المستخدم
git config --global user.name "mz7marko1-lgtm"
# ضبط البريد الإلكتروني
git config --global user.email "mz7marko1@gmail.com"
pkg update
pkg upgrade
Y
pkg update
pkg upgrade
y
pkg install git
pkg update -y
pkg upgrade -y
git config --global user.name "mz7marko1-lgtm"
git config --global user.email "mz7marko1@gmail.com"
git clone https://github.com/mz7marko1-lgtm/my-bot.git
cd my-bot
ls
# تحديث المستودعات وتثبيت بايثون
pkg update && pkg upgrade
Y
mkdir my_bot
cd my_bot
touch bot.py
nano bot.py
python bot.py
termux-setup-storage
nano bot.py
python bot.py
nano bot.py
nano.bot
cd /path/to/your/bot/folder
python bot.py
pkg install clang make -y
git clone https://github.com/ggerganov/whisper.cpp.git && cd whisper.cpp && make
bash ./models/download-ggml-model.sh base
termux-setup-storage
cp "/sdcard/Download/THE GODFATHER _ Learn English with Mafia Movies(360P).mp4.mp4" ./video.mp4
ffmpeg -i video.mp4 -ar 16000 -ac 1 -c:a pcm_s16le input.wav
pkg install ffmpeg -y
cp /sdcard/Download/THE*GODFATHER*.mp4 ./video.mp4
ls /sdcard/Download/
find /sdcard/ -name "*Godfather*" -type f
ls /sdcard/Download/
cp "/sdcard/Download/THE GODFATHER _ Learn English with Mafia Movies(360P).mp4" ./video.mp4
ffmpeg -i video.mp4 -ar 16000 -ac 1 -c:a pcm_s16le input.wav
./build/bin/whisper-cli -m models/ggml-base.bin -f input.wav -osrt
./main -m models/ggml-base.bin -f input.wav -osrt
./whisper-cli -m models/ggml-base.bin -f input.wav -osrt
find . -type f -name "*whisper*"
make
pkg install cmake -y
make
./build/bin/main -m models/ggml-base.bin -f input.wav -osrt
./build/bin/whisper-cli -m models/ggml-base.bin -f input.wav -osrt
termux-setup-storage
cp input.wav.srt ~/storage/downloads/
pkg install python -y && pip install deep-translator srt
cat << 'EOF' > translate.py
import srt
from deep_translator import GoogleTranslator

translator = GoogleTranslator(source='en', target='ar')

print("جاري الترجمة إلى العربية، انتظر قليلاً...")

try:
    with open("input.wav.srt", "r", encoding="utf-8") as f:
        subtitles = list(srt.parse(f.read()))

    total = len(subtitles)
    for i, sub in enumerate(subtitles, 1):
        if sub.content.strip():
            try:
                sub.content = translator.translate(sub.content)
            except Exception:
                pass
        print(f"تم ترجمة {i} من {total}", end="\r")

    with open("arabic.srt", "w", encoding="utf-8") as f:
        f.write(srt.compose(subtitles))

    print("\nتمت الترجمة بنجاح! تم إنشاء الملف: arabic.srt")

except Exception as e:
    print(f"\nحدث خطأ: {e}")
EOF

python translate.py
cp arabic.srt ~/storage/downloads/
pip install srt deep-translator
cat << 'EOF' > translate.py
import urllib.request
import urllib.parse
import json
import re

def translate_text(text):
    if not text.strip():
        return text
    url = "https://translate.googleapis.com/translate_a/single?client=gtx&sl=auto&tl=ar&dt=t&q=" + urllib.parse.quote(text)
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as response:
            res = json.loads(response.read().decode('utf-8'))
            return "".join([item[0] for item in res[0] if item[0]])
    except Exception:
        return text

print("جاري الترجمة إلى العربية، انتظر لحظات...")

try:
    with open("input.wav.srt", "r", encoding="utf-8") as f:
        content = f.read().replace('\r\n', '\n')

    blocks = re.split(r'\n\n+', content.strip())
    translated_blocks = []
    total = len(blocks)

    for i, block in enumerate(blocks, 1):
        lines = block.split('\n')
        if len(lines) >= 3 and '-->' in lines[1]:
            header = lines[:2]
            text_to_trans = "\n".join(lines[2:])
            translated = translate_text(text_to_trans)
            translated_blocks.append("\n".join(header) + "\n" + translated)
        elif len(lines) == 2 and '-->' in lines[0]:
            header = [lines[0]]
            text_to_trans = "\n".join(lines[1:])
            translated = translate_text(text_to_trans)
            translated_blocks.append("\n".join(header) + "\n" + translated)
        else:
            translated_blocks.append(block)

        print(f"تم ترجمة المقطع {i} من {total}", end="\r")

    with open("arabic.srt", "w", encoding="utf-8") as f:
        f.write("\n\n".join(translated_blocks))

    print("\nتمت الترجمة بنجاح! تم إنشاء الملف: arabic.srt")

except Exception as e:
    print(f"\nحدث خطأ: {e}")
EOF

python translate.py
cp arabic.srt ~/storage/downloads/
ls arabic.srt
cp arabic.srt /sdcard/Download/
nano create_subtitle.py
python create_subtitle.py
nano generator.py
python generator.py
nano auto_srt.sh
#!/bin/bash
# التأكد من وجود اسم ملف الفيديو
if [ -z "$1" ]; then   echo "الرجاء تحديد اسم ملف الفيديو. مثال: ./auto_srt.sh video.mp4";   exit 1; fi
chmod +x auto_srt.sh
./auto_srt.sh "Bassem Youssef on Jon Stewart _ 2022 Mark Twain Prize(720P_HD).mp4"
termux-setup-storage
cp /storage/emulated/0/snaptube/download/"SnapTube Video/Bassem Youssef on Jon Stewart _ 2022 Mark Twain Prize(720P_HD).mp4" ./video.mp4
find /storage/emulated/0/ -name "*.mp4" 2>/dev/null | grep -i "Bassem" | head -n 1 | xargs -I {} cp "{}" ./video.mp4
ls -l video.mp4
whisper video.mp4 --model tiny --output_format srt
pip install --upgrade pip
pip install openai-whisper
python -m whisper video.mp4 --model tiny --output_format srt
pkg update && pkg install python python-pip ffmpeg -y
termux-change-repo
pkg install python ffmpeg -y
pip install --upgrade pip
pip install openai-whisper
whisper video.mp4 --model tiny --output_format srt
pkg reinstall python-pip -y
python -m whisper video.mp4 --model tiny --output_format srt
python -m pip install openai-whisper
pkg install clang make cmake python-dev libffi-openssl -y
python -m pip install --upgrade pip setuptools wheel
python -m pip install numpy
