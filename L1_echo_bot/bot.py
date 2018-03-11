# -*- coding: utf-8 -*-
from bot_properties import bot_properties
import telebot


bot = telebot.TeleBot(bot_properties.token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    # bot.send_message(message.chat.id, message.text)
    bot.send_message(message.chat.id, "Містер Кіт єбав всіх в ріт!")

if __name__ == '__main__':
    bot.polling(none_stop=True)