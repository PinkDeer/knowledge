### Виртуальное окружение

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

### Установка Django и первые шаги

Установка Django
```
pip install django
```
Создание проекта
```
django-admin startproject projectname
```
Создание приложения
```
cd projectname
python manage.py startapp appname
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
