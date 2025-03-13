#from random import randint
from aiogram import Bot, Dispatcher
#from aiogram.filters import Command
from aiogram.enums import ParseMode
#from less3.keyboards.keyboard import  kb1
#from less3.keyboards.keyboard import  kb2
from aiogram.client.default import DefaultBotProperties  # Импортируем DefaultBotProperties
#from less3.utils.randomfox import fox
import asyncio
import config
from handlers import common,career_choice

# Обработчик команды /start



# Запуск бота
async def main():
    # Укажите ваш токен
    API_TOKEN = config.token
    # Инициализация бота с использованием DefaultBotProperties
    bot = Bot(token=API_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()
    dp.include_router(career_choice.router)
    dp.include_router(common.router)
    #
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())


