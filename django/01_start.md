### Виртуальное окружение и установка Django

Создание
```
python3 -m venv name
```
Активация
```
source name/bin/activate
```
Деактивация
```
deactivate
```
Удаление
```
rm -r name
```
Установка Django
```
pip install django
```

### Создание проета и приложения

Создание проекта
```
django-admin startproject blogdjango
```
Создание приложения
```
cd blogdjango
python manage.py startapp blog
```
Запуск сервера
```
./manage.py runserver
# по умолчанию 8000 порт, можно указать явно другой
# ./manage.py runserver 4000
```
Или другой командой
```
python manage.py runserver
```
Применение миграций
```
./manage.py migrate
```
