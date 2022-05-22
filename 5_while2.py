"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""

from unittest import skip

questions_and_answers = {"Привет": "Привет!", "Как дела?": "Хорошо!", "Что делаешь?": "Программирую", "Как тебя зовут?": "Оля, а тебя?"}

def ask_user(answers_dict):
    """
    Замените pass на ваш код
    """
    while True:
      answers_dict = input('Введите ваш вопрос, пожалуста. ')
      if answers_dict in questions_and_answers:
        print(questions_and_answers.get(answers_dict))
      else:
        print('Извините, я не знаю.') and skip
    
if __name__ == "__main__":
    ask_user(questions_and_answers)
