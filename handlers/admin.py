import os

from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup


class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    desctiption = State()
    price = State()


async def admin_start(message: types.Message):
    if message.chat.type == 'private' and str(message.from_user.id) == os.getenv('BOT_ADMIN'):
        await FSMAdmin.photo.set()
        await message.answer('Upload photo')
    else:
        await message.answer('Anly admin has access to this command.')


async def admin_cancel(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.answer('OK.')


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
        data['desctiption'] = message.text
    await FSMAdmin.next()
    await message.answer('Now, set the price:')


async def set_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = float(message.text)

    async with state.proxy() as data:
        await message.answer(str(data))

    await state.finish()


async def admin_getlogs(message: types.Message):
    if os.path.exists(str(os.getenv('BOT_LOG_FILENAME'))):
        await message.answer('Sending logs...')
        await message.answer_document(open(os.getenv('BOT_LOG_FILENAME'), 'rb'))
    else:
        await message.answer('Log file not found!')


async def admin_photo_video(message: types.Message):
    """
    Used to get media ID. Use IDs to send these images/videos/gifs to chats or users.
    """
    if message.photo:
        await message.reply(f'Photo ID: {message.photo[0].file_id}')
    if message.video:
        await message.reply(f'Video ID: {message.video.file_id}')
    if message.animation:
        await message.reply(f'Animation ID: {message.animation.file_id}')


async def empty(message: types.Message):  # Must be last, deletes all non-existend commands/messages.
    await message.answer('No such command!')
    await message.delete()


def register_admin_handlers(disp: Dispatcher):
    disp.register_message_handler(admin_start, commands=['upload'], state=None)
    disp.register_message_handler(admin_cancel, commands=['отмена', 'cancel'], state='*')
    disp.register_message_handler(admin_cancel, Text(equals='отмена', ignore_case=True), state='*')
    disp.register_message_handler(admin_cancel, Text(equals='cancel', ignore_case=True), state='*')
    disp.register_message_handler(set_photo, content_types=['photo'], state=FSMAdmin.photo)
    disp.register_message_handler(set_name, state=FSMAdmin.name)
    disp.register_message_handler(set_description, state=FSMAdmin.desctiption)
    disp.register_message_handler(set_price, state=FSMAdmin.price)
    disp.register_message_handler(admin_getlogs,
                                  lambda message: message.chat.type == 'private'
                                                  and str(message.from_user.id) == os.getenv('BOT_ADMIN'),
                                  commands=['getlogs'])
    disp.register_message_handler(admin_photo_video,
                                  lambda message: message.chat.type == 'private'
                                                  and str(message.from_user.id) == os.getenv('BOT_ADMIN'),
                                  content_types=['photo', 'video', 'animation'], )
    disp.register_message_handler(empty,
                                  lambda message: message.chat.type == 'private'
                                                  and str(message.from_user.id) == os.getenv('BOT_ADMIN'))
