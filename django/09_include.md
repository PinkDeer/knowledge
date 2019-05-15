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
