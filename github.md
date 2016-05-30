[Atom](/atom.md) [Bash](bash.md) [Gems](/gems.md) [Github](/github.md) [Rails](rails.md) [Ruby](ruby.md) [Tasks](tasks.md)

## Github


* [Команды](#команды)
* [Markdown](#markdown)

### Команды

---

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
git push -u origin master
```

#### Загрузить и мержить ветку master удаленного репозитория
```
git fetch --all
git reset --hard origin/master
git pull origin master
```

[![up](/image/up.png)](#github)


### Markdown

---

* [О markdown](https://help.github.com/articles/about-writing-and-formatting-on-github/)
* [Базовый синтаксис](https://help.github.com/articles/basic-writing-and-formatting-syntax/)|[Примеры](https://learn.getgrav.org/content/markdown)
* [Редактор](https://jbt.github.io/markdown-editor/)|[Редактор2](https://stackedit.io/editor#)

[![up](/image/up.png)](#github)
