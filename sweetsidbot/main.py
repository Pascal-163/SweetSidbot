import asyncio
import os
from aiogram import Bot, Dispatcher, executor

from dotenv import load_dotenv

load_dotenv()

loop = asyncio.new_event_loop()
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
bot = Bot(TELEGRAM_BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, loop=loop)

if __name__ == '__main__':
    from handlers import dp
    executor.start_polling(dp)
