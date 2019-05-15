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
