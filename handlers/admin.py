from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup


class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    desctiption = State()
    price = State()


async def admin_start(message: types.Message):  # TODO: check if user is admin via os.getenv('BOT_ADMIN')
    await FSMAdmin.photo.set()
    await message.answer('Upload photo')


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


def register_admin_handlers(disp: Dispatcher):
    disp.register_message_handler(admin_start, commands=['upload'], state=None)
    disp.register_message_handler(admin_cancel, commands=['отмена', 'cancel'], state='*')
    disp.register_message_handler(admin_cancel, Text(equals='отмена', ignore_case=True), state='*')
    disp.register_message_handler(admin_cancel, Text(equals='cancel', ignore_case=True), state='*')
    disp.register_message_handler(set_photo, content_types=['photo'], state=FSMAdmin.photo)
    disp.register_message_handler(set_name, state=FSMAdmin.name)
    disp.register_message_handler(set_description, state=FSMAdmin.desctiption)
    disp.register_message_handler(set_price, state=FSMAdmin.price)
