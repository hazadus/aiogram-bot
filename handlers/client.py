import os

from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton

from spawn_bot import bot
from keyboards import kbd_client
from database.db_sqlite import sqlite_get_all_products, sqlite_delete_product


async def command_start(message: types.Message):
    # noinspection PyBroadException
    try:
        await bot.send_message(message.from_user.id, '<start/help> placeholder. This is direct chat with bot.',
                               reply_markup=kbd_client)
        await message.delete()
    except:
        await message.reply('<start/help> placeholder. Please send commands directly to bot.')


async def command_menu(message: types.Message):
    for product in await sqlite_get_all_products():
        inline_kbd = InlineKeyboardMarkup(row_width=2)
        inline_btn1 = InlineKeyboardButton(text='Add to cart', callback_data=f'add_to_cart_id={product[0]}')
        inline_btn2 = InlineKeyboardButton(text='Open link', url='https://www.hazadus.ru/')
        inline_kbd.add(inline_btn1, inline_btn2)

        if message.chat.type == 'private' and str(message.from_user.id) == os.getenv('BOT_ADMIN'):
            inline_btn3 = InlineKeyboardButton(text='Delete', callback_data=f'delete_id={product[0]}')
            inline_kbd.add(inline_btn3)

        await bot.send_photo(message.from_user.id,
                             product[1], f'{product[2]}\nDescription: {product[3]}\nPrice: {product[4]}',
                             reply_markup=inline_kbd)
    await message.delete()


async def command_remove_kbd(message: types.Message):
    await bot.send_message(message.from_user.id, 'Deleting keyboard. Use /start to restore.',
                           reply_markup=ReplyKeyboardRemove())
    await message.delete()


async def callback_add_to_cart(callback: types.CallbackQuery):
    prod_id = int(callback.data.replace('add_to_cart_id=', ''))
    await callback.answer(f'Added to cart: product id={prod_id}')


async def callback_delete_product(callback: types.CallbackQuery):
    prod_id = int(callback.data.replace('delete_id=', ''))
    await sqlite_delete_product(prod_id)
    await callback.answer(f'Product id={prod_id} deleted.', show_alert=True)


def register_client_handlers(disp: Dispatcher):
    disp.register_message_handler(command_start, commands=['start', 'help'])
    disp.register_message_handler(command_menu, commands=['menu'])
    disp.register_message_handler(command_remove_kbd, commands=['remove_kbd'])
    disp.register_callback_query_handler(callback_add_to_cart, Text(startswith='add_to_cart_id='))
    disp.register_callback_query_handler(callback_delete_product, Text(startswith='delete_id='))
