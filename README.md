# aiogram bot
Telegram bot template built using aiogram library.

## Contents
 * [Deployment](#deployment)
 * [Running](#running)
 * [References](#references)
 * [ToDos](#todos)

## Deployment
Use following commands to deploy bot on Linux/Mac OS X system:
```bash
$ cd /usr/projects
$ git clone https://github.com/hazadus/aiogram-bot
$ virtualenv aiogram-bot
$ cd ./aiogram-bot
$ source bin/activate
$ pip install -r requirements.txt
```


## Running
### Server Mode
Edit `run_bot.sh`:
```bash
#!/bin/bash

# Set these env vars according to yours
# Your bot's token:
export BOT_TOKEN=TelegramBotToken
# Your telegram ID:
export BOT_ADMIN=BotAdminChatID
export BOT_LOG_FILENAME=aiogram_bot.log
export BOT_SQLITE_FILENAME=aiogram_bot.db

cd /usr/projects/aiogram-bot
source bin/activate
nohup python ./aiogram_bot.py &
```
Then `chmod a+x ./run_bot.sh`.
To start the bot in production mode:
```bash
$ ./run_bot.sh
```
### Dev/Debug Mode
Edit `run_bot_d.sh`:
```bash
#!/bin/bash

# Set these env vars according to yours
export BOT_TOKEN=token
export BOT_ADMIN=chatid
export BOT_LOG_FILENAME=aiogram_bot.log
export BOT_SQLITE_FILENAME=aiogram_bot.db

python ./aiogram_bot.py
```
Then `chmod a+x ./run_bot_d.sh`.
To start the bot in dev/debug mode:
```bash
$ ./run_bot_d.sh
```

## References
- [aiogram docs](https://docs.aiogram.dev/en/latest/)
- [aiogram on GitHub](https://github.com/aiogram/aiogram)
- [Python Hub Studio - aiogram video lessons playlist](https://www.youtube.com/watch?v=TYs3-uyjC30&list=PLNi5HdK6QEmX1OpHj0wvf8Z28NYoV5sBJ)
- [Python Hub Studio - aiogram inline buttons overview](https://www.youtube.com/watch?v=gpCIfQUbYlY&list=PLNi5HdK6QEmX1OpHj0wvf8Z28NYoV5sBJ&index=10)
- [SQLite Tutorial](https://www.sqlitetutorial.net)

## ToDos
  * aiosqlite
 * aioredis
 * save new user info to DB table
 * add user cart
