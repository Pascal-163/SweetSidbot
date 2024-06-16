from aiogram.types import Message
from main import dp
from sql import recipes
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


@dp.message_handler(commands=('krasnujbarchat', 'persik', 'rafaello',
                              'tiramisu', 'serdce'))
async def get_recipes(message: Message):

    item = message.text.split()

    if not item:
        await message.answer("Сообщение не содержит команды.")
        return

    recipe_name = item[0]
    recipe_info = await recipes(recipe_name)

    if recipe_info is None:
        await message.answer("Рецепт не найден. Проверьте правильность"
                             "написания.")
    else:
        await message.answer(f"Рецепт: {recipe_info}")
