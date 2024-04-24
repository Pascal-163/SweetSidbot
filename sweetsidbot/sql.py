import sqlite3


async def recipes(item):
    conn = sqlite3.connect('recipes.db')
    cursor = conn.cursor()

    cursor.execute("SELECT Рецепт FROM tort WHERE Команда = ?", (str(item),))
    recipes_info = cursor.fetchall()
    conn.close()

    return recipes_info
