import os

from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup

from database.db_sqlite import sqlite_add_product


class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()


async def admin_upload(message: types.Message):
    await FSMAdmin.photo.set()
    await message.answer('Upload photo')


async def admin_cancel(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.answer('OK, canceled.')


async def set_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await FSMAdmin.next()
    await message.answer('Now, enter title (name):')


async def set_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.answer('Now, enter description:')


async def set_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    await FSMAdmin.next()
    await message.answer('Now, set the price:')


async def set_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = float(message.text)

    await sqlite_add_product(state)

    await state.finish()


async def admin_getlogs(message: types.Message):
    if os.path.exists(str(os.getenv('BOT_LOG_FILENAME'))):
        await message.answer('Sending logs...')
        await message.answer_document(open(os.getenv('BOT_LOG_FILENAME'), 'rb'))
    else:
        await message.answer('Log file not found!')


async def admin_media(message: types.Message):
    """
    Used to get media ID. Use IDs to send these images/videos/gifs to chats or users.
    """
    if message.photo:
        await message.reply(f'Photo ID: {message.photo[0].file_id}')
    if message.video:
        await message.reply(f'Video ID: {message.video.file_id}')
    if message.animation:
        await message.reply(f'Animation ID: {message.animation.file_id}')
    if message.sticker:
        await message.reply(f'Sticker ID: {message.sticker.file_id}')


async def empty(message: types.Message):  # Must be last, deletes all non-existend commands/messages.
    await message.answer('No such command!')
    await message.delete()


def filter_admin(message: types.Message):
    return message.chat.type == 'private' and str(message.from_user.id) == os.getenv('BOT_ADMIN')


def register_admin_handlers(disp: Dispatcher):
    disp.register_message_handler(admin_upload, filter_admin, commands=['upload'], state=None)
    disp.register_message_handler(admin_cancel, filter_admin, commands=['отмена', 'cancel'], state='*')
    disp.register_message_handler(admin_cancel, filter_admin, Text(equals='отмена', ignore_case=True), state='*')
    disp.register_message_handler(admin_cancel, filter_admin, Text(equals='cancel', ignore_case=True), state='*')
    disp.register_message_handler(set_photo, filter_admin, content_types=['photo'], state=FSMAdmin.photo)
    disp.register_message_handler(set_name, filter_admin, state=FSMAdmin.name)
    disp.register_message_handler(set_description, filter_admin, state=FSMAdmin.description)
    disp.register_message_handler(set_price, filter_admin, state=FSMAdmin.price)
    disp.register_message_handler(admin_getlogs, filter_admin, commands=['getlogs'])
    disp.register_message_handler(admin_media, filter_admin, content_types=['photo', 'video', 'animation', 'sticker'])
    disp.register_message_handler(empty, filter_admin)
