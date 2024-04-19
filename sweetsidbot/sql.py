import sqlite3


async def recipes(item):
    conn = sqlite3.connect('recipes.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tort WHERE Команда = ?", (str(item[1]),))
    print('Печать из sql')
    print(item)
    recipes_info = cursor.fetchall()
    conn.close()

    return recipes_info
