import json
import telebot
from telebot import types

token = ""
bot = telebot.TeleBot(token)

people = {}
teachers = [1889897687]


@bot.message_handler(commands=["start"])
def start(message):
    print(people)
    chat_id = message.chat.id
    answer = bot.send_message(chat_id, "Привет, напиши фамилию и имя")
    bot.register_next_step_handler(answer, get_users)


def get_users(message):
    chat_id = message.chat.id
    username = message.text
    people[chat_id] = {"coin": 0, "name": username}
    bot.send_message(chat_id, "Мы тебя зарегестрировали!")
    with open("file.json", 'w') as read_file:
        object = json.load(read_file)
    print(people)


@bot.message_handler(commands=["id"])
def get_coin(message):
    chat_id = message.chat.id
    s = ""
    for user_id, user_name in people.items():
        s += f"{user_id}:{user_name}"

    if chat_id in teachers:
        bot.send_message(chat_id, s)
        message = bot.send_message(chat_id, "Отправьте id ученика!!!!!!")
        bot.register_next_step_handler(message, all_ok)


def all_ok(message):
    chat_id = message.chat.id
    text = message.text
    user_id, count = text.split()
    people[int(user_id)]["coin"] += int(count)
    print(chat_id)
    bot.send_message(chat_id, "Да, все ок")
    bot.send_message(user_id, f"Вам начислили {count}")



    # if id not in people:
    #     bot.send_message(chat_id, "Такой пользователь не найден. Попробуйте снова")
    # else:
    #     people["coin"] += 1


# people = {131123: {"coin": 0, "name": "Pupkin"}}
# student = people.get(id)
#
#    сказать, что студент не найден
# else:
#    student["coin"] += 1

@bot.message_handler(commands=["button"])
def button(message):
    chat_id = message.chat.id
    markup = types.InlineKeyboardMarkup(row_width=2)
    # item_1 = types.InlineKeyboardButton("shop", callback_data="purchases")
    item_2 = types.InlineKeyboardButton("balance", callback_data="money")
    markup.add(item_2)
    bot.send_message(chat_id, "Выберите, что вы хотите увидеть", reply_markup=markup)


@bot.message_handler(commands=["balance"])
def balance(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, f"Ваш баланс: {people[chat_id]['coin']}")



if __name__ == "__main__":

    j_string = '{"name": "Bob", "languages": "English"}'

    y = json.loads(j_string)
    print("JSON string = ", y)
    print()
    f = open('data.json', "r")

data = json.loads(f.read())

for i in data['emp_details']:
        print(i)
        f.close()

bot.polling(none_stop=True)





