#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot
from telebot import types
from config import API_TOKEN
import sqlite3
from DB import velo,search
import time



partVelo=[]

bot = telebot.TeleBot(API_TOKEN)

Table=["Electro","Podves","hard"]


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Добавить Велосипед")
    btn2 = types.KeyboardButton("Удалит велосипед")
    btn3 = types.KeyboardButton("Создать пост")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Тут ты можешь добавить велосипеды в базу, а также удалить или создать пост ".format(message.from_user), reply_markup=markup)




@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "Удалит велосипед"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Электро ⚡⚡")
        btn2 = types.KeyboardButton("Хардтейл 🚴🚴")
        btn3 = types.KeyboardButton("Подвесы 🦹‍♂️🦹‍♂️")
        back=types.KeyboardButton("Назад 🔙")
        markup.add(btn1, btn2,btn3, back)
        bot.send_message(message.chat.id, text="Выберите класс удаляемого велосипеда", reply_markup=markup)
    elif(message.text == "Добавить Велосипед"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Электро ⚡")
        btn2 = types.KeyboardButton("Хардтейл 🚴")
        btn3 = types.KeyboardButton("Подвесы 🦹‍♂️")
        back=types.KeyboardButton("Назад 🔙")
        markup.add(btn1, btn2, btn3, back)
        bot.send_message(message.chat.id, text="Выберите класс добавляемого велосипеда", reply_markup=markup)




    elif(message.text == "Назад 🔙"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Добавить Велосипед")
        btn2 = types.KeyboardButton("Удалит велосипед")
        btn3 = types.KeyboardButton("Создать пост")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, text="Возвращаю в главное меню".format(message.from_user), reply_markup=markup)


    if message.text == 'Электро ⚡':
        msg = bot.send_message(message.chat.id,
        """название велосипеда
        рамы
        вилки
        переднего колеса
        заднего колеса
        Тормоза переднего
        Тормаза заднего
        заднйи перекл
        передний перкл
        вес
        Цена продажи """)

        table= Table[0]
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Назад 🔙")
        markup.add(btn1)
        bot.send_message(message.chat.id, text="вводить в одну строку через запятую".format(message.from_user), reply_markup=markup)

        bot.register_next_step_handler(message,velo,table)






    if message.text == 'Хардтейл 🚴':
        msg = bot.send_message(message.chat.id,
        """название велосипеда
        рамы
        вилки
        переднего колеса
        заднего колеса
        Тормоза переднего
        Тормаза заднего
        заднйи перекл
        передний перкл
        вес
        Цена продажи """)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Назад 🔙")
        markup.add(btn1)
        bot.send_message(message.chat.id, text="вводить в одну строку через запятую".format(message.from_user), reply_markup=markup)
        table=Table[2]

        bot.register_next_step_handler(message,velo,table)

    if message.text == 'Подвесы 🦹‍♂️':
        msg = bot.send_message(message.chat.id,
        """название велосипеда
        рамы
        вилки
        переднего колеса
        заднего колеса
        Тормоза переднего
        Тормаза заднего
        заднйи перекл
        передний перкл
        вес
        Цена продажи """)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Назад 🔙")
        markup.add(btn1)
        bot.send_message(message.chat.id, text="вводить в одну строку через запятую".format(message.from_user), reply_markup=markup)
        table=Table[1]
        bot.register_next_step_handler(message,velo,table)

    if message.text== "Электро ⚡⚡":
        
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Назад 🔙")
        markup.add(btn1)
        bot.send_message(message.chat.id, text="ПОСЛЕ УДАЛЕНИЯ ВЕЛОСИПЕД ИСЧЕЗНТ ИЗ ЦВЕТОВ".format(message.from_user), reply_markup=markup)
        table=Table[0]
        bot.send_message(message.chat.id,text=str(search(table)).format(message.from_user), reply_markup=markup)
        








bot.infinity_polling()




