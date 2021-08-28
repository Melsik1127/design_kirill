import telebot
from telebot import types
from time import sleep


bot = telebot.TeleBot("1995557521:AAEfIvCa9YxYDaGIZ-H_lScod2iTnaF5YNc")


#command - start
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "3️⃣..")
    sleep(0.5)
    bot.send_message(message.chat.id, "2️⃣..")
    sleep(0.5)
    bot.send_message(message.chat.id, "1️⃣..")
    sleep(0.5)

    #buttons
    markup = types.InlineKeyboardMarkup()
    but1 = types.InlineKeyboardButton("Принять звонок", callback_data="accept_bell")
    markup.add(but1)


    bot.send_document(message.chat.id, open("img/1.gif", "rb"), reply_markup=markup)




bot.polling()