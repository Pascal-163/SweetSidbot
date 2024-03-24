import csv
import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('recipes.db')  # Замените на вашу базу данных
cursor = conn.cursor()

# Замените 'your_table' на имя вашей таблицы в базе данных
table_name = 'tort'

# Замените 'your_data.csv' на имя вашего CSV файла
csv_file = 'recipes.csv'

# Создание таблицы, если её нет
cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {table_name} (
        Название TEXT,
        Рецепт TEXT,
        Команда TEXT
    );
''')

# Чтение данных из CSV файла и их запись в базу данных
with open(csv_file, 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Пропустить заголовок, если он есть
    for row in csv_reader:
        cursor.execute(f'''
            INSERT INTO {table_name} (Название, Рецепт, Команда)
            VALUES (?, ?, ?);
        ''', (row[0], row[1], row[2]))  # Используйте int(), чтобы преобразовать в целое число

# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()

print(f'Data from {csv_file} imported to {table_name} in the database.')
