#!/usr/bin/env python
import telebot
from telebot import types
import random
from telebot.types import Message

TOKEN = '1880257043:AAH1vPzDRlD6dY6KC99U2CZuJRV79yDu_ic'


bot = telebot.TeleBot(TOKEN)
STICKER_ID = 'CAACAgIAAxkBAAIEymCj9BeaUyFS1vPb63OxqKeqXn37AAIEAQACVp29Ct4E0XpmZvdsHwQ'
USERS = set()


@bot.message_handler(commands=['start', 'help'])
def command_handler(message: Message):
    if message.text == '/start':
        bot.send_message(message.from_user.id, 'Я бот который был создан Айдаром ради тебя одной) переспим?')
        bot.register_next_step_handler(message, reg_next)
    elif message.text == '/help':
        bot.send_message(message.from_user.id, 'Я пока мало чего умею, но и ты борщ не досолила!!!')


def reg_next(message: Message):
    if 'ахаххахаххазаззаъаахываваха' in message.text.lower():
        bot.send_message(message.from_user.id, 'Между прочем ничего смешного тут нету 😂')
    elif 'да' in message.text.lower():
        keyboard = types.InlineKeyboardMarkup()
        key_your_home = types.InlineKeyboardButton(text='У тебя', callback_data='yourhome')
        keyboard.add(key_your_home)
        key_my_home = types.InlineKeyboardButton(text='У меня', callback_data='myhome')
        keyboard.add(key_my_home)
        key_padik = types.InlineKeyboardButton(text='Мы же жесткие в падике конечно', callback_data='vpadike')
        keyboard.add(key_padik)
        question = 'Ну что ж тогда выбирай где?)'
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == 'yourhome':
        bot.send_message(call.message.chat.id, 'Оу май познакослюсь с твоим отцом')
    elif call.data == 'myhome':
        bot.send_message(call.message.chat.id, 'Да уж родители прямо скажем будут в ахуях')
    elif call.data == 'vpadike':
        bot.send_message(call.message.chat.id, 'А я знал что мы с тобой родственные души')


@bot.message_handler(content_types=['video', 'photo'])
def video_gif(message: Message):
    if message.video:
        bot.send_message(message.from_user.id, 'АХАХАХАХАХ')
    elif message.photo:
        bot.send_message(message.from_user.id, 'Это что за богиня такая')


@bot.message_handler(content_types=['text'])
@bot.edited_message_handler(content_types=['text'])
def echo_digits(message: Message):
    if 'Айдар, такой красивый мальчик' in message.text:
        bot.reply_to(message, 'YEAAAAAH, MY FUCKING GIRL')
        return
    reply = str(random.random())
    if message.from_user.id in USERS:
        reply += f'  {message.from_user.id}  hello again'
    bot.reply_to(message, reply)
    USERS.add(message.from_user.id)


@bot.message_handler(content_types=['sticker'])
def stiker_handler(message: Message):
    bot.send_sticker(message.from_user.id, STICKER_ID)


@bot.inline_handler(lambda query: query.query == 'text')
def query_text(inline_query):
    print(inline_query)
    try:
        r = types.InlineQueryResultArticle('1', 'Result', types.InputTextMessageContent('Result message.'))
        r2 = types.InlineQueryResultArticle('2', 'Result2', types.InputTextMessageContent('Result message2.'))
        bot.answer_inline_query(inline_query.id, [r, r2])
    except Exception as e:
        print(e)


bot.polling()
