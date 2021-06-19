from sqlite3.dbapi2 import Cursor
import telebot
from time import sleep 
import sqlite3
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove

#variables
#1837012196:AAFNjaGSaiUt_u2fXV4dtsHshHjOJUYXUy4

TOKEN = "1600740144:AAFpFngQxwH528CPMaZXPG_X-qmvvCgHjM4"
bot = telebot.TeleBot(TOKEN)

#cursor.execute("""UPDATE users SET full_version = True WHERE id = 846352856""")
#cursor.execute("""SELECT full_version FROM users WHERE id = 846352856""")
#result = cursor.fetchall()

@bot.message_handler(commands=['start'])
def begin(message):
    #добавляю пользователя в бд (id, есть ли полная версия, есть ли пробный период)
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

        user_id = [message.chat.id, False, True, "0"]
        cursor.execute("INSERT INTO users VALUES(?,?,?,?);", (user_id))
        connect.commit()
    except:
        pass
    
    #проверка на полную/пробную версию
    connect = sqlite3.connect("users.db")
    cursor = connect.cursor()
    user_id = [message.chat.id]
    cursor.execute("SELECT full_version FROM users WHERE id = (?);", user_id)
    result = cursor.fetchall()
    result = str(result).replace("[(", "")
    result = str(result).replace(",)]", "")
    result_1 = result

    cursor.execute("SELECT trial_version FROM users WHERE id = (?);", user_id)
    result = cursor.fetchall()
    result = str(result).replace("[(", "")
    result = str(result).replace(",)]", "")
    result_2 = result
    
    if result_1 == "1":
        start_result = "Функции разблокированы:\n✅ Функция запроса файла с сайтов UI8.net, <a href = 'https://craftwork.design'>craftwork</a>, ls.graphics, <a href = 'https://www.freepik.com/profile/preagreement/getstarted'>freepik premium</a>"
    if result_1 == "0" and result_2 == "1":
        start_result = "Функции разблокированы:\n✅ Функция запроса файла с сайта ui8.net (пробная версия)"
    if result_1 == "0" and result_2 == "0":
        start_result = ""

    #replykeyboard клавиши
    inlineKeyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard = True)
    inlineKeyboard.row("Запросить файл")
    inlineKeyboard.row("Подробности")
    inlineKeyboard.row("Полный доступ")

    

    bot.send_message(message.chat.id, start_result + """
    
Наш бот предоставляет безлимитный доступ к сайтам UI8.net, <a href = 'https://craftwork.design'>craftwork</a>, ls.graphics, <a href = 'https://www.freepik.com/profile/preagreement/getstarted'>freepik premium</a> и экономит ваше время и ваши деньги

💫 С помощью нашего бота можно скачивать любые файлы, которые есть на сайте: шрифты, иконки, иллюстрации, UI-киты, мокапы и многое другое. 

🚀 Благодаря регулярным обновлениям файлов и постоянным улучшениям, бот успешно работает уже более года. Сотни пользователей, ежедневно скачивают тысячи файлов через нашего бота

""", reply_markup=inlineKeyboard, parse_mode='html', disable_web_page_preview = True)

@bot.message_handler(commands=['add_link'])
def add_link(message):
    #добавление ссылок
    
    if message.chat.id == 846352856 or message.chat.id == 646741803:
        global msg
        global rules_true
        rules_true = True
        markup = InlineKeyboardMarkup(row_width=1)
        but_1 = InlineKeyboardButton("⬅️Назад", callback_data="del_last_message")
        markup.add(but_1)
        msg = bot.send_message(message.chat.id, "Введите ссылку на платный файл и ссылку на скачивание файла. Пример:\n https://ui8.net/ui8/products/bento-matte-3d https://drive.google.com/file/d/1czlS1Ek2FNbt2wb3K2weedJ8drb61gOI/view?usp=sharing", disable_web_page_preview=True, reply_markup=markup)
        bot.register_next_step_handler(msg, add_href)
    else:
        rules_true = False
        bot.send_message(message.chat.id, "У вас нету доступа!")

