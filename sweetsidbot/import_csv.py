import csv
import sqlite3

conn = sqlite3.connect('recipes.db')
cursor = conn.cursor()

table_name_1 = 'tort'
table_name_2 = 'capcake'

csv_file_1 = 'recipes_tort.csv'
csv_file_2 = 'recipes_capcake.csv'
# ЧЕРЕЗ словарь

cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {table_name_1} (
        Название TEXT,
        Рецепт TEXT,
        Команда TEXT
    );
''')
cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {table_name_2} (
        Название TEXT,
        Описание TEXT,
        Команда TEXT
    );
''')

with open(csv_file_1, 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    for row in csv_reader:
        cursor.execute(f'''
            INSERT INTO {table_name_1} (Название, Рецепт, Команда)
            VALUES (?, ?, ?);
        ''', (row[0], row[1], row[2]))

with open(csv_file_2, 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    for row in csv_reader:
        cursor.execute(f'''
            INSERT INTO {table_name_2} (Название, Описание, Команда)
            VALUES (?, ?, ?);
        ''', (row[0], row[1], row[2]))

conn.commit()
conn.close()

print(f'Data from {csv_file_1} imported to {table_name_1} in the database.')
print(f'Data from {csv_file_2} imported to {table_name_2} in the database.')

