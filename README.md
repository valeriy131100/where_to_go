# where_to_go

Карта Москвы с интересными местами и их описанием.

Пример сайта доступен по адресу [valeriy1311002.pythonanywhere.com](https://valeriy1311002.pythonanywhere.com/).

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

| Переменная            | Описание                                                                                   | Тип значения                                                              | Значение по умолчанию                                          |
|-----------------------|--------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|----------------------------------------------------------------|
| DEBUG                 | Режим дебага                                                                               | True/False                                                                | False                                                          |
| SECRET_KEY            | Секретный ключ Django                                                                      | Строка                                                                    | REPLACE_ME                                                     |
| ALLOWED_HOSTS         | IP-адреса, которые разрешено обслуживать серверу                                           | Список                                                                    | []                                                             |
| SECURE_SSL_REDIRECT   | Перенаправлять ли HTTP запросы на HTTPS                                                    | True/False                                                                | not DEBUG                                                      |
| SECURE_HSTS_SECONDS   | Если не 0, то устанавливает заголовок HTTP Strict Transport Security на все ответы сервера | Число секунд                                                              | 0                                                              |
| SESSION_COOKIE_SECURE | Использовать ли безопасные cookie                                                          | True/False                                                                | not DEBUG                                                      |
| CSRF_COOKIE_SECURE    | Указывает, использовать ли безопасные куки для CSRF                                        | True/False                                                                | not DEBUG                                                      |
| DATABASE_URL          | Строка подключения к базе данных                                                           | [dj-database-url](https://github.com/jacobian/dj-database-url#url-schema) | f'sqlite:///{BASE_DIR / "db.sqlite3"}'                         |
| LANGUAGE_CODE         | Код языка                                                                                  | Строка                                                                    | ru-ru                                                          |
| TIME_ZONE             | Часовой пояс                                                                               | Строка                                                                    | UTC                                                            |
| STATIC_URL            | Путь по которому на сайте будет доступна статика                                           | Строка                                                                    | /static/                                                       |
| STATIC_ROOT           | Путь до папки со статикой                                                                  | Строка                                                                    | Если DEBUG, то None, иначе str(BASE_DIR / 'static')            |
| STATICFILES_DIRS      | Дополнительные источники статики                                                           | Список                                                                    | []                                                             |
| MEDIA_URL             | Путь по которому на сайте будут доступны медиа-файлы                                       | Строка                                                                    | /media/                                                        |
| MEDIA_ROOT            | Путь до папки с медиа-файлами                                                              | Строка                                                                    | str(BASE_DIR / 'media')                                        |

</details>

После того как вы задали переменные среды необходимо применить миграции базы данных. Находясь в директории where_to_go исполните:
```bash
$ venv/bin/python manage.py migrate
```

## Загрузка данных о месте из JSON

Чтобы загрузить данные о месте из JSON-файла используйте команду:
```bash
$ venv/bin/python manage.py load_place https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/%D0%90%D0%BD%D1%82%D0%B8%D0%BA%D0%B0%D1%84%D0%B5%20Bizone.json
```

Можно передать несколько мест через пробел:
```bash
$ venv/bin/python manage.py load_place https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/%D0%94%D0%B8%D0%B7%D0%B0%D0%B9%D0%BD-%D0%BA%D0%B2%D0%B0%D1%80%D1%82%D0%B0%D0%BB%20%D0%A4%D0%BB%D0%B0%D0%BA%D0%BE%D0%BD.json https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/%D0%9A%D0%BE%D0%B2%D0%BE%D1%80%D0%BA%D0%B8%D0%BD%D0%B3%20Gravity.json
```

<details>
<summary>Пример JSON-а</summary>

```json
{
    "title": "Коворкинг Gravity",
    "imgs": [
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/40c9291aa02d8bf794918dde1cc86af1.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/d41624d956c8222962290f5af9c9aa09.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/1c6aad34e98200e8b5ba5c7998cd6a6b.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/3b5999fd66e1bab82d20f5edd599fd2f.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/01474fdd148f2276ecb953d793ffe782.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/3539ae1482ebc75107e81977f6db3a4e.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/fe9505faa385b1bd2dfacd8ccfa03b20.jpg"
    ],
    "description_short": "В этом коворкинге ваш бизнес, словно ракета, сбросит ступени, преодолеет притяжение неудач и вырвется на просторы вселенной успеха, где границы определяет только воображение. Гостям предоставляются не только рабочие места, но и мягкие диваны, настольные игры, мини-кухня и кафе-бар со вкусными авторскими блюдами.",
    "description_long": "<p>Динамичное время стартапов и креативных идей рождает уникальные места. Работайте в удобное вам время. Новый коворкинг Gravity рядом со станцией метро «Бауманская» меньше всего походит на скучный офис с «белыми воротничками», но предлагает функционал, без которого сложно представить идеальное рабочее место.</p><p>Яркий лофт с уникальными граффити и огромными окнами полон света и воздуха. Это пространство сотрудничества и общения, так что громоздким столам на десяток человек — да, а перегородкам и закуткам — нет! В вашем распоряжении —  безлимитный интернет, использование МФУ без ограничений, мягкие диваны, комната отдыха, кафе. Всегда можно обратиться к администратору за поддержкой. </p><p>Планируете встречу, презентацию, конференцию? Тогда обратите внимание на одну из двух переговорных комнат (на 8 или 12 человек). Командам из 7-8 человек подойдёт отдельная комната. Благодаря гибкой системе абонементов оплачивать визиты легко и выгодно. </p>",
    "coordinates": {
        "lng": "37.68049",
        "lat": "55.768522"
    }
}
```

Если место с координатами из JSON-а уже существует, то оно не будет создано.

</details>

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
