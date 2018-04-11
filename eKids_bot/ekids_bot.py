import os
import telebot
import time

from telebot import types
from bot_properties import bot_properties
from eKids_bot.utils import Round

bot = telebot.TeleBot(bot_properties.token)
user_round = Round()

@bot.message_handler(commands=['game'])
def game(message):
    user_round.get_new_round()
    user_round.get_answer_for_user()

    # Формируем разметку
    markup = user_round.generate_markup(user_round.right_answer, user_round.wrong_answer)
    bot.send_message(message.chat.id, user_round.question, reply_markup=markup)

@bot.message_handler(commands=['music'])
def find_file_ids(message):
    markup = user_round.generate_markup('Top', 'Bottom')
    for file in os.listdir('music/'):
        if file.split('.')[-1] == 'mp3':
            f = open("music/"+file, 'rb')
            res = bot.send_voice(message.chat.id, f, 'Test question', reply_markup=markup)
            print(res)
        time.sleep(3)

@bot.message_handler(func=lambda message: True, content_types=['text'])
def check_answer(message):
    answer = user_round.get_answer_for_user()

    if not answer:
        bot.send_message(message.chat.id, 'Чтобы начать игру, выберите команду /game')
    else:
        # Уберем клавиатуру с вариантами ответа.
        keyboard_hider = types.ReplyKeyboardRemove()
        # Если ответ правильный/неправильный
        if message.text == answer:
            bot.send_message(message.chat.id, 'Верно! \nЕщё? /game', reply_markup=keyboard_hider)
        else:
            bot.send_message(message.chat.id, 'Увы, Вы не угадали. Попробуйте ещё раз! \n /game',
                             reply_markup=keyboard_hider)

if __name__ == '__main__':
    bot.polling(none_stop=True)


