import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8373911799:AAEMlCODHsIeGA-qa8zMTFFbUx4pYYTaGnM"

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🚀 Shield VPN бот работает!\n\nОтправь /vpn")

async def vpn(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔐 VPN ключ будет доступен после оплаты.\n\n💰 Стоимость: 299 руб/мес")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("vpn", vpn))
    print("✅ Бот запущен!")
    app.run_polling()

if __name__ == "__main__":
    main()
