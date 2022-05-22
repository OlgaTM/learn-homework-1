"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import ephem
import settings
import datetime

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')

def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)

def name_planet(update, context):
    user_planet = update.message.text
    list_user_planet = user_planet.split(' ')
    name_planet = list_user_planet[1]
    today = datetime.date.today()
    if name_planet == 'Mars':
      planet = ephem.Mars(today)
      constellation = ephem.constellation(planet)[1]
      update.message.reply_text(f'Сегодня планета {name_planet} находится в созвездии {constellation}')
    elif name_planet == 'Pluto':
      planet = ephem.Pluto(today)
      constellation = ephem.constellation(planet)[1]
      update.message.reply_text(f'Сегодня планета {name_planet} находится в созвездии {constellation}')
    elif name_planet == 'Mercury':
      planet = ephem.Mercury(today)
      constellation = ephem.constellation(planet)[1]
      update.message.reply_text(f'Сегодня планета {name_planet} находится в созвездии {constellation}')  
    elif name_planet == 'Venus':
      planet = ephem.Venus(today)
      constellation = ephem.constellation(planet)[1]
      update.message.reply_text(f'Сегодня планета {name_planet} находится в созвездии {constellation}')
    elif name_planet == 'Jupiter':
      planet = ephem.Jupiter(today)
      constellation = ephem.constellation(planet)[1]
      update.message.reply_text(f'Сегодня планета {name_planet} находится в созвездии {constellation}')  
    elif name_planet == 'Saturn':
      planet = ephem.Saturn(today)
      constellation = ephem.constellation(planet)[1]
      update.message.reply_text(f'Сегодня планета {name_planet} находится в созвездии {constellation}') 
    elif name_planet == 'Neptun':
      planet = ephem.Neptun(today)
      constellation = ephem.constellation(planet)[1]
      update.message.reply_text(f'Сегодня планета {name_planet} находится в созвездии {constellation}')
    elif name_planet == 'Uranus':
      planet = ephem.Uranus(today)
      constellation = ephem.constellation(planet)[1]
      update.message.reply_text(f'Сегодня планета {name_planet} находится в созвездии {constellation}')
    elif name_planet == 'Sun':
      planet = ephem.Sun(today)
      constellation = ephem.constellation(planet)[1]
      update.message.reply_text(f'Сегодня планета {name_planet} находится в созвездии {constellation}')
    else:
      update.message.reply_text('Неизвестная планета')
      

def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)

def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", name_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()
