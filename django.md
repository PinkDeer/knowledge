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

Шаблон: _appname/templates/appame/index.html_
```
{% extends 'appname/base_appname.html' %} # подключение базового шаблона приложения

{% block title %}
  Some Title
{% endblock %}

{% block content %}
  Some Content
{% endblock %}
```
Базовый шаблон приложения _appname/templates/appname/base_appname.html_
```
{% extends '../base.html'%} # подключение базового шаблона проекта
```
Необходимо подключение базового шаблона проекта
_projectname/settings.py_
```
TEMPLATES = [
    {
        ...
        'DIRS': [
            os.path.join(BASE_DIR, 'templates') # BASE_DIR - абсолютный путь до проекта
        ],
        ...
        },
    },
]
```

Базовый шаблон проекта _templates/base.html_:
```
<!DOCTYPE html>
<html lang="en" dir="ltr">

  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>

      {% block title %}
        Project Name  # контент по умолчанию. Будет использоваться, если в шаблоне не определено значение
      {% endblock %}

    </title>
  </head>

  <body>

    {% block content %}
      There is no any content for you
    {% endblock %}

  </body>
</html>

```

### Модели

[Типы полей](https://docs.djangoproject.com/en/2.2/ref/models/fields/)

Пример
```
class Classname(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    body = models.TextField(blank=True, db_index=True)
    date_pub = models.DateTimeField(auto_now_add=True)

    # специальный метод для вывода в консоль конкретного экземляра класса вместо адреса объекта
    def __str__(self):
        return '{}'.format(self.title)
```
Создание файла миграции
```
./manage.py makemigrations
```
Применение миграции к базе данных
```
./manage.py migrate
```

### Полезное

#### Консоль
Открыть консоль
```
./manage.py shell
```
Импортирование модели
```
from appname.models import Classname
```

#### Обработка списка в цикле

В _appname/views.py_ объявление переменной
```
from django.shortcuts import render

def func_name(request):
    n = ['1', '2', '3'] # объявление переменной
    return render(request, 'appaname/index.html', context={'var': n}) # ключ var со значением n - это переменная которая будет использоваться в шаблоне
```
В шаблоне _appname/templates/appame/index.html_:
```
{% for i in var %}
  <p>
    {{ i }}
  </p>
{% endfor %}
```
#### Переменная BASE_DIR

_projectname/settings.py_
```
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
```
*Детальный разбор:*

В корне проекта открыть пайтон
```
python3
```
Подключить модуль os
```
import os
```
Создать переменную base, в атрибуте указать название файла
```
base = os.path.dirname(os.path.dirname(os.path.abspath('settings.py')))
base
```
Абсолютный путь до папки с проектом
```
os.path.join(base, 'templates')
```
