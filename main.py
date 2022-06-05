import logging
from aiogram import Bot, Dispatcher, executor, types
from config import Token, open_weather_token
import requests

bot = Bot(token=Token)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

def get_weather(city, open_weather_token, ru=None):
    try:
        r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}'
                         f'&appid={open_weather_token}&lang={ru}')
        data = r.json()
        print(data)
    except Exception as ex:
        print(ex)
        print('Проверьте название города')




def main():
    city = input('Введите город: ')
    get_weather(city, open_weather_token)



@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет!\nВведи /help посмотри что я умею")

@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    await message.reply("/math - математические примеры\n")

@dp.message_handler(commands=["math"])
async def math(message: types.Message):
    await message.reply("Введи математический пример:")
    @dp.message_handler()
    async def math2(message: types.Message):
        await message.reply(eval(message.text))


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
