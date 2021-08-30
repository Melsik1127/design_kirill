import telebot
from telebot import types
from time import sleep
import sqlite3


bot = telebot.TeleBot("1995557521:AAEfIvCa9YxYDaGIZ-H_lScod2iTnaF5YNc")


#command - start
@bot.message_handler(commands=['start'])
def start(message):
    global user_name
    bot.send_message(message.chat.id, "3️⃣...")
    sleep(0.5)
    bot.send_message(message.chat.id, "2️⃣...")
    sleep(0.5)
    bot.send_message(message.chat.id, "1️⃣...")
    sleep(0.5)

    #buttons
    markup = types.InlineKeyboardMarkup()
    but1 = types.InlineKeyboardButton("Принять звонок", callback_data="accept_bell")
    markup.add(but1)

    user_name = message.from_user.first_name
    bot.send_video(message.chat.id, open("img/gifs/1.gif", "rb"), reply_markup=markup)

#реакция на кнопки
@bot.callback_query_handler(func=lambda call: True)
def data(call):
    if call.message:
        if call.data == "accept_bell":
            markup = types.InlineKeyboardMarkup()
            but1 = types.InlineKeyboardButton("Продолжить", callback_data="continue")
            markup.add(but1)

            bot.send_video(call.message.chat.id, open("img/gifs/2.gif", "rb"), caption="""
🔥 ДОБРО ПОЖАЛОВАТЬ, {user}, в мир где нет конкуренции, а есть ты и твои клиенты 

Данный бот поможет найти тебе их с помощью уникального встроеного интелекта, а далее ты просто обретешь мощное сарафанное радио и у тебя появятся целых два источника доходов

💰 Бот который находит клиентов 
💰 Сарафанное радио 

Жми кнопку “Продолжить” и следуй указателям 👇🏻""".format(user=user_name), reply_markup=markup)
        if call.data == "continue":
            markup = types.InlineKeyboardMarkup(row_width=2)
            but1 = types.InlineKeyboardButton("Дизайнер", callback_data="choice_1")
            but2 = types.InlineKeyboardButton("Таргетолог/SMM", callback_data="choice_2")
            but3 = types.InlineKeyboardButton("Маркетолог", callback_data="choice_3")
            but4 = types.InlineKeyboardButton("IT-Специалист", callback_data="choice_4")
            but5 = types.InlineKeyboardButton("Дргугой вид деятельности", callback_data="choice_5")
            markup.add(but1, but2, but3, but4, but5)

            bot.send_video(call.message.chat.id, open("img/gifs/6.gif", "rb"), caption="""
🎉 Браво! Двигаешься в правильном направлении

Прежде чем начать, хочу узнать кто ты из спецов?

Выбери свою роль 👇🏻 """, reply_markup=markup)
        if "choice" in call.data:
            bot.send_video(call.message.chat.id, open("img/gifs/3.gif", "rb"), caption="""
🎉 Супер! Нам с тобой по пути

Перед тем, как я запущу тебе функцию по поиску клиентов, давай проверим твою подписку на главного бота @medesignbot""")
            
            connect = sqlite3.connect("users.db")
            cursor = connect.cursor()
            user_id = [call.message.chat.id]
            cursor.execute("SELECT full_version FROM users WHERE id = (?);", user_id)
            result = cursor.fetchall()
            result = str(result).replace("[(", "")
            result = str(result).replace(",)]", "")
            


            sleep(3)
            bot.send_message(call.message.chat.id, "3️⃣...")
            sleep(0.5)
            bot.send_message(call.message.chat.id, "2️⃣...")
            sleep(0.5)
            bot.send_message(call.message.chat.id, "1️⃣...")
            sleep(0.5)
            
            if result == "0":
                markup = types.InlineKeyboardMarkup(row_width=1)
                butt_1 = types.InlineKeyboardButton("🌘 3 месяца", callback_data="month_3")
                butt_2 = types.InlineKeyboardButton("🌗 6 месяцев", callback_data="month_6")
                butt_3 = types.InlineKeyboardButton("🌕 12 месяцев", callback_data="month12")
                markup.add(butt_1, butt_2, butt_3)

                bot.send_video(call.message.chat.id, open("img/gifs/4.gif", "rb"), caption="""
⛔ Так, так...

У тебя нет подписки, чтобы пользоваться моими функциями

Может, она истекла или ты не приобрел ее?

👾 Давай исправим это!""", reply_markup=markup)
            if result == "1":
                markup = types.InlineKeyboardMarkup(row_width=1)
                butt_1 = types.InlineKeyboardButton("🔍 Найти клиента", callback_data="find_client")
                butt_2 = types.InlineKeyboardButton("💬 Как пользоваться?", callback_data="how_to_use")
                markup.add(butt_1, butt_2)

                bot.send_video(call.message.chat.id, open("img/gifs/5.gif", "rb"), caption="""
🎉 Супер! Твоя подписка активна

✅ Функция поиска клиента разблокирована

Можешь спокойно приступить к поиску""", reply_markup=markup)








bot.polling()