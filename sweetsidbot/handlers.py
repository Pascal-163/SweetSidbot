from aiogram.types import Message
from main import dp
from sql import recipes


@dp.message_handler(commands=None)
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
