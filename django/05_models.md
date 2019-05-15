#### Создание модели

Типы полей: [2.2 eng](https://docs.djangoproject.com/en/2.2/ref/models/fields/) | [1.9 rus](https://djbook.ru/rel1.9/ref/models/fields.html)

Пример _blog/models.py_
```
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    body = models.TextField(blank=True, db_index=True)
    date_pub = models.DateTimeField(auto_now_add=True)

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

_blog/views.py_

```
from django.shortcuts import render
from .models import Post # импортировать модель

def posts_lis(request):
  vars = Post.objects.all() # обращение к менеджеру модели
  return render(request, 'blog/index.html) context={'posts': posts} # ключ posts принимает значение переменной posts
```

Объекты можно добавить через консоль

#### Редактирование индексного шаблона

Обработка списка объектов в цикле

_blog/templates/blog/index.html_

```
{% extends 'appname/base_appname.html' %}

{% block title %}
  Classnames Title
{% endblock %}

{% block content %}
  {% for post in posts %}
    <h1>
      {{ post.title }} # обращение к атрибуту экзапляра класса
    </h1>
    <p>
      {{ post.body|truncatewords:15}} # фильтр шаблона
    </p>
    <p>
      { post.date_pub }}
    </p>
  {% endfor %}
{% endblock %}
```

[Подробнее](https://docs.djangoproject.com/en/2.2/ref/templates/builtins/) про фильтры шаблона
