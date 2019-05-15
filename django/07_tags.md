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

urlpatterns = [tags_list
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

  <div class="card mb-4">
    <div class="card-header">
      {{ post.date_pub }}
    </div>
    <div class="card-body">
      <h5 class="card-title">{{ post.title }}</h5>
      <p class="card-text">{{ post.body|truncatewords:15 }}</p>
      <a href="{{ post.get_absolute_url }}" class="btn btn-light">Read</a>
    </div>
  </div>

{% endblock %}
```
#### Создание ссылки для каждого тэга

_appname/models.py_
```
--/--/--
    --/--/--

class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return '{}'.format(self.title)

```
Редактировать шаблон

_blog/templates/blog/tags_list.html_

```
{% extends 'blog/base_blog.html'%}

{% block title %}
  Tags list - {{ block.super }}
{% endblock %}

{% block content %}
  <h1 class="mb-5">Tags</h1>

    {% for tag in tags %}
      <h3><a href="{{ tag.get_absolute_url }}">{{ tag.title }}</h3> # добавить ссылку
    {% endfor %}

{% endblock %}

```
