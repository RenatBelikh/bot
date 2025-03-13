from aiogram import Router,Bot, Dispatcher, types , F
from aiogram.filters import Command
from aiogram.enums import ParseMode
from aiogram.fsm import state

from less3.keyboards.keyboard import  kb1,kb2
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.client.default import DefaultBotProperties  # Импортируем DefaultBotProperties
from less3.keyboards.prof_keyboards import  make_row_keyboard
from random import randint
import asyncio

#import config

# Укажите ваш токен
#API_TOKEN = config.token

# Инициализация бота с использованием DefaultBotProperties
#bot = Bot(token=API_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
#dp = Dispatcher()

router = Router()

available_jobs = [
     'Программмист',
     'Дизайнер',
     'Маркетолог',
]

available_grades = ['Junior','Middle','Senior' ]

class ChoicesProfile(StatesGroup):
     job = State()
     grade = State()

@router.message(Command('prof'))
async def command_prof (message: types.Message, state: FSMContext):
    await message.answer(text="Выберите профессию", reply_markup=make_row_keyboard(available_jobs))
    await state.set_state(ChoicesProfile.job)
    #await state.set_state(ChoicesProfile.name)


@router.message(ChoicesProfile.job, F.text.in_(available_jobs))
async def prof_chosen (message: types.Message, state: FSMContext):
    await state.update_data(profession=message.text)
    await message.answer(text="Выберите уровень", reply_markup=make_row_keyboard(available_grades))
    await state.set_state(ChoicesProfile.grade)



@router.message(ChoicesProfile.job)
async def prof_chosen_incorrect (message: types.Message):
    await message.answer(text="Выберите профессию", reply_markup=make_row_keyboard(available_jobs))





@router.message(ChoicesProfile.grade, F.text.in_(available_grades))
async def grade_chosen(message: types.Message, state: FSMContext):
        user_data =  await state.get_data()
        await message.answer(f"Ваша профессия: {user_data['profession']}\n"
                             f"Ваш уровень: {message.text}", reply_markup=types.ReplyKeyboardRemove())
       # await state.set_state(ChoicesProfile.grade)
        await state.clear()

@router.message(ChoicesProfile.grade)
async def grade_chosen_incorrect (message: types.Message):
    await message.answer(text="Выберите уровень", reply_markup=make_row_keyboard(available_grades))
#добавил комментарий
