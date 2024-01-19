import sqlite3
import telebot
from telebot import types

token = "6762639830:AAFUUCGNfTBluBLUIDt7QlNLPmcuq3lrmZQ"
bot = telebot.TeleBot(token)

people = {}


@bot.message_handler(commands=["start"])
def send_message(message):
    chat_id = message.chat.id
    answer = bot.send_message(chat_id, "Привет, представься, пожалуйста)")
    bot.register_next_step_handler(answer, your_user_name)


def your_user_name(message):
    chat_id = message.chat.id
    text = message.text

    if text == 1:
        print("Все отлично")
        answer = bot.send_message(chat_id, "Ты молодец!!")
        bot.register_next_step_handler(answer, your_sure_name)
    else:
        answer = bot.send_message(chat_id, "Нет, что-то не так, попробуй еще раз")
        bot.register_next_step_handler(answer, your_user_name)


def your_sure_name(message):
    chat_id = message.chat.id


bot.polling(none_stop=True)