@bot.message_handler(commands=['remove_link'])
def remove_link(message):
    #удаление ссылок
    if message.chat.id == 846352856 or message.chat.id == 646741803:
        global msg
        global rules_true
        rules_true = True
        markup = InlineKeyboardMarkup(row_width=1)
        but_1 = InlineKeyboardButton("⬅️Назад", callback_data="del_last_message")
        markup.add(but_1)
        msg = bot.send_message(message.chat.id, "Введите ссылку на платный файл. Пример:\n https://ui8.net/ui8/products/bento-matte-3d", disable_web_page_preview=True, reply_markup=markup)
        bot.register_next_step_handler(msg, remove_href)
    else:
        rules_true = False
        bot.send_message(message.chat.id, "У вас нету доступа!")

@bot.message_handler(content_types=['text'])
def text(message):
    print("text")
    
    #Запросить файл 1
    if message.text == "Запросить файл":
        global rules_true
        rules_true = True
        markup = InlineKeyboardMarkup(row_width=1)
        but_1 = InlineKeyboardButton("⬅️Назад", callback_data="start_2")
        markup.add(but_1)
        msg = bot.send_message(message.chat.id,text = """
🎁 Запросить файл

Пришли ссылку на нужный материал и бот отправит ссылку на файл для скачивания.""", reply_markup=markup)
        bot.register_next_step_handler(msg, find_file)
    #Подробности 1
    if message.text == "Подробности":
        markup = InlineKeyboardMarkup(row_width=1)
        but_1 = InlineKeyboardButton("⬅️Назад", callback_data="start_2")
        markup.add(but_1)
        bot.send_message(message.chat.id, text = """что либо, для заполнения и проверки работоспособности кнопки""", reply_markup=markup)
    #Полный доступ 1
    if message.text == "Полный доступ":
        inlineKeyboard = InlineKeyboardMarkup(row_width=1)
        butt_1 = InlineKeyboardButton("🌕6 месяцев", callback_data="month_6")
        butt_2 = InlineKeyboardButton("🌕12 месяцев", callback_data="month_12")
        butt_3 = InlineKeyboardButton("⬅️Назад", callback_data="start_2")
        inlineKeyboard.add(butt_1, butt_2, butt_3)

        bot.send_message(message.chat.id, text = """
💎 Доступ к боту


После успешной оплаты, ты моментально получаешь безлимитный доступ к боту с тысячам качественных ресурсов, созданных профессиональными дизайнерами. Общая стоимость всех ресурсов на сайте превышает 150,000$! а также к другим функциям бота

Доступ на данный момент возможен сразу на целый год 🌕 12 месяцев. т.к дается заказ на сумму тарифа + У нас нет ограничений на загрузки, в отличие от сайта.
Выбери данный тариф нажав на его""", reply_markup=inlineKeyboard)

#вторая часть активации, 6 месяцев
def activate_6_month(message):
    print("activate_6_month")
    inlineKeyboard = InlineKeyboardMarkup(row_width=1)
    butt_1 = InlineKeyboardButton("⬅️Назад", callback_data="month_6")
    inlineKeyboard.add(butt_1)

    f = open('month_6.txt', 'r', encoding='utf-8')
    line = f.readline()
    nn = False
    for line in f:
        if message.text == line.replace("\n",""):
            nn = True
            connect = sqlite3.connect("users.db")
            cursor = connect.cursor()
            user = message.chat.id
            cursor.execute("UPDATE users SET full_version = True WHERE id = (?)", (user, ))
            connect.commit()
            bot.send_message(message.chat.id, "✅Поздравляю! Теперь у вас есть полный доступ", reply_markup=inlineKeyboard)
    if nn == False:
        bot.send_message(message.chat.id, "❌Упс.. Это неверный ключ", reply_markup=inlineKeyboard)
    f.close()

