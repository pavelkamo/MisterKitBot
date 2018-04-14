import os
import telebot
import time

from telebot import types
from bot_properties import bot_properties
from eKids_bot.utils import Round

bot = telebot.TeleBot(bot_properties.token)
user_round = Round()

@bot.message_handler(commands=['commands'])
def get_commands(message):
    bot.send_message(message.chat.id, 'Все доступные команды:\n'
                                      '/presetnation - получить файл презентации\n'
                                      '/code1 - question\n'
                                      '/code2 - data_item\n'
                                      '/code3 - Round()\n'
                                      '/code4 - Bot behaviour\n'
                                      '/code5 - check_answer')

@bot.message_handler(commands=['code1'])
def get_code1(message):
    bot.send_message(message.chat.id, 'Code 1:\n https://codeshare.io/5e89nK')

@bot.message_handler(commands=['code2'])
def get_code2(message):
    bot.send_message(message.chat.id, 'Code 2:\n https://codeshare.io/anNnyX')

@bot.message_handler(commands=['code3'])
def get_code3(message):
    bot.send_message(message.chat.id, 'Code 3:\n https://codeshare.io/5opPjp')

@bot.message_handler(commands=['code4'])
def get_code4(message):
    bot.send_message(message.chat.id, 'Code 4:\n https://codeshare.io/a3pY4v')

@bot.message_handler(commands=['code5'])
def get_code5(message):
    bot.send_message(message.chat.id, 'Code 5:\n https://codeshare.io/GkNAl3')

@bot.message_handler(commands=['presetnation'])
def get_presentation(message):
    bot.send_message(message.chat.id, 'Presenttion:\n https://www.dropbox.com/s/94qjek6x3i1vipc/TelegramBot2.pptx?dl=0')

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


