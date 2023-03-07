#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot
from telebot import types
from config import API_TOKEN
import sqlite3 
from DB import create_connection, BDelectro

create_connection("bycicle.db")

partVelo=[]

bot = telebot.TeleBot(API_TOKEN)


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
        
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Назад 🔙")
        markup.add(btn1)
        bot.send_message(message.chat.id, text="вводить в одну строку через запятую".format(message.from_user), reply_markup=markup)

        bot.register_next_step_handler(msg,velo)
        BDelectro(partVelo)
    
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

        bot.register_next_step_handler(msg,velo)

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

        bot.register_next_step_handler(msg,velo)

       

def velo(message):
    x = message.text
    partVelo.append(x.split(", "))
    print(partVelo)
    bot.reply_to(message, message.text )
    


bot.infinity_polling()




