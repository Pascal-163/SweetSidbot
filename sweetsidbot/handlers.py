from aiogram.types import Message
from aiogram.dispatcher.filters import Command

from main import dp
from sql import recipes


@dp.message_handler(Command('persik'))
async def get_recipes(message: Message):

    print('Получаем значение команды')
    item = message.text.split(maxsplit=1)
    print(item)

    if not item:
        await message.answer("Пожалуйста, укажите название рецепта.")
        return

    # Получаем информацию о рецепте из базы данных по указанному названию
    recipe_info = await recipes(item)

    print(recipe_info)

    if not recipe_info:
        await message.answer("Рецепт не найден.")
        return

    if len(recipe_info) < 2:
        await message.answer("Информация о рецепте неполная.")
        return

    recipe_name = recipe_info[0]
    recipe_ingredients = recipe_info[1]

    # Отправляем информацию о рецепте пользователю
    await message.answer(f"Рецепт: {recipe_name}\nИнгредиенты: {recipe_ingredients}")
