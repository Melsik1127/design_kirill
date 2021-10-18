import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from time import sleep
import sqlite3
from telebot import apihelper

apihelper.proxy = {"https": "socks5://143.198.237.236"}

print(sqlite3.sqlite_version)


bot = telebot.TeleBot("1995557521:AAEfIvCa9YxYDaGIZ-H_lScod2iTnaF5YNc")


#command - start
@bot.message_handler(commands=['start'])
def start(message):

    try:
        connect = sqlite3.connect("users.db")
        cursor = connect.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS users(
            id INT PRIMARY KEY,
            full_version BOOLEAN,
            trial_version BOOLEAN,
            date TEXT
        );

        """)

        user_id = [message.chat.id, "0", "1", "0"]
        cursor.execute("INSERT INTO users VALUES(?,?,?,?);", (user_id))
        connect.commit()
    except:
        pass

    global user_name
    bot.send_message(message.chat.id, "3️⃣...")
    sleep(0.5)
    bot.send_message(message.chat.id, "2️⃣...")
    sleep(0.5)
    bot.send_message(message.chat.id, "1️⃣...")
    sleep(0.5)

    #buttons
    markup = InlineKeyboardMarkup()
    but1 = InlineKeyboardButton("Принять звонок", callback_data="accept_bell")
    markup.add(but1)

    user_name = message.from_user.first_name
    bot.send_video(message.chat.id, open("img/gifs/1.gif", "rb"), reply_markup=markup)

#text
@bot.message_handler(content_types=["text"])
def text(message):
    pass
def activate_6_month(message):
    print("activate_6_month")
    inlineKeyboard = InlineKeyboardMarkup(row_width=1)
    butt_1 = InlineKeyboardButton("⬅️Назад", callback_data="month_6")
    inlineKeyboard.add(butt_1)

    f = open('month_6.txt', 'r', encoding='utf-8')
    line = f.readline()
    key_found = False
    for line in f:
        line = line.replace("\n","")
        if message.text == line:
            key_found = True
            connect = sqlite3.connect("users.db")
            cursor = connect.cursor()
            user = message.chat.id
            cursor.execute("UPDATE users SET full_version = '1' WHERE id = (?)", (user, ))
            connect.commit()
            bot.send_message(message.chat.id, "✅Поздравляю! Теперь у вас есть полный доступ", reply_markup=inlineKeyboard)
    if key_found == False:
        bot.send_message(message.chat.id, "❌Упс.. Это неверный ключ", reply_markup=inlineKeyboard)
    f.close()



#реакция на кнопки
@bot.callback_query_handler(func=lambda call: True)
def data(call):
    if call.message:
        if call.data == "accept_bell":
            markup = InlineKeyboardMarkup()
            but1 = InlineKeyboardButton("Продолжить", callback_data="continue")
            markup.add(but1)

            bot.send_video(call.message.chat.id, open("img/gifs/2.gif", "rb"), caption="""
🔥 ДОБРО ПОЖАЛОВАТЬ, {user}, в мир где нет конкуренции, а есть ты и твои клиенты 

Данный бот поможет найти тебе их с помощью уникального встроеного интелекта, а далее ты просто обретешь мощное сарафанное радио и у тебя появятся целых два источника доходов

💰 Бот который находит клиентов 
💰 Сарафанное радио 

Жми кнопку “Продолжить” и следуй указателям 👇🏻""".format(user=user_name), reply_markup=markup)
        if call.data == "continue":
            markup = InlineKeyboardMarkup(row_width=2)
            but1 = InlineKeyboardButton("Дизайнер", callback_data="choice_1")
            but2 = InlineKeyboardButton("Таргетолог/SMM", callback_data="choice_2")
            but3 = InlineKeyboardButton("Маркетолог", callback_data="choice_3")
            but4 = InlineKeyboardButton("IT-Специалист", callback_data="choice_4")
            but5 = InlineKeyboardButton("Дргугой вид деятельности", callback_data="choice_5")
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
                markup = InlineKeyboardMarkup(row_width=1)
                butt_1 = InlineKeyboardButton("🌘 3 месяца", callback_data="month_3")
                butt_2 = InlineKeyboardButton("🌗 6 месяцев", callback_data="month_6")
                butt_3 = InlineKeyboardButton("🌕 12 месяцев", callback_data="month12")
                markup.add(butt_1, butt_2, butt_3)

                bot.send_video(call.message.chat.id, open("img/gifs/4.gif", "rb"), caption="""
⛔ Так, так...

У тебя нет подписки, чтобы пользоваться моими функциями

Может, она истекла или ты не приобрел ее?

👾 Давай исправим это!""", reply_markup=markup)
            if result == "1":
                markup = InlineKeyboardMarkup(row_width=1)
                butt_1 = InlineKeyboardButton("🔍 Найти клиента", callback_data="find_client")
                butt_2 = InlineKeyboardButton("💬 Как пользоваться?", callback_data="how_to_use")
                markup.add(butt_1, butt_2)

                bot.send_video(call.message.chat.id, open("img/gifs/5.gif", "rb"), caption="""
