import os

import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from dotenv import load_dotenv
import message_texts

# import telebot
# import sqlite3


# bot = telebot.TeleBot('6113793338:AAHcxo-4cGldzKqTgFpqDT2sWoJcEXVrqVc')

load_dotenv()

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
if not TELEGRAM_BOT_TOKEN:
    exit('Specify TELEGRAM_BOT_TOKEN env variable')


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    effective_chat = update.effective_chat
    if not effective_chat:
        logger.warning("effective_chat is None in /start")
        return
    await context.bot.send_message(
            chat_id=effective_chat.id,
            text=message_texts.GREETINGS
    )


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    effective_chat = update.effective_chat
    if not effective_chat:
        logger.warning("effective_chat is None in /help")
        return
    await context.bot.send_message(
            chat_id=effective_chat.id,
            text=message_texts.HELP
    )


async def tort(update: Update, context: ContextTypes.DEFAULT_TYPE):
    effective_chat = update.effective_chat
    if not effective_chat:
        logger.warning("effective_chat is None in /tort")
        return
    await context.bot.send_message(
            chat_id=effective_chat.id,
            text=message_texts.TORT
    )

   
# @bot.callback_query_handler(func=lambda id: True)
# def get_all_recipes(id):
#     try:
#         conn = sqlite3.connect('recipes1.db')
#         cursor = conn.cursor()
#         print("Подключен к SQLite")

#         sql_select_query = """SELECT * FROM tort"""
#         cursor.execute(sql_select_query)
#         records = cursor.fetchall()
#         print("Вывод всех рецептов")

#         info = ''
#         for row in records:
#             info += f"ID: {row[0]}\nНазвание: {row[1]}\nРецепт: {row[2]}\nКоманда: {row[3]}\n\n"

#     except sqlite3.Error as error:
#         print("Ошибка при работе с SQLite", error)
#     finally:
#         if conn:
#             conn.close()
#             print("Соединение с SQLite закрыто")

#     bot.send_message(id.message.chat.id, info)


if __name__ == '__main__':
    application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    help_handler = CommandHandler('help', help)
    application.add_handler(help_handler)

    tort_handler = CommandHandler('tort', tort)
    application.add_handler(tort_handler)

    application.run_polling()
