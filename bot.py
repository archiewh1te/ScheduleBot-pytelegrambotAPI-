import telebot
import config
from telebot import types
from sql import *
import schedule
import time
import threading



bot = telebot.TeleBot(config.TOKEN)

# INFO - menu

@bot.message_handler(commands= ['get_info', 'info'] )
def get_user_info(message):
    markup_inline = types.InlineKeyboardMarkup()
    item_yes = types.InlineKeyboardButton(text = 'да' , callback_data= 'yes')
    item_no = types.InlineKeyboardButton(text = 'нет' , callback_data= 'no')

    markup_inline.add(item_yes, item_no)
    bot.send_message(message.chat.id, ' Желаете узнать инфо о вас ?' ,
              reply_markup= markup_inline
    )

# Кнопки

@bot.callback_query_handler(func= lambda call: True)
def answer(call):
    if call.data == 'yes' :
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item_id = types.KeyboardButton( ' МОЙ ID')
        item_username = types.KeyboardButton ( ' МОЙ НИК')

        markup_reply.add(item_id, item_username)
        bot.send_message(call.message.chat.id, 'Нажмите на одну из конопок',
               reply_markup = markup_reply
)
    elif call.data == 'no' :
        bot.send_message(call.message.chat.id, 'Ну и ладно'),


# Пишем боту Привет и получаем ответ
@bot.message_handler(content_types = ['text'])   # Приветствие!
def start(message):
    if message.text == 'Привет':
         sti = open('welcome.webp', 'rb')
         bot.send_sticker(message.chat.id, sti)
         bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы быть подопытным кроликом.".format(message.from_user, bot.get_me()),
             parse_mode='html')

    elif message.text == 'МОЙ ID':
          bot.send_message(message.chat.id,  f'Ваш ID: {message.from_user.id}')
    elif message.text == 'МОЙ НИК' :
           bot.send_message(message.chat.id,  f'Ваш Ник: {message.from_user.first_name} {message.from_user.last_name}')



def job():                        # Вывод списка из фаила  SQL.PY
     bot.send_message('-1001528572769', f' КЛЮЧИ Квалификационный:\n' + output) # В СКОБКАХ УКАЗЫВАЕТЕ АЙДИ ГРУППЫ КУДА БУДУТ СКИДЫВАТЬСЯ ДАННЫЕ ИЗ ТАБЛИЦЫ БД







def runbot():
    bot.polling(none_stop = True)

print('Бот запущен') #УВЕДОМЛЕНИЕ О ТОМ ЧТО БОТ ЗАПУЩЕН

def runSchedulers():
    schedule.every().day.at("09:00").do(job) # СТАВИМ ВРЕМЯ НА 9 ЧАСОВ УТРА КОГДА БОТ БУДЕТ ПИСАТЬ В ГРУППУ 

    while True:
          schedule.run_pending()
          time.sleep(1)

if __name__ == "__main__":
    t1 = threading.Thread(target=runbot)
    t2 = threading.Thread(target=runSchedulers)

    t1.start()
    t2.start()



