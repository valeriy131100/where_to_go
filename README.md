# where_to_go

Карта Москвы с интересными местами и их описанием.

## Установка
Вам понадобится установленный Python 3.7+ и git.

Склонируйте репозиторий:
```bash
$ git clone https://github.com/valeriy131100/where_to_go
```

Создайте в этой папке виртуальное окружение:
```bash
$ cd where_to_go
$ python3 -m venv venv
```

Активируйте виртуальное окружение и установите зависимости:
```bash
$ source venv/bin/activate
$ pip install -r requirements.txt
```

## Настройка перед использованием
Создайте файл .env и запишите туда параметры в формате `ПЕРЕМЕННАЯ=значение`или иным образом задайте переменные среды.
<details>
<summary>Список доступных переменных среды</summary>

| Переменная            | Описание                                                                                   | Тип значения                                                              | Значение по умолчанию                  |
|-----------------------|--------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|----------------------------------------|
| DEBUG                 | Режим дебага                                                                               | True/False                                                                | False                                  |
| SECRET_KEY            | Секретный ключ Django                                                                      | Строка                                                                    | REPLACE_ME                        |
| ALLOWED_HOSTS         | IP-адреса, которые разрешено обслуживать серверу                                           | Список                                                                    | []                                     |
| SECURE_SSL_REDIRECT   | Перенаправлять ли HTTP запросы на HTTPS                                                    | True/False                                                                | not DEBUG                              |
| SECURE_HSTS_SECONDS   | Если не 0, то устанавливает заголовок HTTP Strict Transport Security на все ответы сервера | Число секунд                                                              | 0                                      |
| SESSION_COOKIE_SECURE | Использовать ли безопасные cookie                                                          | True/False                                                                | not DEBUG                              |
| CSRF_COOKIE_SECURE    | Указывает, использовать ли безопасные куки для CSRF                                        | True/False                                                                | not DEBUG                              |
| DATABASE_URL          | Строка подключения к базе данных                                                           | [dj-database-url](https://github.com/jacobian/dj-database-url#url-schema) | f'sqlite:///{BASE_DIR / "db.sqlite3"}' |
| LANGUAGE_CODE         | Код языка                                                                                  | Строка                                                                    | ru-ru                                  |
| TIME_ZONE             | Часовой пояс                                                                               | Строка                                                                    | UTC                                    |
| STATIC_URL            | Путь по которому на сайте будет доступна статика                                           | Строка                                                                    | /static/                               |
| STATIC_ROOT           | Путь до папки со статикой                                                                  | Строка                                                                    | str(BASE_DIR / 'static')               |
| STATICFILES_DIRS      | Дополнительные источники статики                                                           | Список                                                                    | []                                     |
| MEDIA_URL             | Путь по которому на сайте будут доступны медиа-файлы                                       | Строка                                                                    | /media/                                |
| MEDIA_ROOT            | Путь до папки с медиа-файлами                                                              | Строка                                                                    | str(BASE_DIR / 'media')                |

</details>

После того как вы задали переменные среды необходимо применить миграции базы данных. Находясь в директории where_to_go исполните:
```bash
$ venv/bin/python manage.py migrate
```

## Запуск

Находясь в директории where_to_go исполните:
```bash
$ venv/bin/python manage.py runserver
```

По умолчанию сервер запустится на [127.0.0.1:8000](http://127.0.0.1:8000).

Вы можете указать в качестве параметра IP-адрес и порт для сервера:
```bash
$ venv/bin/python manage.py runserver 127.0.0.1:8000
```
