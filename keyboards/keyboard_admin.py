from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btn1 = KeyboardButton('/upload')
btn2 = KeyboardButton('/delete')

kbd_admin = ReplyKeyboardMarkup(resize_keyboard=True,  # Make buttons smaller
                                one_time_keyboard=False  # Set to True to hide kbd after first button press
                                )

kbd_admin.row(btn1, btn2)
