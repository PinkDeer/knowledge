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
