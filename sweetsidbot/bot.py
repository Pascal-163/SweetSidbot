from aiogram import types, Dispatcher
# import os

# import logging
# from telegram import Update
# from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
# from dotenv import load_dotenv
# import message_texts

import telebot
import sqlite3
bot = telebot.TeleBot('6113793338:AAHcxo-4cGldzKqTgFpqDT2sWoJcEXVrqVc')

# load_dotenv()

# logging.basicConfig(
#     format='%(asctime)s - %(levelname)s - %(message)s',
#     level=logging.INFO
# )
# logger = logging.getLogger(__name__)

# TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
# if not TELEGRAM_BOT_TOKEN:
#     exit('Specify TELEGRAM_BOT_TOKEN env variable')

dp = Dispatcher(bot)


# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     effective_chat = update.effective_chat
#     if not effective_chat:
#         logger.warning("effective_chat is None in /start")
#         return
#     await context.bot.send_message(
#             chat_id=effective_chat.id,
#             text=message_texts.GREETINGS
#     )


# async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     effective_chat = update.effective_chat
#     if not effective_chat:
#         logger.warning("effective_chat is None in /help")
#         return
#     await context.bot.send_message(
#             chat_id=effective_chat.id,
#             text=message_texts.HELP
#     )


# async def tort(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     effective_chat = update.effective_chat
#     if not effective_chat:
#         logger.warning("effective_chat is None in /tort")
#         return
#     await context.bot.send_message(
#             chat_id=effective_chat.id,
#             text=message_texts.TORT
#     )


@dp.message_handler(commands=['recipes'])
async def get_recipes(message: types.Message):
    conn = sqlite3.connect('recipes.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tort")
    recipes = cursor.fetchall()

    recipes_str = "\n".join([str(recipe) for recipe in recipes])

    await message.answer(recipes_str)

    conn.close()


# if __name__ == '__main__':
    # application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    # start_handler = CommandHandler('start', start)
    # application.add_handler(start_handler)

    # help_handler = CommandHandler('help', help)
    # application.add_handler(help_handler)

    # tort_handler = CommandHandler('tort', tort)
    # application.add_handler(tort_handler)

    # application.run_polling()
