import config
import telebot
import requests
import time
appid = "ae6533ba5836ef6437c8a6765313a210"
bot = telebot.TeleBot(config.TOKEN)

root_url = "http://api.openweathermap.org/data/3.0/weather?"


def get_w(city_name):
    r = requests.get(
        f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&type=like&units=metric&APPID=ae6533ba5836ef6437c8a6765313a210')

    data = r.json()
    # conditions = data['weather'][0]['description']
    if data['cod'] == 200:
        temp = data['main']['temp']
        temp_min = data['main']['temp_min']
        temp_max = data['main']['temp_max']
        return f"Температура в {city_name} - {temp} Минимальная - {temp_min} Максимальная - {temp_max}"
    else:
        time.sleep(2)
        return f"Ошибка"
# Присваивание токена
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,"Привет ✌️ ")
    bot.send_message(
        message.chat.id, "Приветствую. Погода в каком городе (eng)?")

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):  # Название функции не играет никакой роли
    bot.send_message(message.chat.id, get_w(message.text))
    bot.send_message(message.chat.id, message.text)
    
# Функция повтора сообщений


bot.polling(none_stop=True)
# Цикл
