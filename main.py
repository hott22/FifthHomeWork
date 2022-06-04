import logging
from aiogram import Bot, Dispatcher, executor, types
from config import Token

bot = Bot(token=Token)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

def math_msg(msg):
    return eval(msg)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет!\nВведи /help посмотри что я умею")

@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    await message.reply("/math - математические примеры\n")

@dp.message_handler(commands=["math"])
async def cmd_test1(message: types.Message):
    await message.reply("Введи математический пример:")
    @dp.message_handler()
    async def echo(message: types.Message):
        await message.answer(message.text)
        await message.reply(math_msg(message.text))


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