🎉 Супер! Твоя подписка активна

✅ Функция поиска клиента разблокирована

Можешь спокойно приступить к поиску""", reply_markup=markup)
        if call.data == "month_3":
            inlineKeyboard = InlineKeyboardMarkup(row_width=2)
            butt_1 = InlineKeyboardButton("💸Оплатить", callback_data="buy_3")
            butt_2 = InlineKeyboardButton("🏷Промокод", callback_data="promocode_3")
            butt_3 = InlineKeyboardButton("⬅️Назад", callback_data="btn3")
            inlineKeyboard.row(butt_1)
            inlineKeyboard.row(butt_2, butt_3)

            bot.send_photo(chat_id=call.message.chat.id, photo=open("img/6.jpg","rb"), reply_markup=inlineKeyboard, caption= """
Полный доступ к боту на 🌘 3 месяца

После оплаты доступ к боту и к его функциям будет открыт моментально. Оплата возможна любым удобным способом.

💸 Стоимость: 790₽
        """)
        
        if call.data == "btn3":
            inlineKeyboard = InlineKeyboardMarkup(row_width=1)
            butt_1 = InlineKeyboardButton("🌘 3 месяца", callback_data="month_3")
            butt_2 = InlineKeyboardButton("🌗 6 месяцев", callback_data="month_6")
            butt_3 = InlineKeyboardButton("🌕 12 месяцев", callback_data="month_12")
            inlineKeyboard.add(butt_1, butt_2, butt_3)

            bot.send_message(call.message.chat.id, text = """
    💎 Доступ к боту


    После успешной оплаты, вы моментально получаете безлимитный доступ к боту с тысячам качественных ресурсов, созданных профессиональными дизайнерами. Общая стоимость всех ресурсов на сайтах превышает 150,000$!Также будет открыт доступ к другим функциям бота

    Доступ возможен: 
    🌘 На три месяца 
    🌗 На пол года
    🌕 На год
    *При тарифе пол года и год - вам дается клиент для того, чтобы бот обошолся вам в 0 руб.

    👇🏻 Выберите удобный для вас тариф: """, reply_markup=inlineKeyboard)

        if call.data == "month_6":
    
            inlineKeyboard = InlineKeyboardMarkup(row_width=2)
            butt_1 = InlineKeyboardButton("💸Оплатить", callback_data="buy_2")
            butt_2 = InlineKeyboardButton("🏷Промокод", callback_data="promocode_6")
            butt_3 = InlineKeyboardButton("⬅️Назад", callback_data="btn3")
            inlineKeyboard.row(butt_1)
            inlineKeyboard.row(butt_2, butt_3)

            bot.send_photo(chat_id=call.message.chat.id, photo=open("img/5.jpg", "rb"), caption = """
Полный доступ к боту на 🌗 6 месяцев

После оплаты доступ к боту и к его функциям будет открыт моментально. Оплата возможна любым удобным способом.

💸 Стоимость: 990₽ *Экономия 590₽
+Предоставление клиента на сумму тарифа 
        """, reply_markup=inlineKeyboard)


        if call.data == "buy_2":
            #6
            #connect = sqlite3.connect("users.db")
            #cursor = connect.cursor()
            #user = call.message.chat.id
            #cursor.execute("UPDATE users SET full_version = True WHERE id = (?)", (user, ))
            #connect.commit()
            inlineKeyboard = InlineKeyboardMarkup(row_width=1)
            
            butt_1 = InlineKeyboardButton("💳 Оплатить тариф", callback_data="open_payment")
            butt_2 = InlineKeyboardButton("🔑 Активировать ключ", callback_data="activate_2")


            inlineKeyboard.row(butt_1)
            inlineKeyboard.row(butt_2)
            

            bot.send_photo(chat_id=call.message.chat.id, photo=open("img/7.jpg", "rb"), caption = """
Выберите способ оплаты подписки
🏦 Доступные способы оплаты
    ├ Банковской картой
    ├ Электронным кошельком (Qiwi, YooMoney и тд.)

Подписка будет активирована моментально после оплаты.

🔑 Вам нужен ключ
Для его получения перейдите на сайт, совершите оплату тарифа, дождитесь момента пока вас перекинет на страницу с ключом, скопируйте, перейдите в бота и нажмите на кнопку активировать тариф, после втавьте скопированный ключ
        """, reply_markup=inlineKeyboard, parse_mode="html")
        if call.data == "buy_3":
            #3
            #connect = sqlite3.connect("users.db")
            #cursor = connect.cursor()
            #user = call.message.chat.id
            #cursor.execute("UPDATE users SET full_version = True WHERE id = (?)", (user, ))
            #connect.commit()
            inlineKeyboard = InlineKeyboardMarkup(row_width=1)
            
            butt_1 = InlineKeyboardButton("💳 Оплатить тариф", callback_data="open_payment")
            butt_2 = InlineKeyboardButton("🔑 Активировать ключ", callback_data="activate_3")


            inlineKeyboard.row(butt_1)
            inlineKeyboard.row(butt_2)
            

            bot.send_photo(chat_id=call.message.chat.id, photo=open("img/7.jpg", "rb"), caption = """
