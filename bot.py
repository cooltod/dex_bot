import telebot

bot = telebot.TeleBot('7418276051:AAFB0EZPolVLTmXkQ7jiSKJzkSXsDrBsVjM')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello! I am your Dex Bot.")

bot.polling()