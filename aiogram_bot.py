import sys
import logging

from aiogram.utils import executor

from spawn_bot import dp
from handlers import client, admin, common


# Configure logger
logging.basicConfig(level=logging.INFO,
                    handlers=[
                        logging.FileHandler('aiogram_bot.log'),
                        logging.StreamHandler(sys.stdout)  # output to file AND console
                    ],
                    format="%(asctime)s - %(levelname)s\t%(module)s/%(funcName)s:%(lineno)d\t- %(message)s",
                    datefmt='%d/%m/%Y %H:%M:%S',
                    )


async def on_startup(_):
    logging.info('Bot started.')


client.register_client_handlers(dp)
admin.register_admin_handlers(dp)
common.register_common_handlers(dp)

executor.start_polling(dp,
                       skip_updates=True,  # Skip updates when bot is offline
                       on_startup=on_startup)
