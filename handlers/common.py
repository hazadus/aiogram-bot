import logging

from aiogram import types, Dispatcher


# @dp.message_handler()  # Any message to bot/chat
async def any_message(message: types.Message):
    logging.info(f'"@{message.from_user.username}" id={message.from_user.id} chat_id:{message.chat.id}: {message.text}')
    if 'привет' in message.text.lower():
        await message.answer('И тебе не хворать!')
    # await message.answer('You wrote (answer): ' + message.text)
    # await message.reply('You wrote (reply): ' + message.text)
    # await bot.send_message(message.from_user.id, 'You wrote (send_message): ' + message.text)  # Private (direct) msg


def register_common_handlers(disp: Dispatcher):
    disp.register_message_handler(any_message)
