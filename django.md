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
from django.db import models

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

#### Редактирование views

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
  Classnames Title
{% endblock %}

{% block content %}
  {% for var in vars %}
    <h1>
      {{ var.field1 }} # обращение к атрибуту экзапляра класса
    </h1>
    <p>
      {{ var.field2|truncatewords:15}} # фильтр шаблона
    </p>
    <p>
      { post.date_pub }}
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
    path('', func_name), name="func_name_url") # добавить атрибут name
]
```

Добавить ссылку в шаблон

_templates/base.html_
```
<a href="{% url 'func_name_url'%}">Name</a>
```

#### Отображение внутренного содержимого объектов через sluq

Добавить шаблон пути

_appname/urls.py_
```
from django.urls import path

from .views import *

urlpatterns = [
    path('', func_name), name="func_name_url"),
    path('classname/<str:slug>/'б func_detail, name='classname_detail_url') # в квадратных скобках именованнная группа символов, явно указан тип. func_detail - функция обрабатывающая запросы по этому урлу. name- имя шаблона урла.

]
```
Добавить функцию в views

_appname/views.py_

```
from django.shortcuts import render
from .models import Classname

def func_name(request):
  vars = Classname.objects.all()
  return render(request, 'appname/index.html) context={'vars': vars}

def func_detail(request, slug):
    var = Classname.objects.get(slug__iexact=slug)
    return render(request, 'appname/classname_detail.html', context={'var': var})
```

Создать шаблон

appname/templates/appame/classname_detail.html

```
{% extends 'appname/base_appname.html' %}

{% block title %}
  {{ classname.title }} - {{ block.super }} # через девис будет отображаться дефолтное содержание из родительского шаблона
{% endblock %}

{% block content %}
  <h1>
    {{ classname.title }}
  </h1>
  <p>
    {{ classname.body }}
  </p>
{% endblock %}
```
Добавить ссылку в индексный шаблон

_appname/templates/appame/index.html_

```
{% extends 'appname/base_appname.html' %}

{% block title %}
  Some Title
{% endblock %}

{% block content %}
  {% for var in vars %}
  --/--/--
  --/--/--
  --/--/--
    <a href="{% url "classname_detail_url", slug=classname.slug %} }}">Read</a>
  {% endfor %}
{% endblock %}
```

Чтобы упростить запись ссылки и не запоминать все параметры урлов, нужно добавить специальный метод

_appname/models.py_
```
--/--/--
from django.shortcuts import reverse

class Classname(models.Model):
    --/--/--
    --/--/--

    def get_absolute_url(self):
    return reverse('classname_detail_url', kwargs={'slug': self.slug}) # возвращает ссылку на конкретный экземпляр класса

    --/--/--
    --/--/--
```

А в шаблоне заменить ссылку

_appname/templates/appame/index.html_

```
<a href="{% url "classname_detail_url", slug=classname.slug %} }}">Read</a>
```
на
```
<a href="{{ classname.get_absolute_url }}">Read</a>
```
### Тэги

#### Добавить класс _Tag_

_appname/models.py_
```
--/--/--
    --/--/--

class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return '{}'.format(self.title)

```
Установить связь между основной моделью и моделью тэг

_appname/models.py_

```
class Classname(models.Model):
    field1 = models.CharField(max_length=150, db_index=True)
    field2 = models.SlugField(max_length=150, unique=True)
    field3 = models.TextField(blank=True, db_index=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts') # 'Tag' - название класса, с которым нужно установить связь. blank=True - чтобы свойство tags не было обязательным для модели. related_name='posts' - свойство, которое появиться у экземпляром класса тэг (если не указать указать, то сгенерируется "post_set")
    field4 = models.DateTimeField(auto_now_add=True)

    --/--/--
```

Создание файла миграции и применение миграции
```
./manage.py makemigrations
./manage.py migrate
```

#### Проверка в консоле

Импортировать все модели
```
from appname.models import *
```
Добавить тэг
```
t = Tag.objects.create(title='Text', slug='text')
```
Выбрать объект сновной модели для добавления тэга
```
p = Classname.objects.get(field1="Value1")
```
Добавить значение тэга
```
p.tags.add(t)
```
Все тэги объекта
```
p.tags.all()
```
Связанные с тэгом посты
```
t.posts.all()
```

#### Настройка отображения страницы Tags

Добавить шаблон пути

_appname/urls.py_

```
from django.urls import path

from .views import *

urlpatterns = [
    path('', func_name), name="func_name_url"),
    path('classname/<str:slug>/'б func_detail, name='classname_detail_url')
    path('tags/', tags_list, name='tags_list_url')
]
```

Добавить функцию в views

_appname/views.py_

```
from django.shortcuts import render
from .models import Classname, Tag # добавить модель Tag

--/--/--
    --/--/--

--/--/--
    --/--/--

def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'appname/tags_list.html', context={'tags': tags})
```

Добавить шаблон

_appname/templates/appame/tags_list.html_

```
{% extends 'appname/base_appname.html' %}

{% block title %}
  Tags list - {{ block.super }}
{% endblock %}

{% block content %}
  <h1>Tags</h1>

    {% for tag in tags %}
      <h3>{{ tag.title }}</h3>
    {% endfor %}

{% endblock %}

```
Добавить ссылку на тэги в базовый шаблон проекта

_templates/base.html_

```
<a href="{% url 'tags_list_url'%}">Tags</a>
```
#### Настройка отображения страницы тэга
Добавить шаблон пути

_appname/urls.py_

```
from django.urls import path

from .views import *

urlpatterns = [
    path('', func_name), name="func_name_url"),
    path('classname/<str:slug>/'б func_detail, name='classname_detail_url')
    path('tags/', tags_list, name='tags_list_url')
    path('tag/<str:slug>/', tag_detail, name='tag_detail_url')
]
```
Добавить функцию в views

_appname/views.py_

```
from django.shortcuts import render
from .models import Classname, Tag # добавить модель Tag

--/--/--
    --/--/--

--/--/--
    --/--/--

--/--/--
    --/--/--

def tag_detail(request, slug):
    tag = Tag.objects.get(slug__iexact=slug)
    return render(request, 'appname/tag_detail.html', context={'tag': tag})

```


Добавить шаблон

_appname/templates/appame/tags_list.html_

```
{% extends 'blog/base_blog.html'%}

{% block title %}
  {{ tag_detail_url.title }} - {{ block.super }}
{% endblock %}

{% block content %}
  <h1>Post with "{{ tag.title|title }}" tag:</h1> # фильтр title изменяет первую букву на заглавную

  {% for post in tag.posts.all %}
        {{ post.date_pub }}
        {{ post.title }}
        {{ post.body|truncatewords:15
        <a href="{{ post.get_absolute_url }}">Read</a>
  {% endfor %}

{% endblock %}
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
Вернуть все объекты
```
Classname.objects.all()
```
Вернуть все объекты со значениями
```
Classname.objects.values()
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
##### Изменить какое-нибудь значение

```
p = Classname.objects.get(field1="Value1") # найти объект
p.field1 # проверить значение
p.field1 = 'new_value' # задать новое значение
p.save # сохранить
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
