from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btn1 = KeyboardButton('/remove_kbd')
btn2 = KeyboardButton('/help')
btn4 = KeyboardButton('Share phone number', request_contact=True)
btn5 = KeyboardButton('Share location', request_location=True)

kbd_client = ReplyKeyboardMarkup(resize_keyboard=True,  # Make buttons smaller
                                 one_time_keyboard=False  # Set to True to hide kbd after first button press
                                 )

kbd_client.row(btn1, btn2).row(btn4, btn5)  # Ex: .add(btn1).insert(btn3)
