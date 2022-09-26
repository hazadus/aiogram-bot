from aiogram import types, Dispatcher

from spawn_bot import bot


# @dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    # noinspection PyBroadException
    try:
        await bot.send_message(message.from_user.id, '<start/help> placeholder. Please send commands directly to bot.')
        await message.delete()
    except:
        await message.reply('<start/help> placeholder. Please start bot to send commands directly to bot')


def register_client_handlers(disp: Dispatcher):
    disp.register_message_handler(command_start, commands=['start', 'help'])
