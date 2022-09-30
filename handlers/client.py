from aiogram import types, Dispatcher
from aiogram.types import ReplyKeyboardRemove

from spawn_bot import bot
from keyboards import kbd_client
from database.db_sqlite import sqlite_get_all_products


async def command_start(message: types.Message):
    # noinspection PyBroadException
    try:
        await bot.send_message(message.from_user.id, '<start/help> placeholder. This is direct chat with bot.',
                               reply_markup=kbd_client)
        await message.delete()
    except:
        await message.reply('<start/help> placeholder. Please send commands directly to bot.')


async def command_menu(message: types.Message):
    for product in sqlite_get_all_products():
        await bot.send_photo(message.from_user.id,
                             product[0], f'{product[1]}\nDescription: {product[2]}\nPrice: {product[3]}')
    await message.delete()


async def command_remove_kbd(message: types.Message):
    await bot.send_message(message.from_user.id, 'Deleting keyboard. Use /start to restore.',
                           reply_markup=ReplyKeyboardRemove())
    await message.delete()


def register_client_handlers(disp: Dispatcher):
    disp.register_message_handler(command_start, commands=['start', 'help'])
    disp.register_message_handler(command_menu, commands=['menu'])
    disp.register_message_handler(command_remove_kbd, commands=['remove_kbd'])
