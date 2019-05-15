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