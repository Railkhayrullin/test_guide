# test_guide
Тестовое задание для ООО «КОMТEK»

## Установка:
Клонируем репозиторий на локальную машину:

    git clone https://github.com/Railkhayrullin/test_guide.git

Переходим в папку с проектом.

    cd test_guide

Устанавливаем виртуальное окружение и активируем его.

    python3 -m venv .env
    source .env/bin/activate

Устанавливаем зависимости.

    pip install -r requirements.txt

Устанавливаем PostgreSQL (если установлен, то переходим к следующей команде):

    sudo apt update
    sudo apt install postgresql

Входим в PostgreSQL

    sudo -u postgres psql

Создаем БД и пользователя в PostgreSQL:

    CREATE DATABASE comtek;
    CREATE USER comtek WITH PASSWORD 'comtek';


Зададим кодировку по умолчанию UTF-8, чего и ожидает Django.<br>
Также мы зададим схему изоляции транзакций по умолчанию «read committed»,<br>
которая будет блокировать чтение со стороны неподтвержденных транзакций.<br>

    ALTER ROLE comtek SET client_encoding TO 'utf8';
    ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';

Теперь мы предоставим созданному пользователю доступ для администрирования новой базы данных:

    GRANT ALL PRIVILEGES ON DATABASE comtek TO comtek;

Завершив настройку, закройте диалог PostgreSQL с помощью следующей команды:

        \q

Выполните миграции:

    python manage.py migrate

Создайте миграции моделей Django и примените их:

    python manage.py makemigrations
    python manage.py migrate

Создайте суперпользователя для возможности добавления справочников и элементов через админ-панель:

    python manage.py createsuperuser


## Запуск и остановка локального сервера

Запуск сервера.

    python manage.py runserver

Остановка сервера осуществляется с помощью комбинации клавиш:

    Ctr + C

### После запуска доступны следующие адреса:
Админ-панель для добавления справочников/элементов:

    127.0.0.1:8000/admin/

API эндпоинты:
```
GET   /guide/                                                                                - получение списка справочников 
GET   /guide/?date=*date                                                                     - получение списка справочников, актуальных на указанную дату 
GET   /element/?guide=*guide                                                                 - получение элементов заданного справочника текущей версии
GET   /element/?version=*version                                                             - получение элементов всех справочников указанной версии
GET   /element/?guide=*guide&version=*version                                                - получение элементов заданного справочника указанной версии
GET   /element-validation/?guide=*guide&code=*code&value=*value                              - валидация элементов заданного справочника текущей версии
GET   /element-validation/?guide=*guide&version=*version&code=*code&value=*value&date=*date  - валидация элементов заданного справочника по указанной версии
```
где:
  - *date - дата в формате yyyy-mm-dd
  - *guide - наименование справочника
  - *version - версия справочника
  - *code - код элемента
  - *value - значение елемента

### Особенности:
- При валидации элементов справочника возможно подставление указанных параметров в любой последовательности.
- Вывод результатов происходит постранично, по умолчанию 10 справочников/елементов на страницу.
- Для изменения числа справочников/элементов на странице поменять значение ключа `PAGE_SIZE` в словаре `REST_FRAMEWORK` в `test_guide/settings.py`
- Ссылки на следующую и предыдущую страницы доступны по ключу `next` и `previous` соответственно. 