Выберите способ оплаты подписки
🏦 Доступные способы оплаты
    ├ Банковской картой
    ├ Электронным кошельком (Qiwi, YooMoney и тд.)

Подписка будет активирована моментально после оплаты.

🔑 Вам нужен ключ
Для его получения перейдите на сайт, совершите оплату тарифа, дождитесь момента пока вас перекинет на страницу с ключом, скопируйте, перейдите в бота и нажмите на кнопку активировать тариф, после втавьте скопированный ключ
        """, reply_markup=inlineKeyboard, parse_mode="html")
        
        #активация ключа
        if call.data == "activate_2":
            

            msg = bot.send_message(chat_id=call.message.chat.id, text = "Отправь сюда свой код активации")
            bot.register_next_step_handler(msg, activate_6_month)



        if call.data == "month_12":
    
            inlineKeyboard = InlineKeyboardMarkup(row_width=2)
            butt_1 = InlineKeyboardButton("💸Оплатить", callback_data="buy")
            butt_2 = InlineKeyboardButton("🏷Промокод", callback_data="promocode_12")
            butt_3 = InlineKeyboardButton("⬅️Назад", callback_data="btn3")
            inlineKeyboard.row(butt_1)
            inlineKeyboard.row(butt_2, butt_3)

            bot.send_photo(chat_id=call.message.chat.id, photo=open("img/4.jpg", "rb"), caption = """
Полный доступ к боту на 🌕 12 месяцев

После оплаты доступ к боту и к его функциям будет открыт моментально. Оплата возможна любым удобным способом.

💸 Стоимость: 990₽ *Экономия 590₽
+Предоставление клиента на сумму тарифа 
        """, reply_markup=inlineKeyboard)

        if call.data == "buy":
            inlineKeyboard = InlineKeyboardMarkup(row_width=1)
            
            butt_1 = InlineKeyboardButton("💳 Оплатить тариф", callback_data="open_payment")
            butt_2 = InlineKeyboardButton("🔑 Активировать ключ", callback_data="activate")


            inlineKeyboard.row(butt_1)
            inlineKeyboard.row(butt_2)
            

            bot.send_photo(chat_id=call.message.chat.id, photo=open("img/7.jpg", "rb"), caption = """
Выберите способ оплаты подписки
🏦 Доступные способы оплаты
    ├ Банковской картой
    ├ Электронным кошельком (Qiwi, YooMoney и тд.)

Подписка будет активирована моментально после оплаты.

🔑 Вам нужен ключ
Для его получения перейдите на сайт, совершите оплату тарифа, дождитесь момента пока вас перекинет на страницу с ключом, скопируйте, перейдите в бота и нажмите на кнопку активировать тариф, после втавьте скопированный ключ
        """, reply_markup=inlineKeyboard, parse_mode="html")


        #промокод
        if call.data == "promocode_3":
            inlineKeyboard = InlineKeyboardMarkup(row_width=2)
            butt_1 = InlineKeyboardButton("⬅️Назад", callback_data="month_3")
            inlineKeyboard.row(butt_1)

            bot.send_photo(chat_id=call.message.chat.id, photo=open("img/3.jpg", "rb"), caption="💡 Если вы узнали о данном боте от того, кто продвигает его, для получения заработка и у вас есть определенный промокод, который даст вам скидку на покупку бота, то введите данный промокод ", reply_markup=inlineKeyboard)
        
        if call.data == "promocode_6":
            inlineKeyboard = InlineKeyboardMarkup(row_width=2)
            butt_1 = InlineKeyboardButton("⬅️Назад", callback_data="month_6")
            inlineKeyboard.row(butt_1)

            bot.send_photo(chat_id=call.message.chat.id, photo=open("img/3.jpg", "rb"), caption="💡 Если вы узнали о данном боте от того, кто продвигает его, для получения заработка и у вас есть определенный промокод, который даст вам скидку на покупку бота, то введите данный промокод ", reply_markup=inlineKeyboard)

        if call.data == "promocode_12":
            inlineKeyboard = InlineKeyboardMarkup(row_width=2)
            butt_1 = InlineKeyboardButton("⬅️Назад", callback_data="month_12")
            inlineKeyboard.row(butt_1)

            bot.send_photo(chat_id=call.message.chat.id, photo=open("img/3.jpg", "rb"), caption="💡 Если вы узнали о данном боте от того, кто продвигает его, для получения заработка и у вас есть определенный промокод, который даст вам скидку на покупку бота, то введите данный промокод ", reply_markup=inlineKeyboard)

bot.polling(none_stop=True)
