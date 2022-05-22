"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def comparison_of_srtings(string_1, string_2):
  if type(string_1) != str or type(string_2) != str:
    return(0)
  elif type(string_1) == str and type(string_2) == str and string_1 == string_2:
    return(1)
  elif type(string_1) == str and type(string_2) == str and string_1 != string_2 and len(string_1) > len(string_2) and string_2 != 'learn':
    return(2)
  elif type(string_1) == str and type(string_2) == str and string_1 != string_2 and string_2 == 'learn':
    return(3)
  else:
    return('К сожалению, опции для сравнения Ваших строк нет, попробуйте другой вариант =)')

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    print(comparison_of_srtings(1, 2))
    print(comparison_of_srtings(1, 'Hello'))
    print(comparison_of_srtings('Hello', 2))
    print(comparison_of_srtings('Hello', 'Hello'))
    print(comparison_of_srtings('Good afternoon', 'Hello'))
    print(comparison_of_srtings('Good afternoon', 'learn'))
    print(comparison_of_srtings('Hello', 'Good afternoon'))

if __name__ == "__main__":
    main()
