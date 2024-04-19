import csv
import sqlite3

conn = sqlite3.connect('recipes.db')
cursor = conn.cursor()

table_name = 'tort'

csv_file = 'recipes.csv'

cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {table_name} (
        Название TEXT,
        Рецепт TEXT,
        Команда TEXT
    );
''')

with open(csv_file, 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    for row in csv_reader:
        cursor.execute(f'''
            INSERT INTO {table_name} (Название, Рецепт, Команда)
            VALUES (?, ?, ?);
        ''', (row[0], row[1], row[2]))

conn.commit()
conn.close()

print(f'Data from {csv_file} imported to {table_name} in the database.')
