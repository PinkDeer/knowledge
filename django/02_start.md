### Виртуальное окружение и установка Django

Для использования изолированной среды с определенными версиями приложений необходимо создать виртуальное окружение

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

### Создание проекта и приложения

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
