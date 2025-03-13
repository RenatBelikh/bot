from aiogram import types

# Создаем кнопки (важно: с заглавной буквы!)
button1 = types.KeyboardButton(text='/start')
button2 = types.KeyboardButton(text='стоп')
button3 = types.KeyboardButton(text='инфо')
button4 = types.KeyboardButton(text='Закрыть')
button5 = types.KeyboardButton(text='Покажи лису')
button6 = types.KeyboardButton(text='/prof')

# Собираем кнопки в список списков
keyboard1 = [
    [button1, button2, button3],
    [button4, button5, button6],
]
keyboard2 = [
    [button3, button4],
]

# Создаем клавиатуру
kb1 = types.ReplyKeyboardMarkup(
    keyboard=keyboard1,
    resize_keyboard=True,  # Сделать клавиатуру меньше
    one_time_keyboard=False  # Клавиатура остается после нажатия
)
kb2 = types.ReplyKeyboardMarkup(
    keyboard=keyboard2,
    resize_keyboard=True,  # Сделать клавиатуру меньше
    one_time_keyboard=False  # Клавиатура остается после нажатия
)
