[Atom](/atom.md) [Bash](bash.md) [Gems](/gems.md) [Github](/github.md) [jQuery](/jquery.md) [HTML](html.md) [Rails](rails.md) [Ruby](ruby.md) [SQL](sql.md) [SSH](ssh.md) [Tasks](tasks.md)

## Rails


* [Установка rails](#установка-rails)
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

gem install rails
or
gem install rails -v 4.2.6

rbenv rehash
rails -v
```

[![up](/image/up.png)](#rails)

### Развертывание на Heroku

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
Открыть в браузере отправленное приложение:
```
$ heroku open
```
Переименовать приложение:
```
heroku rename new_name
```

[![up](/image/up.png)](#rails)
