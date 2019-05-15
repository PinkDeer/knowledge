#### Редактирование ссылок в базовом шаблоне

Присвоить имя шаблону урла

_blog/urls.py_
```
from django.urls import path

from .views import *

urlpatterns = [
    path('', posts_list), name="posts_list_url") # добавить атрибут name
]
```

Добавить ссылку в шаблон

_templates/base.html_
```
<a href="{% url 'posts_list_url'%}">Posts</a>
```

#### Отображение внутренного содержимого объектов через sluq

Добавить шаблон пути

_blog/urls.py_
```
from django.urls import path

from .views import *

urlpatterns = [
    path('', posts_list), name="posts_list_url"),
    path('post/<str:slug>/', post_detail, name='classname_detail_url') # в квадратных скобках именованнная группа символов, явно указан тип. post_detail_url - функция обрабатывающая запросы по этому урлу. name- имя шаблона урла.

]
```
Добавить функцию в views

_blog/views.py_

```
from django.shortcuts import render
from .models import Post

def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts})

def post_detail(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    return render(request, 'blog/post_detail.html', context={'post': post})
```

Создать шаблон

appname/templates/appame/post_detail.html

```
{% extends 'blog/base_blog.html' %}

{% block title %}
  {{ blog.title }} - {{ block.super }} # через девис будет отображаться дефолтное содержание из родительского шаблона
{% endblock %}

{% block content %}
  <h1>
    {{ blog.title }}
  </h1>
  <p>
    {{ blog.body }}
  </p>
{% endblock %}
```
Добавить ссылку в индексный шаблон

_blog/templates/blog/index.html_

```
{% extends 'blog/base_blog.html' %}

{% block title %}
  Some Title
{% endblock %}

{% block content %}
  {% post var in post %}
  --/--/--
  --/--/--
  --/--/--
    <a href="{% url "post_detail_url", slug=post.slug %} }}">Read</a>
  {% endfor %}
{% endblock %}
```

Чтобы упростить запись ссылки и не запоминать все параметры урлов, нужно добавить специальный метод

_blog/models.py_
```
--/--/--
from django.shortcuts import reverse

class Classname(models.Model):
    --/--/--
    --/--/--

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug}) # возвращает ссылку на конкретный экземпляр класса

    --/--/--
    --/--/--
```

А в шаблоне заменить ссылку

_blog/templates/blog/index.html_

```
<a href="{% url "blog_detail_url", slug=post.slug %} }}">Read</a>
```
на
```
<a href="{{ classname.get_absolute_url }}">Read</a>
```
