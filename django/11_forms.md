#### Создать файл _blog/forms.py_ и добавить формы

```
from django import forms
from .models import Tag


class TagForm(forms.Form):
        title = forms.CharField(max_length=50)
        slug = forms.CharField(max_length=50)

        def save(self):
            new_tag = Tag.objects.create(
                title=self.cleaned_data['title'],
                slug=self.cleaned_data['slug']
            )
            return new_tag
```

#### Немного теории о _cleaned_data_

В shell ипортировать класс формы
```
from blog.forms import TagForm
```
Создать экземляр класса TagForm
```
>>> tf = TagForm()
>>> tf
<TagForm bound=False, valid=Unknown, fields=(title;slug)> # bound - есть ли связанные данные (введенные в форму)
```
Посмотреть список атрибутов
```
dir(tf) # cleaneв_data - отсутсвует
```
Проверка связанных данных, валидности и словаря ошибок
```
>>> tf.is_bound
False
>>> tf.is_valid()
False
>>> tf.errors
{}
```
Заполнить поля пустыми строками
```
>>> d = {'title': '', 'slug': ''}
>>> tf = TagForm(d)
>>> tf
<TagForm bound=True, valid=Unknown, fields=(title;slug)>
```
Ешё раз проверить
```
>>> tf.is_bound
True
>>> tf.is_valid()
False
>>> tf.errors
{'title': ['This field is required.'], 'slug': ['This field is required.']}
```
Проверить список атрибутов
```
>>> dir(tf) # cleaned_data - появился
>>> tf.cleaned_data
{}
```

Словарь _cleaned_data_ появился, потому что была заполнена форма (_tf.is_bound = True_), далее вызвался метод _is_valid_, затем создается  словарь. Если _is_valid_ вернул _True_, то словарь был бы заполнен.

Заполняем поля данными
```
>>> d = {'title': 'some title', 'slug': 'some-title'}
>>> tf = TagForm(d)
>>> tf.is_valid()
True
>>> tf.errors
{}
>>> tf.cleaned_data
{'title': 'some title', 'slug': 'some-title'}
```
Теперь данные из словаря _cleaned_data_ можно использовать для создания экземпляра модели
```
from blog.models import Tag
tag = Tag(title=tf.cleaned_data['title'], slug=tf.cleaned_data['slug'])
tag.save()
```

#### Добавить функцию _clean_slug_
_blog/forms.py_
```
from django import forms
from .models import Tag
from django.core.exceptions import ValidationError

class TagForm(forms.Form):
        title = forms.CharField(max_length=50)
        slug = forms.CharField(max_length=50)

        def clean_slug(self):
            new_slug = self.cleaned_data['slug'].lower() # сохранять slug в нижнем регистри

            if new_slug == 'create':
                raise ValidationError('Slug my not be "create"') # валидация slug`a 'create'
            return new_slug


        def save(self):
            new_tag = Tag.objects.create(
                title=self.cleaned_data['title'],
                slug=self.cleaned_data['slug']
            )
            return new_tag
```


#### Указать шаблон urla\`a

_blog/utils.py_
```
from django.urls import path

from .views import *

urlpatterns = [
    path('', posts_list, name='posts_list_url'),
    path('post/<str:slug>/', PostDetail.as_view(), name='post_detail_url'),
    path('tags/', tags_list, name='tags_list_url'),
    path('tag/create', TagCreate.as_view(), name='tag_create_url'),
    path('tag/<str:slug>/', TagDetail.as_view(), name='tag_detail_url')
]
```

#### Добавить класс

_blog/views.py_

```
--/--/--
--/--/--
from .forms import TagForm

--/--/--
    --/--/--
--/--/--
    --/--/--
--/--/--
    --/--/--


class TagCreate(View):
    def get(self, request):
        form = TagForm()
        return render(request, 'blog/tag_create.html', context={'form': form})

--/--/--
    --/--/--}
```

#### Создать шаблон

_blog/templates/blog/tag_create.html_
```
{% extends 'blog/base_blog.html' %}

{% block title %}
 Tag create  - {{ block.super
{% endblock %}

{% block content %}

   <form action="{% url 'tag_create_url' %}" method="post">

      {% csrf_token %}

      {% for field in form %}
        <div class="form-group">

          {% if field.errors %}
            <div class="alert alert-danger">
              {{ field.errors }}
            </div>
          {% endif %}

          {{ field.label }}
          {{ field }}

        </div>

      {% endfor %}

     <button type="submit" class="btn btn-primary">Create Tag</button>
   </form>

{% endblock %}
```
#### Определить стиль для input\`ов

_blog/forms.py_
```
--/--/--
        --/--/--
        --/--/--

        title.widget.attrs.update({'class': 'form-control'})
        slug.widget.attrs.update({'class': 'form-control'})

        --/--/--
            --/--/--
```

#### Реализовать метод POST

_blog/views.py_
```
--/--/--
from django.shortcuts import redirect
--/--/--

class TagCreate(View):
    def get(self, request):
        form = TagForm()
        return render(request, 'blog/tag_create.html', context={'form': form})

    def post(self, request):
        bound_form = TagForm(request.POST)

        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(new_tag)
        return render(request, 'blog/tag_create.html', context={'form': bound_form})

```
#### Добавить валидацию

_blog/forms.py_
```
def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        --/--/--
            --/--/--
        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('Slug must be unique. We have "{}" slug already'.format(new_slug))
        return new_slug
```
#### Оптимизация

class TagForm(forms.ModelForm):
    # title = forms.CharField(max_length=50)
    # slug = forms.CharField(max_length=50)
    #
    # title.widget.attrs.update({'class': 'form-control'})
    # slug.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Tag
        fields = ['title', 'slug']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'})
        }

    --/--/--
        --/--/--

    # def save(self):
    #     new_tag = Tag.objects.create(
    #         title=self.cleaned_data['title'],
    #         slug=self.cleaned_data['slug']
    #     )
    #     return new_tag  
```
