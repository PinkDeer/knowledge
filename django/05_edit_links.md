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

### Использование метода include

Создать шаблон _blog/templates/blog/includes/post_card_template.html_

Перенести в него
```
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
```
В шаблонах _appname/templates/appame/tags_list.html_ и _appname/templates/appame/index.html_ вместо этого кода использовать
```
{% include 'blog/includes/post_card_template.html' %}
```

### Добавить footer для карточек со списком тэгов

_blog/templates/blog/includes/post_card_template.html_

<div class="card mb-4">
  <div class="card-header">
    {{ post.date_pub }}
  </div>
  <div class="card-body">
    <h5 class="card-title">{{ post.title }}</h5>
    <p class="card-text">{{ post.body|truncatewords:15 }}</p>
    <a href="{{ post.get_absolute_url }}" class="btn btn-light">Read</a>
  </div>
  <div class="card-footer text-muted">
    Tags:
    {% for tag in post.tags.all %}
      <a href="{{ tag.get_absolute_url }}">{{ tag.title }}</a>
    {% endfor %}
  </div>
</div>


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
