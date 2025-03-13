from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



def make_row_keyboard(buttons: list[str]) -> ReplyKeyboardMarkup:
    row = [KeyboardButton(text=button) for button in buttons]
    return ReplyKeyboardMarkup(keyboard=[row], resize_keyboard=True)
    #вот вариант расшифровывается выше строка
    # for button in buttons:
    # row.append(KeyboardButton(text=button))
