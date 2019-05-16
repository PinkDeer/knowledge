Создать файл _blog/forms.py и добавить формы

```
from django import forms

class TagForm(forms.Form):
        title = forms.CharField(max_length=50)
        slug = forms.CharField(max_length=50)

```

Немного теории о _cleaned_data_

В shell ипортировать класс формы
```
from blog.forms import TagForm
```
Создать экземляр класса TagForm
```
>> tf = TagForm()
>> tf
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
