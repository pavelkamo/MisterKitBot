# -*- coding: utf-8 -*-
import telebot

from bot_properties import bot_properties

bot = telebot.TeleBot(bot_properties.token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, message.text)
    # bot.send_message(message.chat.id, "Містер Кіт каже привіт!")

if __name__ == '__main__':
    bot.polling(none_stop=True)