#вторая часть поиска ссылки
def find_file(message):
    print("find_file")
    global rules_true
    if rules_true == True:
        rules_true = False
    
        #достаем данные о полной/пробной версии
        connect = sqlite3.connect("users.db")
        cursor = connect.cursor()
        user_id = [message.chat.id]
        cursor.execute("SELECT full_version FROM users WHERE id = (?);", user_id)
        result = cursor.fetchall()
        result = str(result).replace("[(", "")
        result = str(result).replace(",)]", "")
        result_1 = result

        cursor.execute("SELECT trial_version FROM users WHERE id = (?);", user_id)
        result = cursor.fetchall()
        result = str(result).replace("[(", "")
        result = str(result).replace(",)]", "")
        result_2 = result

        if result_1 == "0" and result_2 == "0":
            markup = InlineKeyboardMarkup(row_width=1)
            butt_1 = InlineKeyboardButton("Полный доступ", callback_data="btn3")
            butt_2 = InlineKeyboardButton("⬅️Назад", callback_data="start_2")
            markup.add(butt_1, butt_2)
            bot.send_message(message.chat.id, "У вас больше нету бесплатных попыток😞\nКупите полный доступ, чтобы иметь доступ ко всем платным данным:", reply_markup=markup)
        else:
            #достаем ссылки из таблицы
            try:
                connect = sqlite3.connect("links.db")
                cursor = connect.cursor()
                link = [message.text]
                cursor.execute("SELECT free FROM links WHERE paid = (?);", link)
                result = cursor.fetchall()
                result = str(result).replace("[(", "")
                result = str(result).replace(",)]", "")

                inlineKeyboard = InlineKeyboardMarkup(row_width=1)
                butt_1 = InlineKeyboardButton("⬅️Назад", callback_data="start_2")
                inlineKeyboard.add(butt_1)
                
                result_text = "Вот ваша ссылка:\n<a href={res}>файл</a>📄".format(res = result)
                bot.send_message(message.chat.id, result_text, parse_mode="html", reply_markup=inlineKeyboard)
                if result_2 == "1":
                    connect = sqlite3.connect("users.db")
                    cursor = connect.cursor()
                    user = message.chat.id
                    cursor.execute("UPDATE users SET trial_version = False WHERE id = (?)", (user, ))
                    connect.commit()
            except:
                inlineKeyboard = InlineKeyboardMarkup(row_width=1)
                butt_1 = InlineKeyboardButton("⬅️Назад", callback_data="start_2")
                inlineKeyboard.add(butt_1)
                bot.send_message(message.chat.id, "Увы, похоже в нашей базе нету этой ссылки😔", reply_markup=inlineKeyboard)
    else:
        text(message)
#вторая часть remove_link, удаление ссылок
def remove_href(message):
    print("remove_href")
    global rules_true
    if rules_true == True:
        rules_true = False
        try:
            href = message.text
            connect = sqlite3.connect("links.db")
            cursor = connect.cursor()

            cursor.execute('SELECT paid FROM links WHERE paid = (?)', (href, ))
            result = cursor.fetchall()
            if result == []:
                bot.send_message(message.chat.id, "Упс.. похоже, такой ссылки нету в моей базе")
            else:
                cursor.execute('DELETE FROM links WHERE paid = (?)', (href, ))
                connect.commit()
                bot.send_message(message.chat.id, "Ссылка успешно удалена из списка")
        except:
            bot.send_message(message.chat.id, "Упс.. похоже, такой ссылки нету в моей базе")
    else:
        text(message)
