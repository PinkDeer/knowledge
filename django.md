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

from .views import func_name # или 'from .views import *' для ипортирования всех функций из views.py

urlpatterns = [
    path('', func_name), # func_name - функция обрабатывающая запрос
]
```
_views.py_
```
def func_name(request):
  return render(request, 'appname/index.html) # подключение шаблона
```

### HTML шаблоны

Папка с шаблонами: _appname/templates/appame_
Первый шаблон: _appname/templates/appame/index.html_


#### Полезное

**Обработка списка в цикле**

В _views.py_ объявление переменной
```
from django.shortcuts import render

def func_name(request):
    n = ['1', '2', '3'] # объявление переменной
    return render(request, 'appaname/index.html', context={'var': n}) # ключ var со значением n - это переменная которая будет использоваться в шаблоне
```
В шаблоне:
```
{% for i in var %}
  <p>
    {{ i }}
  </p>
{% endfor %}
```
