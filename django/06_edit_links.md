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