#вторая часть add_link, добавление ссылок
def add_href(message):
    print("add_href")
    global rules_true
    if rules_true == True:
        rules_true = False
        try:
            all_links = message.text.split(" ")
            connect = sqlite3.connect("links.db")
            cursor = connect.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS links(
                paid TEXT,
                free TEXT
            );

            """)

            write = [all_links[0], all_links[1]]
            cursor.execute("INSERT INTO links VALUES(?,?);", (write))
            connect.commit()
            bot.send_message(message.chat.id, "Ссылка успешно добавлена")
        except:
            bot.send_message(message.chat.id, "Упс.. похоже, вы неправильно ввели ссылки")
    else:
        text(message)
@bot.callback_query_handler(func=lambda call: True)
def data(call):
    global rules_true
    if call.message:
        if call.data == "del_last_message":
            bot.delete_message(call.message.chat.id, msg.message_id )
            rules_true = False
        #переход на start
        if call.data == "start_2":
            rules_true = False
            begin(call.message)

        #Подробности 2
        if call.data == "btn2":
            markup = InlineKeyboardMarkup(row_width=1)
            but_1 = InlineKeyboardButton("⬅️Назад", callback_data="start_2")
            markup.add(but_1)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text = """что либо, для заполнения и проверки работоспособности кнопки""", reply_markup=markup)

        #Полный доступ 2
        if call.data == "btn3":
            inlineKeyboard = InlineKeyboardMarkup(row_width=1)
            butt_1 = InlineKeyboardButton("🌕6 месяцев", callback_data="month_6")
            butt_2 = InlineKeyboardButton("🌕12 месяцев", callback_data="month_12")
            butt_3 = InlineKeyboardButton("⬅️Назад", callback_data="start_2")
            inlineKeyboard.add(butt_1, butt_2, butt_3)

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text = """
💎 Доступ к боту


После успешной оплаты, ты моментально получаешь безлимитный доступ к боту с тысячам качественных ресурсов, созданных профессиональными дизайнерами. Общая стоимость всех ресурсов на сайте превышает 150,000$! а также к другим функциям бота

Доступ на данный момент возможен сразу на целый год 🌕 12 месяцев. т.к дается заказ на сумму тарифа + У нас нет ограничений на загрузки, в отличие от сайта.
Выбери данный тариф нажав на его""", reply_markup=inlineKeyboard)
        #тариф - 12 месяцев
        if call.data == "month_12":

            inlineKeyboard = InlineKeyboardMarkup(row_width=2)
            butt_1 = InlineKeyboardButton("💸Оплатить", callback_data="buy")
            butt_2 = InlineKeyboardButton("🏷Промокод", callback_data="promocode")
            butt_3 = InlineKeyboardButton("⬅️Назад", callback_data="btn3")
            inlineKeyboard.row(butt_1)
            inlineKeyboard.row(butt_2, butt_3)

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text = """
Полный доступ к боту на 🌕 12 месяцев

После оплаты доступ к боту и к его функциям будет открыт моментально. Оплата возможна любым удобным способом.

💸 Стоимость: 1499₽ (это всего ~125₽ в месяц)
        """, reply_markup=inlineKeyboard)
        

        #тариф - 6 месяцев
        if call.data == "month_6":

            inlineKeyboard = InlineKeyboardMarkup(row_width=2)
            butt_1 = InlineKeyboardButton("💸Оплатить", callback_data="buy_2")
            butt_2 = InlineKeyboardButton("🏷Промокод", callback_data="promocode")
            butt_3 = InlineKeyboardButton("⬅️Назад", callback_data="btn3")
            inlineKeyboard.row(butt_1)
            inlineKeyboard.row(butt_2, butt_3)

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text = """
Полный доступ к боту на 🌕 6 месяцев

После оплаты доступ к боту и к его функциям будет открыт моментально. Оплата возможна любым удобным способом.

