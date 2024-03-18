# Работа с Базой данных
_____
В данном коде реализован проект по парсингу Youtube каналов, видео с каналов, с добавлением данных в базу данных
______
## Структура проекта
Проект состоит из папки 'utils', файла 'main.py' и файла 'config.py'
______
### utils:
В папке имеется файл 'utils.py' который отвечает за парсинг сайта 'youtube', создание базы данных, создание таблиц в базе данных, заполнение таблиц данными.</br>
1. Функция 'get_yuotube_date': Получение данных о каналах и видео с помощью API YouTube,
2. Функция 'create_database': Создание базы данных и таблиц для сохранения данных о каналах и видео,
3. Функция 'save_data_to_database': Сохранение данных о каналах и видео в базу данных
____
### main.py 
Внутри файла находится функция 'main', которая принимает в переменную 'channel_ids', список с id каналами из Youtube, так же с этого файла происходит запуск программы. 
____
### config.py
Внутри файла находится функция 'config'. В данной функции прописан скрипт подключения к базе данных. Подключения происходит при помощи вспомогательного файла database.ini
_____
## Запуск проекта
Чтобы проект корректно заработал на вашем ПК необходимо: 
1. Клонировать проект себе в репозиторий и локально на ПК
```
git@github.com:Meatdam/YouTube_from_database_parser.git
```
2. Установить все зависимости к себе на ПК с файла 'requirements.txt'
```
pip install -r requirements.txt
```
3. Заполнить корректно в файле 'database.ini', данными с вашей БД в переменную
```
host=<localhost> как правило 
user=<ваше имя зарегестрированного в postgreSQL>
password=<Ваш пороль от БД>
port=<5432> как правило
```
Название БД которуй вы захотите создать у себя локально можно прописать в файле 'main.py' в 'create_database'. По умолчанию название задано 'youtube'
