[Atom](/atom.md) || [Bash](bash.md) || [CSS](css.md) || [Gems](/gems.md) || [Github](/github.md) || [HTML](html.md) || [jQuery](/jquery.md) || [Linux](/linux.md) || [Rails](rails.md) || [Ruby](ruby.md) || [SQL](sql.md) || [SSH](ssh.md) || [Tasks](tasks.md)

## Rails


* [Установка rails](#установка-rails)
* [Команды](#Команды)
* [Тестирование](#Тестирование)
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

### Команды

---

Создание нового приложении используz опреленную версию rails:
```
rails _4.2.0_ new sample_app
```
Установка гемов пропустив геиы для эксплуатационного окружения:
```
bundle install --without production
```
Создание от отмена контоллера:
```
rails generate controller StaticPages home help
rails destroy controller StaticPages home help
```
Создание и отмена модели:
```
rails generate model User name:string email:string
rails destroy model User
```

Миграции изменяют состояние базы данных с помощью команды:
```
bundle exec rake db:migrate
```
Мы можем откатить один шаг миграции:
```
bundle exec rake db:rollback
```
Чтобы откатить к самому началу (все миграции):
```
bundle exec rake db:migrate VERSION=0
```
Запуск теста:
```
bundle exec rake test
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

### Тестирование

---

#### TDD


Запуск тестиования
```
bundle exec rake test
```
Чтобы заставить Rails по умолчанию показывать красный и зеленый необходимо доватить в файо test/test_helper.rb следующие строки:
```
require "minitest/reporters"
Minitest::Reporters.use!
```
Автоматизация тестирования с  помощью Guard:


Гем:
```
group :test do
  ...
  gem 'guard-minitest',     '2.3.1'
end
```
Инициализация:
```
bundle exec guard init
```
Отредкактирвать фаил Guardfile:
```
# Определяет правила сопоставления для Guard
guard :minitest, spring: true, all_on_start: false do
  watch(%r{^test/(.*)/?(.*)_test\.rb$})
  watch('test/test_helper.rb') { 'test' }
  watch('config/routes.rb')     { integration_tests }
  watch(%r{^app/models/(.*?)\.rb$}) do |matches|
    "test/models/#{matches[1]}_test.rb"
  end
  watch(%r{^app/controllers/(.*?)_controller\.rb$}) do |matches|
    resource_tests(matches[1])
  end
  watch(%r{^app/views/([^/]*?)/.*\.html\.erb$}) do |matches|
    ["test/controllers/#{matches[1]}_controller_test.rb"] +
    integration_tests(matches[1])
  end
  watch(%r{^app/helpers/(.*?)_helper\.rb$}) do |matches|
    integration_tests(matches[1])
  end
  watch('app/views/layouts/application.html.erb') do
    'test/integration/site_layout_test.rb'
  end
  watch('app/helpers/sessions_helper.rb') do
    integration_tests << 'test/helpers/sessions_helper_test.rb'
  end
  watch('app/controllers/sessions_controller.rb') do
    ['test/controllers/sessions_controller_test.rb',
     'test/integration/users_login_test.rb']
  end
  watch('app/controllers/account_activations_controller.rb') do
    'test/integration/users_signup_test.rb'
  end
  watch(%r{app/views/users/*}) do
    resource_tests('users') +
    ['test/integration/microposts_interface_test.rb']
  end
end
# Возвращает интеграционные тесты, соответствующие данному ресурсу.
def integration_tests(resource = :all)
  if resource == :all
    Dir["test/integration/*"]
  else
    Dir["test/integration/#{resource}_*.rb"]
  end
end
# Возвращает тесты контроллера, соответствующие данному ресурсу.
def controller_test(resource)
"test/controllers/#{resource}_controller_test.rb"
end
# Возвращает все тесты, соответствующие данному ресурсу.
def resource_tests(resource)
integration_tests(resource) << controller_test(resource)
end

```
Добавить в .gitignore:
```
spring/
```

#### Интеграционное тестирование

Интеграционное тестирование позволят проверить поведение приложения в комплексе.
Пример:
```
rails generate integration_test site_layout
```
test/integration/site_layout_test.rb
```
require 'test_helper'
class SiteLayoutTest < ActionDispatch::IntegrationTest
  test "layout links" do
    get root_path
    assert_template 'static_pages/home'
    assert_select "a[href=?]", root_path, count: 2
    assert_select "a[href=?]", help_path
    assert_select "a[href=?]", about_path
    assert_select "a[href=?]", contact_path
  end
```
Проверка:
```
bundle exec rake test:integration
```

#### RSpec


##### Полезные ссылки

* [Better Specs](#http://betterspecs.org/ru])



---

[![up](/image/up.png)](#rails)

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
