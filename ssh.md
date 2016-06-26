[Atom](/atom.md) [Bash](bash.md) [Gems](/gems.md) [Github](/github.md) [jQuery](/jquery.md) [HTML](html.md) [Rails](rails.md) [Ruby](ruby.md) [SQL](sql.md) [SSH](ssh.md) [Tasks](tasks.md)

## SSH


#### ([habr](https://habrahabr.ru/post/122445/)|[wiki](https://ru.wikipedia.org/wiki/SSH))

#### Настройка:

1) Выполнить команду:
```
ssh-keygen
```
2) Пропустить ввода пароля.  
3) Перейти в каталог .ssh, открыть файл id_psa.pub, скорпровать ключ.  
4) Открыть [github](https://github.com/) -> Settings -> SSH and GPG keys -> New SSH key -> Произвольно заполнить поле _Title_. В поле _Кey_ вставить ключ из буфера -> Add SSH key.  
5) При создании нового репозитория, копировать его командой _Clone with SSH_.  
