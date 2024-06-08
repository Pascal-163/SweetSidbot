import sqlite3


async def recipes(item):
    conn = sqlite3.connect('recipes.db')
    cursor = conn.cursor()

    cursor.execute("SELECT Название, Рецепт FROM tort WHERE Команда = ?",
                   (str(item),))
    # cursor.execute("SELECT Название, Рецепт FROM capcake WHERE Команда = ?",
    #                (str(item),))
    recipes_info = cursor.fetchall()
    conn.close()

    return recipes_info
