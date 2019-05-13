## Django
ver 2.2

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
_appname/views.py_
```
from django.shortcuts import render

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

Базовый шаблон проекта _templates/base.html_
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

#### Создание модели

Типы полей: [2.2 eng](https://docs.djangoproject.com/en/2.2/ref/models/fields/) | [1.9 rus](https://djbook.ru/rel1.9/ref/models/fields.html)

Пример _appname/models.py_
```
class Classname(models.Model):
    field1 = models.CharField(max_length=150, db_index=True)
    field2 = models.SlugField(max_length=150, unique=True)
    field3 = models.TextField(blank=True, db_index=True)
    field4 = models.DateTimeField(auto_now_add=True)

    # специальный метод для вывода в консоль конкретного экземляра класса
    # вместо адреса объекта. Метод _str_ отвечает за вывод информации объекте
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

#### Редактирование контроллера

_appname/views.py_

```
from django.shortcuts import render
from .models import Classname # импортировать модель

def func_name(request):
  vars = Classname.objects.all() # обращение к менеджеру модели
  return render(request, 'appname/index.html) context={'vars': vars} # ключ vars принимает значение переменной vars
```

Объекты можно добавить через консоль

#### Редактирование индексного шаблона

Обработка списка объектов в цикле

_appname/templates/appame/index.html_

```
{% extends 'appname/base_appname.html' %}

{% block title %}
  Some Title
{% endblock %}

{% block content %}
  {% for var in vars %}
    <h1>
      {{ var.field1 }} # обращение к атрибуту экзапляра класса
    </h1>
    <p>
      {{ var.field2|truncatewords:15}} # фильтр шаблона
    </p>
  {% endfor %}
{% endblock %}
```

[Подробнее](https://docs.djangoproject.com/en/2.2/ref/templates/builtins/) про фильтры шаблона

### Редактирование ссылок в базовом шаблоне

Присвоить имя шаблону урла

_appname/urls.py_
```
from django.urls import path

from .views import *

urlpatterns = [
    path('', func_name), name="func_name_url" # добавить атрибут name
]
```

Добавить ссылку в шаблон

_templates/base.html_
```
<a href="{% url 'func_name_url'%}">Name</a>
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

Создать экземлпяр класса
```
p = Classname(field1="value1", field1="value2"...)
```
Вывод экземлпяра класса (благодаря def __str__(self))
```
p
```
Сохранение в базу данных
```
p.save()
```
Id экземпляра модели
```
p.id
```
Атрибуты класса
```
dir(p)
```
Создание экземпляра класса с помощью атрибута _objects_ (метод _save()_ не нужно)
```
p2 = Classname.objects.create(field1="value1", field1="value2"...)
```
Вывести все объекты
```
Classname.objects.all()
```
Вернуть объект с определённым значением
```
p3 = Classname.objects.get(field1="value1")
```
Вернуть объект с определённым значением независимо от регистра
```
p4 = Classname.objects.get(field1__iexact="Value1")
```
Вернуть объект/объекты содержащие определенное значение
```
p5 = Classname.objects.filter(field1__contains="Val")
```

#### Обработка списка в цикле

В _appname/views.py_ объявление переменной
```
from django.shortcuts import render

def func_name(request):
    n = ['1', '2', '3'] # объявление переменной
    return render(request, 'appaname/index.html', context={'var': n}) # ключ var со значением n - это переменная которая будет использоваться в шаблоне
```
В шаблоне _appname/templates/appame/index.html_
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
