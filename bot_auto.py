import asyncio
from telethon import TelegramClient

# بياناتك الصحيحة المستخرجة من الحساب
api_id = 31870445
api_hash = 'db14632ca56e125f5260c3845622328c'

# معرف البوت الصحيح والنهائي
bot_username = 'Sudaniotpbot' 

client = TelegramClient('session_automation', api_id, api_hash)

async def main():
    print("🤖 جاري بدء الاتصال بحسابك التليجرام...")
    await client.send_message(bot_username, '/start')
    
    # انتظار رد البوت بالقائمة الأولى
    await asyncio.sleep(5)
    
    async for message in client.iter_messages(bot_username, limit=1):
        if message.buttons:
            print("🔄 جاري الضغط التلقائي على (تحديث البيانات)...")
            await message.click(0)  # يضغط على تحديث البيانات
            
    # انتظار 10 ثوانٍ حتى يقوم البوت بإرسال الكود وتحديث النقاط بنجاح
    print("⏳ انتظار معالجة البوت وتحديث كود التحقق...")
    await asyncio.sleep(10)
    
    async for message in client.iter_messages(bot_username, limit=1):
        if message.buttons:
            # البحث عن زر "أخذ النقاط للكل" والضغط عليه تلقائياً
            for row in message.buttons:
                for button in row:
                    if "أخذ النقاط" in button.text or "للكل" in button.text:
                        print(f"🔘 تم العثور على زر [{button.text}]، جاري سحب النقاط تلقائياً...")
                        await button.click()
                        await asyncio.sleep(3)
                        break
    
    print("✅ تم التحديث وسحب جميع النقاط بنجاح باهر دون تدخل منك!")

with client:
    client.loop.run_until_complete(main())
