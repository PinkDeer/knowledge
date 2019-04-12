## Django

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

### Роутинг

Перенапраление запроса к приложению

_projectname/urls.py_
```
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('appname/', include('appname.urls')), # обращения по url 'appname/' обрабатываются 'appname.urls'
]
```
Подключение приложения

_projectname/settings.py_
```
INSTALLED_APPS = [
    ...
    'appname',
]
```
_appname/urls.py_
```
from django.urls import path

from .views import funcname # или 'from .views import *' для ипортирования всех функций из views.py

urlpatterns = [
    path('', funcname), # funcname - функция обрабатывающая запрос
]
```
_views.py_
```
def funcname(request):
  return
```
