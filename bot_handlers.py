from bot import bot
from message import *
import random
from draft import food
from db import users_db




name = ''


@bot.message_handler(commands='start')
def message_start(message):
    if not users_db.find_one({"chat_id": message.chat.id}):
        users_db.insert_one({"chat_id": message.chat.id})
        bot.send_message(message.chat.id, HELLO_MESSAGE)
        bot.register_next_step_handler(message, reg_name)
    else:
        bot.send_message(message.chat.id, HELLO_AGAIN_MESSAGE)


def reg_name(message):
    global name
    name += message.text
    res = f'Отлично, {name}\n' \
          f'Я помогу тебе справиться с вопросом,' \
          f'который тебя так часто волнует"Что приготовить?"' \
          f'все что тебе нужно это оправить мне команду /help'
    bot.send_message(message.chat.id, res)


@bot.message_handler(commands='help')
def my_help(message):
    bot.send_message(message.chat.id, f'сегодня давай приготовим {food[random.randint(0, 5)][0]}')


if __name__ == '__main__':
     bot.polling(none_stop=True)