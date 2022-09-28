# aiogram bot
Telegram bot template built using aiogram library.

## Contents
 * [Deployment](#deployment)
 * [Running](#running)
 * [References](#references)

## Deployment
```bash
$ cd /usr/projects
$ git clone https://github.com/hazadus/aiogram-bot
$ virtualenv aiogram-bot
$ cd ./aiogram-bot
$ source bin/activate
$ pip install -r requirements.txt
```
Edit `run_bot.sh`:
```bash
#!/bin/bash

# Set these env vars according to yours
# Your bot's token:
export BOT_TOKEN=TelegramBotToken
# Your telegram ID:
export BOT_ADMIN=BotAdminChatID
export BOT_LOG_FILENAME=aiogram_bot.log

cd /usr/projects/aiogram-bot
source bin/activate
nohup python ./aiogram_bot.py &
```
Then `chmod a+x ./run_bot.sh`.

## Running
```bash
$ ./run_bot.sh
```

## References
- [aiogram docs](https://docs.aiogram.dev/en/latest/)
- [aiogram on GitHub](https://github.com/aiogram/aiogram)
- [Python Hub Studio - aiogram video lessons](https://www.youtube.com/watch?v=TYs3-uyjC30&list=PLNi5HdK6QEmX1OpHj0wvf8Z28NYoV5sBJ)
