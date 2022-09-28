#!/bin/bash

# Set these env vars according to yours
export BOT_TOKEN=TelegramBotToken
export BOT_ADMIN=Bot-AdminChatID

cd /usr/projects/aiogram-bot
source bin/activate
nohup python ./aiogram_bot.py &