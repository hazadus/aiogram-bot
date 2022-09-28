#!/bin/bash

# Set these env vars according to yours
export BOT_TOKEN=TelegramBotToken
export BOT_ADMIN=Bot-AdminChatID
export BOT_LOG_FILENAME=aiogram_bot.log

cd /usr/projects/aiogram-bot
source bin/activate
nohup python ./aiogram_bot.py &