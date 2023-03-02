#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot
from telebot import types
from config import API_TOKEN



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
    elif(message.text == "Электро ⚡"):
        bot.send_message(message.chat.id, text="Название велосипеда")
        
        
    elif(message.text == "Назад 🔙"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Добавить Велосипед")
        btn2 = types.KeyboardButton("Удалит велосипед")
        btn3 = types.KeyboardButton("Создать пост")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, text="Возвращаю в главное меню".format(message.from_user), reply_markup=markup)
    


    


bot.infinity_polling()


