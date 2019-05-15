#### Перенапраление запроса к приложению

_blogdjango/urls.py_
```
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')), # обращения по url 'blog/' обрабатываются 'blog/urls.py'
]
```
#### Подключение приложения

_blogdjango/settings.py_
```
INSTALLED_APPS = [
    ...
    'blog',
]
```
_blog/urls.py_
```
from django.urls import path

from .views import posts_list # или 'from .views import *' для ипортирования всех функций из views.py

urlpatterns = [
    path('', posts_list), # posts_list - функция обрабатывающая запрос
]
```
_blog/views.py_
```
from django.shortcuts import render

def posts_list(request):
  return render(request, 'blog/index.html) # подключение шаблона
```
