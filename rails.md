[Atom](/atom.md) || [Bash](bash.md) || [CSS](css.md) || [Gems](/gems.md) || [Github](/github.md) || [HTML](html.md) || [jQuery](/jquery.md) || [Linux](/linux.md) || [Rails](rails.md) || [Ruby](ruby.md) || [SQL](sql.md) || [SSH](ssh.md) || [Tasks](tasks.md)

## Rails


* [Установка rails](#установка-rails)
* [Команды](#команды)
* [Rails console](#rails-console)
* [Тестирование](#тестирование)
  * [TDD](#tdd)
  * [Интеграционное тестирование](#интеграционное-тестирование)
  * [RSpec](#rspec)
* [Развертывание на Heroku](#развертывание-на-heroku)

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

#### Обновление списка доступных версии Ruby
```
cd ~/.rbenv/plugins/ruby-build
git pull
```

[![up](/image/up.png)](#rails)


### Команды


---


Создание нового приложении используя опреленную версию rails:
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
Очистить базу данных:
```
bundle exec rake db:migrate:reset
```
Запуск теста:
```
bundle exec rake test
```


[![up](/image/up.png)](#команды) _Команды_  


### Rails console


---


Отрыть консоль
```
rails c
```
Запуск консоли в изолированном режиме
```
rails c --sandbox
```
Выйти из консоли
```
exit
```

Создание объекта:
```
User.new
# или сразу
user = User.new(name: "Michael Hartl", email: "mhartl@example.com")
user.valid? # проверка допустимости
user.save
user # проверка созданного объекта
```
Создание в один шаг:
```
User.create(name: "A Nother", email: "another@example.org")

foo = User.create(name: "Foo", email: "foo@bar.com") # присврение переменной
foo.destroy
```
Доступ к атрибутам:
```
user.name
=> "Michael Hartl"
user.email
=> "mhartl@example.com"
user.updated_at
=> Thu, 24 Jul 2014 00:57:46 UTC +00:00
```
Посик объектов:
```
User.find(1)
User.find_by(email: "mhartl@example.com")
User.first
User.all
User.count
```
Обновление объектов:
```
user # Просто чтобы вспомнить имеющиеся атрибуты
>> user.email = "mhartl@example.net"
"mhartl@example.net"
>> user.save
```
Второй способ обновления:
```
user = User.first
user.update_attributes(name: "The Dude", email: "dude@abides.org")
user.update_attribute(:name, "The Dude") # update_attribute - для обновления одного атрубута.
```
Проверка объекта _errors_ созданного проверкой:
```
user.errors.full_messages
```

#### Окружение
```
$ rails console
Loading development environment
>> Rails.env
=> "development"
>> Rails.env.development?
=> true
>> Rails.env.test?
=> false
```
Запуск в тестовом окружении:
```
$ rails console test Loading test environment
>> Rails.env
=> "test"
>> Rails.env.test?
=> true
```
Чтобы запустить rails в промышленном окружении необходимо настроить базы данных:
```
bundle exec rake db:migrate RAILS_ENV=production
rails server --environment production
```
Проверка окружения на heroku
```
$ heroku run console
>> Rails.env
=> "production"
```

[![up](/image/up.png)](#rails)


### Тестирование


---


#### TDD

Запуск тестирования
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
[![up](/image/up.png)](#rails)

#### Тестирование модели


##### email


Проверка допустимости, наличия, длины и формата (test/models/user_test.rb):
```
require 'test_helper'
class UserTest < ActiveSupport::TestCase
  def setup
    @user = User.new(name: "Example User", email: "user@example.com")
  end
  test "should be valid" do # допустимость
    assert @user.valid?
  end
  test "name should be present" do # наличие
    @user.name = " "
    assert_not @user.valid?
  end
  test "email should be present" do # наличие
    @user.email = " "
    assert_not @user.valid?
  end
  test "name should not be too long" do # проверка длины
    @user.name = "a" * 51
    assert_not @user.valid?
  end
  test "email should not be too long" do # проверка длины
    @user.email = "a" * 244 + "@example.com"
    assert_not @user.valid?
  end
  test "email validation should reject invalid addresses" do # формат email
   invalid_addresses = %w[user@example,com user_at_foo.org user.name@example.
                          foo@bar_baz.com foo@bar+baz.com]
   invalid_addresses.each do |invalid_address|
     @user.email = invalid_address
     assert_not @user.valid?, "#{invalid_address.inspect} should be invalid"
   end
   test "email addresses should be unique" do # проверка на уникальность
    duplicate_user = @user.dup
    duplicate_user.email = @user.email.upcase
    @user.save
    assert_not duplicate_user.valid?
  end
 end

end
```
Добавить валидацию (user.rb), зеленый тест:
```
class User < ActiveRecord::Base
  before_save { self.email = email.downcase }
  validates :name, presence: true, length: { maximum: 50 }
  VALID_EMAIL_REGEX = /\A[\w+\-.]+@[a-z\d\-.]+\.[a-z]+\z/i
  validates :email, presence: true, length: { maximum: 255 },
                    format: { with: VALID_EMAIL_REGEX },
                    uniqueness: { case_sensitive: false }
end
```
Создание индекса в базе данных для столбца email:
```
rails generate migration add_index_to_users_email
```
Заполнить db/migrate/[timestamp] add_index_to_users_email.rb:
```
class AddIndexToUsersEmail < ActiveRecord::Migration
  def change
    add_index :users, :email, unique: true
  end
end
```
Очичтить test/fixtures/users.yml:
```
# пустой
```


##### пароль
Миграциф:
```
rails generate migration add_password_digest_to_users password_digest:string
```
Добавить гем:
```
gem 'bcrypt',               '3.1.7'
```
Добваить в user.rb:
```
class User < ActiveRecord::Base
  before_save { self.email = email.downcase }
  validates :name, presence: true, length: { maximum: 50 }
  VALID_EMAIL_REGEX = /\A[\w+\-.]+@[a-z\d\-.]+\.[a-z]+\z/i
  validates :email, presence: true, length: { maximum: 255 },
                    format: { with: VALID_EMAIL_REGEX },
                    uniqueness: { case_sensitive: false }
  has_secure_password # новое
  validates :password, length: { minimum: 6 } # новое
end
```
И изменить setup в test/models/user_test.rb:
```
def setup
  @user = User.new(name: "Example User", email: "user@example.com",
                     password: "foobar", password_confirmation: "foobar")
end
```
И добавить:
```
test "password should have a minimum length" do
    @user.password = @user.password_confirmation = "a" * 5
    assert_not @user.valid?
  end
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


[Atom](/atom.md) || [Bash](bash.md) || [CSS](css.md) || [Gems](/gems.md) || [Github](/github.md) || [HTML](html.md) || [jQuery](/jquery.md) || [Linux](/linux.md) || [Rails](rails.md) || [Ruby](ruby.md) || [SQL](sql.md) || [SSH](ssh.md) || [Tasks](tasks.md)
