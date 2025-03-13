

from aiogram import Router,Bot, Dispatcher, types , F
from aiogram.filters import Command
from aiogram.enums import ParseMode
from less3.keyboards.keyboard import  kb1,kb2

from aiogram.client.default import DefaultBotProperties  # Импортируем DefaultBotProperties
from less3.utils.randomfox import fox
from random import randint
import asyncio

#import config

# Укажите ваш токен
#API_TOKEN = config.token

# Инициализация бота с использованием DefaultBotProperties
#bot = Bot(token=API_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
#dp = Dispatcher()

router = Router()

# Обработчик команды /start
@router.message(Command("start"))
async def cmd_start(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Привет, {name} Я твой бот', reply_markup=kb1)

# Эхо-обработчик (отвечает тем же текстом, что и пользователь)

#хэндлер на команду /fox
@router.message(Command('fox'))
@router.message(Command('лиса'))
@router.message(F.text.lower() == 'покажи лису')
async def cmd_fox(message: types.Message):
    name = message.chat.first_name
    img_fox = fox()
    await message.answer(f'Держи лису, {name} ')
    await message.answer_photo(photo=img_fox)
   # await bot.send_photo(message.from_user.id,photo=img_fox)

@router.message(F.text.lower() == 'num')
async def send_random(message: types.Message):
    number = randint(1, 10)
   # number = random.randint(a=1, b=10)
   # number1 = randint()
    await message.answer(f"{number}")

#Хэндлер на сообщение
@router.message(F.text)
async def msg_echo(message: types.Message):
    msg_user=message.text
    name = message.chat.first_name
    if 'привет' in msg_user:
        await message.answer(f'Привет {name}')
    elif 'пока' in msg_user:
        await message.answer(f'Пока {name}')
    elif 'дай' in msg_user:
            await message.answer(f'дай {name}',reply_markup=kb2)
    else:
        await message.answer(f'Ты написал - {msg_user}')



# Запуск бота
#async def main():
 #   await dp.start_polling(bot)

#if __name__ == "__main__":
#    asyncio.run(main())