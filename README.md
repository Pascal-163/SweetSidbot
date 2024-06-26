# Telegram бот SweetSidbot

## Описание проекта
Бот SweetSidbot - карманная книга рецептов. Бот помогает кондитеру-любителю всегда под рукой иметь нужные рецепты приготовления угощений.

## Стек, использованный при написании проекта
- SQL
- Python
- aiogram

## Запуск проекта в dev-режиме
- Создайте телеграм-бота и получите TOKEN

- Склонируйте репозиторий
```git clone git@github.com:Pascal-163/SweetSidbot.git```

- Установите и активируйте виртуальное окружение
```python -m venv venv```

```source venv/Scripts/activate```

- Установите зависимости
```pip install -r requirements.txt```

- Заполните файл .env (TOKEN)

- Создайте свою базу данных с рецептами в формате csv: нужны 3 колонки Название, Рецепт и Команда, которой будет вызван нужный рецепт

- Сделайте импорт данных в БД, например, sqlite3 с помощью скрипта import_csv.py
```python import_csv.py```

- Запустите бота
```python main.py```

## Планы на проект
- Добавить приветствие к команде /start
- Добавить команды /help, /allrecipes
- Добавить картинки рецептов
- Добавить простейшие вычисления: по заданной массе угощения пользователем выводится рецепт с уточнением требуемого количества (массы) ингредиентов
- Добавить расчет бухгалтерии, чтобы кондитер мог рассчитывать траты на ингредиенты и кешбек

## Автор проекта
Сидоров Алексей   
Telegram @pascal161   
aleksid92@gmail.com