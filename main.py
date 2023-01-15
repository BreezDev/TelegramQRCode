import telebot
import pyqrcode
from telebot import types

bot = telebot.TeleBot("YOUR_BOT_TOKEN")

@bot.message_handler(commands=['qr'])
def qr_code(message):
    link = message.text[4:]
    qr = pyqrcode.create(link)
    qr.png('qr.png', scale=6)
    with open('qr.png', 'rb') as f:
        bot.send_photo(message.chat.id, f)

bot.polling()
