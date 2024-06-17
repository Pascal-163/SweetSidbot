from aiogram.types import Message
from main import dp
from sql import recipes
<<<<<<< HEAD
# import logging
# from telegram import Update
# from telegram.ext import ContextTypes
# import message_texts


# async def tort(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     effective_chat = update.effective_chat
#     # if not effective_chat:
#     #     logger.warning("effective_chat is None in /tort")
#     #     return
#     await context.bot.send_message(
#             chat_id=effective_chat.id,
#             text=message_texts.TORT
#     )
=======
import message_texts
>>>>>>> 340cd2040674f6cc6fa69f70281012c521b4b34a


@dp.message_handler(commands=["start"])
async def start(message: Message):
    await message.answer(message_texts.GREETINGS)


@dp.message_handler(commands=["help"])
async def help_handler(message: Message):
    await message.answer(message_texts.HELP)


@dp.message_handler(commands=["tort"])
async def tort_handler(message: Message):
    await message.answer(message_texts.TORT)


@dp.message_handler(commands=["capcake"])
async def capcake_handler(message: Message):
    await message.answer(message_texts.CAPCAKE)


@dp.message_handler(commands=None)
async def get_recipes(message: Message):

    item = message.text.split()

    if not item:
        await message.answer("Сообщение не содержит команды.")
        return

    recipe_name = item[0]
    recipe_info = await recipes(recipe_name)

    if not recipe_info or len(recipe_info[0]) == 0:
        await message.answer("Рецепт не найден в сборнике. Проверьте "
                             "правильность написания и сравните со списком "
                             "доступных рецептов /tort, /capcake")
    else:
        await message.answer(f"Рецепт: \n {recipe_info}")

# - Добавить картинки рецептов
# сделать кнопки старт, хелп, списки рецептов