from telebot import types
from random import randint

question_1 = {}
question_1['question'] = 'What programming language are you studying?'
question_1['right_answer'] = 'Python'
question_1['wrong_answer'] = 'Java'

question_2 = {}
question_2['question'] = 'Are you human?'
question_2['right_answer'] = 'Yes'
question_2['wrong_answer'] = 'No'

question_3 = {}
question_3['question'] = 'Have you ever been on Mars?'
question_3['right_answer'] = 'No'
question_3['wrong_answer'] = 'Yes'

game_data = [question_1, question_2, question_3]

"""Получить одну запись с данными из хранилища"""
def get_data_item(item_number):
    return game_data[item_number]

def count_items():
    return len(game_data)


class Round():

    def get_new_round(self):
        item_number = randint(0, len(game_data)-1)
        self.item = get_data_item(item_number)
        self.question = self.item.get('question')
        self.right_answer = self.item.get('right_answer')
        self.wrong_answer = self.item.get('wrong_answer')

    def generate_markup(self, right_answer, wrong_answer):
        """
        Создаем кастомную клавиатуру для выбора ответа
        :param right_answer: Правильный ответ
        :param wrong_answer: Неправильный ответо
        :return: Объект кастомной клавиатуры
        """
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.add(right_answer)
        markup.add(wrong_answer)
        return markup

    def get_answer_for_user(self):
        try:
            return self.right_answer
        # Если человек не играет, ничего не возвращаем
        except AttributeError:
            return None