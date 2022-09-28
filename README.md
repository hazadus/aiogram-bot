# aiogram bot
Telegram bot template built using aiogram library.

## References
- [aiogram docs](https://docs.aiogram.dev/en/latest/)
- [aiogram on GitHub](https://github.com/aiogram/aiogram)

## Installation
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
export BOT_TOKEN=TelegramBotToken
export BOT_ADMIN=Bot-AdminChatID

cd /usr/projects/aiogram-bot
source bin/activate
nohup python ./aiogram_bot.py &
```
Then `chmod a+x ./run_bot.sh`.

## Running
```bash
$ ./run_bot.sh
```