import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters.command import Command



token='5655600178:AAHhDmhKk06k4_EYxpfLD5n_ilVTMZ4RBFY'

bot = Bot(token=token)

dp = Dispatcher()

@dp.message(Command('start'))
async def hello(message):
    await message.answer("hello")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())