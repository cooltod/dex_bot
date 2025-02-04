import telebot
import os

# Environment variable से टोकन प्राप्त करें
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("Error: TELEGRAM_BOT_TOKEN सेट नहीं है। कृपया इसे पहले सेट करें।")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello! मैं आपका Dex Bot हूँ।")

bot.polling()
