# test_task_appevent
Тестовое задание AppEvent

Что есть:

Скрипт парсит сайт https://news.ycombinator.com/ с периодичностью 5 минут, используя crontab (настройки задаются в settings.py список CRONJOBS).
Имеется возможность спарсить сайт по нажатию кнопки в административной панели.

API:

<поле> - доступны поля id, title, created (можно поменять в site_parser.views поле ordering_fields)
<br><число> - какое-то число

<br>http://127.0.0.1:8000/posts - по умолчанию показывает 5 постов
<br>http://127.0.0.1:8000/posts?ordering=<поле> - фильтрация по полю
<br>http://127.0.0.1:8000/posts?limit=<число> - установление лимита
<br>http://127.0.0.1:8000/posts?offset=<число> - установление сдвига
<br>http://127.0.0.1:8000/posts?ordering=<поле>&limit=<число>&offset=<число> - можно комбинировать при помощи символа &

Инструкция по запуску:

1. Склонировать репозиторий
2. Создать и подключится к виртуальному окружению
2. Прописать:
    <br>2.1 pip3 install -r requirements.txt
    <br>2.2 python manage.py migrate
    <br>2.3 python manage.py crontab add 
3. Запустить при помощи python manage.py runserver
