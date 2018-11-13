[Atom](/atom.md) || [Bash](bash.md) || [CSS](css.md) || [Gems](/gems.md) || [Git](/git.md) || [HTML](html.md) || [jQuery](/jquery.md) || [Linux](/linux.md) || [Rails](rails.md) || [Ruby](ruby.md) || [SQL](sql.md) || [SSH](ssh.md) || [Tasks](tasks.md)

## Rails


* [Установка rails](#установка-rails)
* [Команды](#команды)
* [Rails console](#rails-console)
* [Тестирование](#тестирование)
  * [TDD](#tdd)
  * [Интеграционное тестирование](#интеграционное-тестирование)
  * [RSpec](#rspec)
* [Полезные команды](#полезные-команды)
* [Развертывание на Heroku](#развертывание-на-heroku)
  * [Подтверждение регистрации development и production на Heroku (Rails 5.2)](#подтверждение-регистрации-development-и-production-на-heroku-(Rails-5.2))
* [Делой на VPS](#делой на-vps)

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
```# README

Lessonm

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
Удалить колонку из таблицы
```
rails d migration remove_columnname_from_tablename columnname:type
```
Запуск теста:
```
bundle exec rake test
```
Очистка кеша:
```
rake tmp:cache:clear
```
Удалить колонку Country из таблицы SampleApps:
```
rails g migration RemoveCountryFromSampleApps country:string
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
```# README

Lessonm
user.errors.full_messages
```
Создание переменной:
```
@var=User.find(2)
@var.name
@var.name="Tom"
@var.save
```
Поиск по атрибуту:
```
User.find_by_name:"Tom"
```
Удалить все записи:
```
User.destroy_all
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

#### Полезные команды

Все доступные задачи Rake
```
bundle exec rake -T
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
Сброс базы данных (после снова запустить миграцию heroku run rake db:migrate):
```
heroku pg:reset DATABASE
```
Открыть в браузере отправленное приложение:
```
$ heroku open
```
Перезагрузить сайт:
```
heroku restart
```
Посмотреть логи:
```
heroku logs
heroku logs -t # в реальном времени
```
Переименовать приложение:
```
heroku rename new_name
```
Список приложений
```
---
```
Выбрать приложение
```
heroku git:remote -a MyHerokuAppName
```

#### Подтверждение регистрации development и production на Heroku (Rails 5.2)

.gitignore
```
config/master.key
```
В модель user.rb добавить модуль :confirmable
```
devise :recoverable, :rememberable, :trackable, :validatable, :confirmable
```
Редактировать config/initializers/devise.rb
```
config.reconfirmable = false
```
Добавить гем letter_opener
```
group :development
  gem 'letter_opener`
end
```
Редактировать config/environments/development.rb
```
config.action_mailer.default_url_options = { host: 'localhost', port: 3000 }
+  config.action_mailer.delivery_method = :letter_opener
+  config.action_mailer.smtp_settings = {
+  address:              'smtp.gmail.com',
+  port:                 587,
+  domain:               'example.com',
+  user_name:            Rails.application.credentials.development[:aws][:user_name],
+  password:             Rails.application.credentials.development[:aws][:password],
+  authentication:       'plain',
+  enable_starttls_auto: true }
```
Редактировать config/environments/production.rb
```
config.action_mailer.default_url_options = { host: 'example.com'}
config.action_mailer.delivery_method = :smtp
config.action_mailer.smtp_settings = {
address:              'smtp.gmail.com',
port:                 587,
domain:               'example.com',
user_name:            Rails.application.credentials.production[:aws][:user_name],
password:             Rails.application.credentials.production[:aws][:password],
authentication:       'plain',
enable_starttls_auto: true }
```
??? Редактировать config/environments/production.rb
```
config.require_master_key = true
```
Открыть config/credentials.yml.enc
```
EDITOR="atom --wait" bin/rails credentials:edit
```
Отредактировать
```
development:
  aws:
    user_name: xxx
    password: yyy
production:
  aws:
    user_name: xxx
    password: yyy
```
В настройках приложения на сайте Хероку в разделе "Reveal Config Vars" добавить переменную RAILS_MASTER_KEY, значение скопировать из config/master.key.


### Делой на VPS


---

Подключение по ssh:
```
ssh root@ipaddress
```
Установка nano, если нет на сервере:
```
sudo apt-get install nano
```
Изменить пароль суперпользователя:
```
sudo passwd root
```
Создание нового пользователя
```
sudo adduser deploy
sudo adduser deploy sudo
su deploy
```
На локальной машине:
```
ssh-copy-id deploy@ipaddress
```
Информацию о текущем языковом окружении:
```
locale
```
Список всех установленных языков и кодировок:
```
locale -a
```
Сгенерироват нужную локаль, например:
```
sudo locale-gen ru_RU.UTF-8
```
Настройки для pg баз данных с поддержкой русского языка:
```
sudo nano /etc/environment
```
```
PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games"
LANGUAGE=en_US.UTF-8
LANG=en_US.UTF-8
LC_ALL=ru_RU.UTF-8
LC_COLLATE=ru_RU.UTF-8
LC_TIME=en_US.UTF-8
```
Часовой пояс сервера:
```
timedatectl
```
Выбор часового пояса:
```
sudo dpkg-reconfigure tzdata
```
#### Установка ruby:
```
curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list

sudo apt-get update
sudo apt-get install git-core curl zlib1g-dev build-essential libssl-dev libreadline-dev libyaml-dev libsqlite3-dev sqlite3 libxml2-dev libxslt1-dev libcurl4-openssl-dev software-properties-common libffi-dev nodejs yarn

cd
git clone https://github.com/rbenv/rbenv.git ~/.rbenv
echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(rbenv init -)"' >> ~/.bashrc
exec $SHELL

git clone https://github.com/rbenv/ruby-build.git ~/.rbenv/plugins/ruby-build
echo 'export PATH="$HOME/.rbenv/plugins/ruby-build/bin:$PATH"' >> ~/.bashrc
exec $SHELL

rbenv install 2.5.1
rbenv global 2.5.1
ruby -v

gem install bundler
```
```
rbenv rehash
```
#### Установка Nginx:
```
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 561F9B9CAC40B2F7
sudo apt-get install -y apt-transport-https ca-certificates

# Add Passenger APT repository
sudo sh -c 'echo deb https://oss-binaries.phusionpassenger.com/apt/passenger xenial main > /etc/apt/sources.list.d/passenger.list'
sudo apt-get update

# Install Passenger & Nginx
sudo apt-get install -y nginx-extras passenger

# Configuration file '/etc/nginx/nginx.conf'
# What would you like to do about it ?  Your options are:
# Y
```
Команды Nginx:
```
sudo service nginx start
sudo service nginx stop
sudo service nginx restart
```
В файл /etc/nginx/nginx.conf:
```
# sudo nano /etc/nginx/nginx.conf

# Раскомментировать
include /etc/nginx/passenger.conf;
# Закомментировать
# include /etc/nginx/conf.d/*.conf;
```
В файле /etc/nginx/passenger.conf изменить строку passenger_ruby... на:
```
# sudo nano /etc/nginx/passenger.conf
passenger_ruby /home/deploy/.rbenv/shims/ruby;
```
#### Установка postgres:
```
# 9.5
sudo apt-get install postgresql postgresql-contrib libpq-dev

# 9.6
sudo add-apt-repository "deb http://apt.postgresql.org/pub/repos/apt/ $(lsb_release -sc)-pgdg main"
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo apt-get update
sudo apt-get install postgresql-9.6
```
В файле /etc/postgresql/9.5/main/pg_hba.conf не должна быть закомментирована строка (любой пользователь по паролю может получить достун к любой базе данных):
```
# IPv4 local connections:
host    all             all             127.0.0.1/32            md5
```
Изменить unix пользователя на пользователя postgres:
```
sudo su - postgres
```
Далее работа идёт от имени пользователя postgres.
##### Консоль доступа к базе данных:
```
psql
```
Список текущих пользователей:
```
\dg
```
Создание нового юзера:
```
create user username with password 'password';
```
Список текущих баз:
```
\l
```
Создать базу данных:
```
create database "db_name_prod" with owner = username;
```
Выход из консоли:
```
\q
```
Проверить доступ к базе:
```
psql -h localhost -U username -W db_name_prod
```
Снова выход из консоли psql ```\q```, затем выход из пользователя postgres ```exit```.

#### Настройка Сapistrano

Добавить гемы:
```
group :development do
  gem 'capistrano',            '3.11'
  gem 'capistrano-rails',      '1.4'
  gem 'capistrano-passenger',  '0.2.0'
  gem 'capistrano-rbenv',      '2.1.3'
  gem '
```
Запустить команду:
```
cap install STAGES=production
```
Редактировать Capfile:
```
require 'capistrano/rails'
require 'capistrano/passenger'
require 'capistrano/rbenv'
require 'capistrano/bundler'
set :rbenv_type, :user
set :rbenv_ruby, '2.5.1'
```
Редактировать config/deploy.rb:
```
lock "3.11.0"

set :application, "app_name"
set :repo_url, "git@github.com:app_name.git"

set :deploy_to, '/home/deploy/apps/app_name'

append :linked_files, "config/database.yml", "config/credentials.yml.enc", "config/master.key"
append :linked_dirs, "log", "tmp/pids", "tmp/cache", "tmp/sockets", "vendor/bundle", "public/system", "public/uploads"
```
Редактировать config/deploy/production.rb
```
server 'app_name.ru', user: 'deploy', roles: %w{app db web}
```
Удаляем конфиг:
```
sudo rm /etc/nginx/sites-available/default
```
Создаем новый конфиг
```
sudo nano /etc/nginx/sites-available/app_name.conf
```
```
server {
        listen 80;
        listen [::]:80 ipv6only=on;

        server_name app_name.ru;
        # access_log /var/log/nginx/app_name/access.log;
        # error_log  /var/log/nginx/app_name/error.log;

        passenger_enabled on;
        rails_env    production;
        root         /home/deploy/apps/app_name/current/public;

        # redirect server error pages to the static page /50x.html
        error_page   500 502 503 504  /50x.html;
        location = /50x.html {
            root   html;
        }
}
```
Создаем ссылку на файл, чтобы при перезагрузке nginx подхватил конфиг:
```
sudo ln -s /etc/nginx/sites-available/app_name.conf /etc/nginx/sites-enabled/app_name.conf
```
Перезагружаем Nginx:
```
sudo service nginx restart
```
Логи nginx:
```
sudo nano /var/log/nginx/access.log   
sudo nano /var/log/nginx/error.log
```
Список всех команд capistrano
```
cap -T
cap -D # c подробным описанием
```
```
nginx -t
```
Запуск деплоя:
```
cap production deploy
```
Скопировать на сервер:
```
scp config/database.yml deploy@ipaddress:/home/deploy/apps/app_name/shared/config/database.yml
scp config/credentials.yml.enc deploy@ipaddress:/home/deploy/apps/app_name/shared/config/credentials.yml.enc
scp config/master.key deploy@ipaddress:/home/deploy/apps/app_name/shared/config/master.key
```
[![up](/image/up.png)](#rails)


[Atom](/atom.md) || [Bash](bash.md) || [CSS](css.md) || [Gems](/gems.md) || [Git](/git.md) || [HTML](html.md) || [jQuery](/jquery.md) || [Linux](/linux.md) || [Rails](rails.md) || [Ruby](ruby.md) || [SQL](sql.md) || [SSH](ssh.md) || [Tasks](tasks.md)