💸 Стоимость: 990₽ (это всего ~165₽ в месяц)
        """, reply_markup=inlineKeyboard)
        #чем оплачивать?
        if call.data == "buy":
            #connect = sqlite3.connect("users.db")
            #cursor = connect.cursor()
            #user = call.message.chat.id
            #cursor.execute("UPDATE users SET full_version = True WHERE id = (?)", (user, ))
            #connect.commit()
            inlineKeyboard = InlineKeyboardMarkup(row_width=1)
            butt_1 = InlineKeyboardButton("🔑Активировать тариф", callback_data="activate")
            butt_2 = InlineKeyboardButton("⬅️Назад", callback_data="month_12")

            inlineKeyboard.row(butt_1)
            inlineKeyboard.row(butt_2)
            

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text = """
<b>Выберите способ оплаты подписки</b>
🏦 Доступные способы оплаты
    ├ Банковской картой
    ├ Электронным кошельком (Qiwi, YooMoney и тд.)

Подписка будет активирована моментально после оплаты.

<b>Вам нужен ключ, для его покупки перейдите на <a href='тут пока ничего нету ;)'>сайт</a></b>
        """, reply_markup=inlineKeyboard, parse_mode="html")

        if call.data == "buy_2":
            #connect = sqlite3.connect("users.db")
            #cursor = connect.cursor()
            #user = call.message.chat.id
            #cursor.execute("UPDATE users SET full_version = True WHERE id = (?)", (user, ))
            #connect.commit()
            inlineKeyboard = InlineKeyboardMarkup(row_width=1)
            butt_1 = InlineKeyboardButton("🔑Активировать тариф", callback_data="activate_2")
            butt_2 = InlineKeyboardButton("⬅️Назад", callback_data="month_6")

            inlineKeyboard.row(butt_1)
            inlineKeyboard.row(butt_2)
            

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text = """
<b>Выберите способ оплаты подписки</b>
🏦 Доступные способы оплаты
    ├ Банковской картой
    ├ Электронным кошельком (Qiwi, YooMoney и тд.)

Подписка будет активирована моментально после оплаты.

<b>Вам нужен ключ, для его покупки перейдите на <a href='https://www.digiseller.market/asp2/pay_wm.asp?id_d=3167666&lang=ru-RU'>сайт</a></b>
        """, reply_markup=inlineKeyboard, parse_mode="html")
        
        #активация ключа
        if call.data == "activate_2":
            

            msg = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text = "Отправь сюда свой код активации")
            bot.register_next_step_handler(msg, activate_6_month)

        #промокод
        if call.data == "promocode":
            inlineKeyboard = InlineKeyboardMarkup(row_width=2)
            butt_1 = InlineKeyboardButton("⬅️Назад", callback_data="month_12")
            inlineKeyboard.row(butt_1)

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text = "Просто текст", reply_markup=inlineKeyboard)
        
        #оплата картой
        if call.data == "buy_card":
            inlineKeyboard = InlineKeyboardMarkup(row_width=2)
            butt_1 = InlineKeyboardButton("Apple Pay", callback_data="apple_card")
            butt_2 = InlineKeyboardButton("Samsung Pay", callback_data="samsung_card")
            butt_3 = InlineKeyboardButton("Банковская карта", callback_data="bank_card")
            butt_4 = InlineKeyboardButton("⬅️Назад", callback_data="buy")
            inlineKeyboard.row(butt_1,butt_2)
            inlineKeyboard.row(butt_3,butt_4)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text = """
<b>Выберите способ оплаты подписки</b>""", reply_markup=inlineKeyboard, parse_mode="html")

        #оплата электр. кошельком
        if call.data == "buy_wallet":
            inlineKeyboard = InlineKeyboardMarkup(row_width=2)
            butt_1 = InlineKeyboardButton("Qiwi", callback_data="qiwi")
            butt_2 = InlineKeyboardButton("YooMoney", callback_data="yoomoney")
            butt_3 = InlineKeyboardButton("⬅️Назад", callback_data="buy")
            inlineKeyboard.row(butt_1,butt_2)
            inlineKeyboard.row(butt_3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text = """
<b>Выберите способ оплаты подписки</b>""", reply_markup=inlineKeyboard, parse_mode="html")
bot.polling()