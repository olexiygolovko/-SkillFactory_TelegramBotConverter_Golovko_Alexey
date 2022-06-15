import telebot
from telebot import types

from config import TOKEN, keys
from extensions import APIException, Convertor


def create_markup(base=None):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    buttons = []
    for val in keys.keys():
        if val != base:
            buttons.append(types.KeyboardButton(val.capitalize()))
    markup.add(*buttons)
    return markup


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def start(message: telebot.types.Message):
    text = f'🤖 Привет! Я телеграмм бот - WhatCourseBot\n' \
           f'Моя задача - конвертировать валюту\n' \
           f'/values - список доступных валют\n' \
           f'/convert - приступить к конвертации\n' \
           f'/help - вывести навигацию повторно\n' \
           f'/start - в начало'
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = f'🤓 Доступные валюты:'
    for i in keys.keys():
        text = '\n✅ '.join((text, i))
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['convert'])
def values(message: telebot.types.Message):
    text = 'Выберите валюту из которой конвертировать:'
    bot.send_message(message.chat.id, text, reply_markup=create_markup())
    bot.register_next_step_handler(message, base_handler)


def base_handler(message: telebot.types.Message):
    base = message.text.strip().lower()
    text = 'Выберите валюту в которую конвертировать:'
    bot.send_message(message.chat.id, text, reply_markup=create_markup(base))
    bot.register_next_step_handler(message, quote_handler, base)


def quote_handler(message: telebot.types.Message, base):
    sym = message.text.strip().lower()
    text = 'Укажите количество конвертируемой валюты:'
    bot.send_message(message.chat.id, text)
    bot.register_next_step_handler(message, amount_handler, base, sym)


def amount_handler(message: telebot.types.Message, base, sym):
    amount = message.text.strip()
    try:
        new_price = Convertor.get_price(base, sym, amount)
    except APIException as e:
        bot.send_message(message.chat.id, f'Ошибка конвертации:\n{e} ')
    else:
        text = f'Курс {amount} {base} - {new_price} {sym} '
        bot.send_message(message.chat.id, text)


bot.polling()
