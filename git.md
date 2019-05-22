### Команды

#### Первоначальная настройка системы

```
git config --global user.name "YourName"
git config --global user.email your.email@example.com
```

#### Первоначальная настройка репозитория

```
git init
git status
git add .
git commit -am "Your comment"

git remote add orogin https://github.com/<username>/<appname>.git
# or
git remote add origin git@github.com:<username>/<appname>.git

git push -u origin master
```
Метка __-m__ позволяет добавлять сообщение для фиксации; если пропустить -m, то Git откроет редактор и предложит ввести сообщение в нем.  
Флаг __-a__ как сокращение для (очень частого) случая фиксации всех изменений к существующим файлам (или файлов, созданных с использованием git mv, которые не считаются новыми для Git):

#### Загрузить и мержить ветку master удаленного репозитория
```
git fetch --all
git reset --hard origin/master
git pull origin master
```
#### Отменить изменения

Чтобы вернутcя к предыдущей фиксации, если измения еще не зафиксировались, необходимо выполнить следующую команду (с -f флагом, чтобы инициировать перезапись текущих изменений):
```
git checkout -f
```
#### Ветвление

Создание новой рабочей ветки:
```
$ git checkout -b new_branch
```
Перечисление всех локальных веток. Звездочка * указывает, какая ветка в настоящий момент включена
```
$ git branch
master
* new_branch
```
Вернуться к master ветке:
```
$ git checkout master
```
Объединение new_branch c master:
```
$ git merge new_branch
```
Удаление ветки new_branch:
```
$ git branch -d new_branch
```
Можете отказаться от изменений, относящихся к рабочей ветке, в таком случае использовать git branch -D. В отличие от флага -d, флаг -D сотрет ветку даже если мы не объединили изменения.


Удаление файла из репозиатория:
```
git rm file_path --cached
```
Удалить файл из истории git:
```
git filter-branch --tree-filter 'rm -f file_path' HEAD
git push origin --force --all
```

####  Переименовение
```
$ git mv README.rdoc README.md
```

### Markdown

---

* [О markdown](https://help.github.com/articles/about-writing-and-formatting-on-github/)
* [Базовый синтаксис](https://help.github.com/articles/basic-writing-and-formatting-syntax/)|[Примеры](https://learn.getgrav.org/content/markdown)
* [Редактор](https://jbt.github.io/markdown-editor/)|[Редактор2](https://stackedit.io/editor#)

### Gitbook

* [Официальный сайт](https://www.gitbook.com/)
* [Документация](https://docs.gitbook.com/)


### Настройка SSH для Github:

1) Выполнить команду `ssh-keygen`.

2) Пропустить ввода пароля.  

3) Перейти в каталог .ssh с помощью команды `cd ~/.ssh`, открыть файл id_psa.pub, скопировать ключ.
Или вывести ключ в консоль командой `cat ~/.ssh/id_rsa.pub` и скопировать его.

4) Открыть [github](https://github.com/) -> Settings -> SSH and GPG keys -> New SSH key -> Произвольно заполнить поле _Title_. В поле _Кey_ вставить ключ из буфера -> Add SSH key.  

5) При создании нового репозитория, копировать его командой _Clone with SSH_.

[habr](https://habrahabr.ru/post/122445/)/[wiki](https://ru.wikipedia.org/wiki/SSH)
