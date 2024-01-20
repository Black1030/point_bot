import json
import telebot
from telebot import types
from functions import read_data, write_data

token = ""
bot = telebot.TeleBot(token)

people = {}
teachers = [1889897687]


@bot.message_handler(commands=["start"])
def start(message):
    print(people)
    chat_id = message.chat.id
    data = read_data('data_base.json')
    if str(chat_id) in data.keys():
        bot.send_message(chat_id, "Вы уже зареганы")
    else:
        answer = bot.send_message(chat_id, "Привет, напиши фамилию и имя")
        bot.register_next_step_handler(answer, get_users)

def maessage_of_button(message):
    text = message.text
    if text == "shop":
        print(1)

def get_users(message):
    chat_id = message.chat.id
    username = message.text
    filename = 'data_base.json'
    people = read_data(filename)
    people[chat_id] = {"coin": 0, "name": username}
    write_data(people, filename)
    bot.send_message(chat_id, "Мы тебя зарегистрировали!")
    print(people)


@bot.message_handler(commands=["id"])
def get_coin(message):
    chat_id = message.chat.id
    data = read_data('data_base.json')
    if str(chat_id) in list(data.keys()):

        message = bot.send_message(chat_id, "Отправьте id ученика!!!!!!")
        bot.register_next_step_handler(message, all_ok)


def all_ok(message):
    chat_id = message.chat.id
    text = message.text
    user_id, count = text.split()
    data = read_data('data_base.json')
    data[str(user_id)]["coin"] += int(count)
    write_data(data, 'data_base.json')
    bot.send_message(chat_id, "Да, все ок")
    bot.send_message(user_id, f"Вам начислили {count}")

@bot.message_handler(commands=["button"])
def button(message):
    chat_id = message.chat.id


    markup = types.InlineKeyboardMarkup(row_width=2)
    item_1 = types.InlineKeyboardButton("shop", callback_data="shop")
    item_2 = types.InlineKeyboardButton("balance", callback_data="money")
    markup.add(item_1, item_2)
    bot.send_message(chat_id, "Выберите, что вы хотите увидеть", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "shop"):
        bot.send_message(message.chat.id, text="")

@bot.message_handler(commands=["balance"])
def balance(message):
    chat_id = message.chat.id
    data = read_data('data_base.json')
    bot.send_message(chat_id, f"Ваш баланс: {data[str(chat_id)]['coin']}")

bot.polling(none_stop=True)





