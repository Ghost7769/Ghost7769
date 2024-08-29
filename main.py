import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# استبدل 'YOUR_TOKEN' بالرمز الخاص بالبوت
TOKEN = '7043561215:AAE0fKitdHW6hSomR4nH0Be81XRiaodnaNo'

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('مرحبا! أنا بوت تليجرام.')

async def help_command(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('هذه قائمة الأوامر المتاحة:\n/start - بدء البوت\n/help - مساعدة\n/myip - عرض عنوان IP العام')

async def my_ip(update: Update, context: CallbackContext) -> None:
    try:
        # طلب عنوان IP العام باستخدام ipify API
        response = requests.get('https://api.ipify.org?format=json')
        ip_info = response.json()
        ip_address = ip_info['ip']
        await update.message.reply_text(f'عنوان IP العام لجهازك هو: {ip_address}')
    except requests.RequestException as e:
        await update.message.reply_text(f'حدث خطأ أثناء محاولة الحصول على عنوان IP: {e}')

def main() -> None:
    application = Application.builder().token(TOKEN).build()

    # تسجيل الأوامر
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('help', help_command))
    application.add_handler(CommandHandler('myip', my_ip))

    # بدء تشغيل البوت
    application.run_polling()

if __name__ == '__main__':
    main()