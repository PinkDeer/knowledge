#### Папка с шаблонами

 _blog/templates/blog_

Индексный шаблон: _blog/templates/blog/index.html_
```
{% extends 'blog/base_blog.html' %} # подключение базового шаблона приложения

{% block title %}
  Some Title
{% endblock %}

{% block content %}
  Some Content
{% endblock %}
```

#### Базовый шаблон приложения

_blog/templates/blog/base_blog.html_
```
{% extends '../base.html'%} # подключение базового шаблона проекта
```

#### Базовый шаблон проекта

Необходимо подключение базового шаблона проекта
_blogdjango/settings.py_
```
TEMPLATES = [
    {
        ...
        'DIRS': [
            os.path.join(BASE_DIR, 'templates') # BASE_DIR - абсолютный путь до проекта
        ],
        ...
        },
    },
]
```

_templates/base.html_

```
<!DOCTYPE html>
<html lang="en" dir="ltr">

  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>

      {% block title %}
        Blog Django  # контент по умолчанию. Будет использоваться, если в шаблоне не определено значение
      {% endblock %}

    </title>
  </head>

  <body>

    {% block content %}
      There is no any content for you
    {% endblock %}

  </body>
</html>

```
