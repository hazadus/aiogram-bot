#!/bin/bash

# Set these env vars according to yours
export BOT_TOKEN=token
export BOT_ADMIN=chatid
export BOT_LOG_FILENAME=aiogram_bot.log
export BOT_SQLITE_FILENAME=aiogram_bot.db

python ./aiogram_bot.py