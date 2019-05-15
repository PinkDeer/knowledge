Папка с шаблонами: _appname/templates/appame_

Шаблон: _appname/templates/appame/index.html_
```
{% extends 'appname/base_appname.html' %} # подключение базового шаблона приложения

{% block title %}
  Some Title
{% endblock %}

{% block content %}
  Some Content
{% endblock %}
```
Базовый шаблон приложения _appname/templates/appname/base_appname.html_
```
{% extends '../base.html'%} # подключение базового шаблона проекта
```
Необходимо подключение базового шаблона проекта
_projectname/settings.py_
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

Базовый шаблон проекта _templates/base.html_
```
<!DOCTYPE html>
<html lang="en" dir="ltr">

  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>

      {% block title %}
        Project Name  # контент по умолчанию. Будет использоваться, если в шаблоне не определено значение
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
