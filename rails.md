[Atom](/atom.md) || [Bash](bash.md) || [Gems](/gems.md) || [Github](/github.md) || [HTML](html.md) || [jQuery](/jquery.md) || [Linux](/linux.md) || [Rails](rails.md) || [Ruby](ruby.md) || [SQL](sql.md) || [SSH](ssh.md) || [Tasks](tasks.md)

## Rails


* [Установка rails](#установка-rails)
* [Создание](#Создание)
* [Развертывание на Heroku](#Развертывание-на-heroku)

### Установка rails

---

#### Первоначальная настройка системы

```
sudo apt-get update
sudo apt-get install git-core curl zlib1g-dev build-essential libssl-dev libreadline-dev libyaml-dev libsqlite3-dev sqlite3 libxml2-dev libxslt1-dev libcurl4-openssl-dev python-software-properties libffi-dev
```
#### Установка rbenv и ruby
```
cd
git clone git://github.com/sstephenson/rbenv.git .rbenv
```
Может появиться ошибка:
```
fatal: unable to connect to github.com:
github.com[0: 192.30.252.128]: errno=Connection refused
```
Выполнить команду:
```
git config --global url."https://".insteadOf git://
```
Далее
```
echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(rbenv init -)"' >>  ~/.bashrc
exec $SHELL

git clone git://github.com/sstephenson/ruby-build.git ~/.rbenv/plugins/ruby-build
echo 'export PATH="$HOME/.rbenv/plugins/ruby-build/bin:$PATH"' >> ~/.bashrc
exec $SHELL

git clone https://github.com/sstephenson/rbenv-gem-rehash.git ~/.rbenv/plugins/rbenv-gem-rehash

rbenv install 2.3.1
rbenv global 2.3.1
ruby -v
```
#### Установка bundler

```
echo "gem: --no-ri --no-rdoc" > ~/.gemrc
gem install bundler
```
#### Установка rails

```
sudo add-apt-repository ppa:chris-lea/node.js
sudo apt-get update
sudo apt-get install nodejs
```
Если ошибка, то выполнить команды:
```
curl -sL https://deb.nodesource.com/setup | sudo bash -  
sudo apt-get install nodejs  
sudo apt-get install build-essential  
```
Далее
```
gem install rails
or
gem install rails -v 4.2.6

rbenv rehash
rails -v
```

[![up](/image/up.png)](#rails)

### Создание

---

#### Cоздание нового проекта

На примере блога
```
$ rails new blog
```
С опцией --skip-test-unit не генерируется директория test, связанная с дефолтным Test::Unit фреймворком.
```
$ rails new app_name --skip-test-unit
```
Создание модели Post
```
rails generate model Post title:string summary:text body:text
```
Миграция
```
rake db:migrate
```
Создание контроллера Post
```
rails g controller posts
```
Корневой маршрут root в *config/routes.rb* c указанием контроллера *posts* и акшена *index*
```
Rails.application.routes.draw do
  root 'posts#index'
  resources :posts
end

```
#### Проверка маршрута
```
rake routes
```
Вывести все посты
```
class PostsController < ApplicationController
  def index
    @posts = Post.all
  end
end
```
Создать вьюху *index.html.erb* для вывода всех постов (*app/views/posts/*). Вывод только заголовков:
```
<h1>Статьи</h1>
  <% @posts.each do |post| %>
  <h2><%= post.title  %></h2>
  <% end %>
```
#### Запуск

```
rails s -e production
           development (по умолчанию)
           test
```
#### Проверка всех полей модели (в rails консоли):
```
Modelname.attribute_names
```
#### Все записи:
```
Modelname.all
```

---
**Черновик**

добавить контроллер
```
def show
    @posts = Post.find(params[:id])
end
```
добавить въюху show.html.erb
```
<h1><%= @post.title %></h1>
<p><%= @post.body %></p>
```


в app/views/layouts/application.html.erb добить ссылку на создание нового поста
```
<body>
  <%= link_to 'Новая статья', new_post_path %>
  <%= yield %>
</body>
```

Добавить экшен для создания новой статьи
```
def new
  @post = Post.new
end
```

Добавить вьюху new.html.erb
```
<h1>Новая статья</h1>
<%= render 'form' %>
```

И поля в форм
```
<%= form_for @post do |f| %>
  <div class="form-control">
    <%= f.label :title %>
    <%= f.text_field :title%>
  </div>

  <div class="form-control">
    <%= f.label :summary %>
    <%= f.text_area :summary%>
  </div>

  <div class="form-control">
    <%= f.label :body %>
    <%= f.text_area :body%>
  </div>

  <div class="form-control">
    <%= f.submit 'Сохранить' %>
  </div>
<% end %>
```

Добавить экшены для создания поста
```
def create
  @post = Post.new (post_params)
  if @post.save
    redirect_to @post
  else
   render :new
  end
end

private

def post_params
  params.require(:post).permit(:title, :summary, :body)
end
```

Добавить экшен для редактирования
```
def edit
  @post = Post.find(params[:id])
end
```
и вьюху edit.html.erb
```
<h1>Редактировать статью</h1>
<%= render 'form' %>
```

Добавить
```
def update
  @post = Post.find(params[:id])
  if @post.update_attributes(post_params)
    redirect_to @post
  else
   render :edit
  end
end
```

в app/views/layouts/application.html.erb добить ссылку на все статьи
```
<body>
  <%= link_to 'Все статьи', posts_path %>
  <%= link_to 'Новая статья', new_post_path %>
  <%= yield %>
</body>
```


Сделать названия статей линками, редактировать index.html
```
<h1>Статьи</h1>
  <% @posts.each do |post| %>
  <h2><%= link_to post.title, post_path(post) %></h2>
  <% end %>
```
  В show добавить кнопку удаления
```
<h1><%= @post.title %></h1>
<%= link_to 'Изменить', edit_post_path(@post) %>
<%= link_to 'Удалить', post_path(@post), method: :delete, data: {confirm: 'Вы уверены?' } %>
<p><%= @post.body %></p>
```

Добавить экше для удления
```
def destroy
  @post = Post.find(params[:id])
  @post.destroy
  redirect_to @post
end
```
Код контроллера на данный момент
```
class PostsController < ApplicationController
  def index
    @posts = Post.all
  end

  def show
    @post = Post.find(params[:id])
  end

  def new
    @post = Post.new
  end

  def create
    @post = Post.new (post_params)
    if @post.save
      redirect_to @post
    else
     render :new
    end
  end

  def edit
    @post = Post.find(params[:id])
  end

  def update
    @post = Post.find(params[:id])
    if @post.update_attributes(post_params)
      redirect_to @post
    else
     render :edit
    end
  end

  def destroy
    @post = Post.find(params[:id])
    @post.destroy
    redirect_to @post
  end

  private

  def post_params
    params.require(:post).permit(:title, :summary, :body)
  end

end
```
Оптимизируем
```
class PostsController < ApplicationController

  before_action :set_post, only: [ :show, :edit, :update, :destroy]

  def index
    @posts = Post.all
  end

  def show
  end

  def new
    @post = Post.new
  end

  def create
    @post = Post.new (post_params)
    if @post.save
      redirect_to @post
    else
     render :new
    end
  end

  def edit
  end

  def update
    if @post.update_attributes(post_params)
      redirect_to @post
    else
     render :edit
    end
  end

  def destroy
    @post.destroy
    redirect_to @post
  end

  private

  def set_post
    @post = Post.find(params[:id])
  end

  def post_params
    params.require(:post).permit(:title, :summary, :body)
  end

end

```
Оптимизиурем index.html.erb
```
<h1>Статьи</h1>

<%= render @posts %>

```
Переносим в \_post.html.erb
```
<% @posts.each do |post| %>
<h2><%= link_to post.title, post_path(post) %></h2>
<% end %>
```
Но цикл указывать не нужно
```>
<h2><%= link_to post.title, post_path(post) %></h2>

```
Валидация
Пустые поля:
```
class Post < ApplicationRecord
  validates :title, :summary, :content, presence: true
end

```

---

[![up](/image/up.png)](#rails)

#### Rails console

Отрыть консоль
```
rails c
```
Выйти из консоли
```
exit
```

Создание на примере блога:
```
Post.create(title: 'First title', summary: 'First summary', body: 'First body')
```
Посмотреть все посты:
```
Post.all
```

### Развертывание на Heroku

---

Heroku использует базу данных PostgreSQL (произносится “post-gres-cue-ell”, и часто называется “Postgres”), это означает что нам нужно добавить гем pg  в production окружение для того чтобы позволить Рельсам общаться с Postgres (гем rails_12factor, который Heroku использует для работы со статическими ассетами, такими как изображения и таблицы стилей):

```
group :production do
  gem 'pg', '0.15.1'
  gem 'rails_12factor', '0.0.2'
end
```

Опция --without production предотвращает локальную установку любых продакшен-гемов:
```
$ bundle install --without production
```
Регистрация на Heroku: https://signup.heroku.com/identity  

Установка необходимого софта: https://toolbelt.heroku.com/
```
wget -O- https://toolbelt.heroku.com/install-ubuntu.sh | sh
```

Далее необходимо перейти в каталог с приложением и создать новый поддомен:
```
$ cd ~/folder_app
$ heroku create
```
Отправка приложения:
```
$ git push heroku master
```
Запуск миграции продакшен базы данных:
```
heroku run rake db:migrate
```
Если возникает ошибка __▸ ETIMEDOUT: connect ETIMEDOUT 50.19.103.36:5000__ [заблокирован 5000 порт](#http://www.orhancanceylan.com/heroku-run-command-operation-timed-out/) , то необходимо использовать команду:
```
$ heroku run:detached rake db:migrate
```
Открыть в браузере отправленное приложение:
```
$ heroku open
```
Переименовать приложение:
```
heroku rename new_name
```

[![up](/image/up.png)](#rails)
