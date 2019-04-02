[Atom](/atom.md) || [Bash](bash.md) || [CSS](css.md) || [Gems](/gems.md) || [Git](/git.md) || [HTML](html.md) || [jQuery](/jquery.md) || [Linux](/linux.md) || [Rails](rails.md) || [Ruby](ruby.md) || [SQL](sql.md) || [SSH](ssh.md) || [Tasks](tasks.md)

## SSH


#### ([habr](https://habrahabr.ru/post/122445/)|[wiki](https://ru.wikipedia.org/wiki/SSH))

#### Настройка:

1) Выполнить команду `ssh-keygen`.
2) Пропустить ввода пароля.  
3) Перейти в каталог .ssh с помощью команды `cd ~/.ssh`, открыть файл id_psa.pub, скопировать ключ.
Или вывести ключ в консоль командой `cat ~/.ssh/id_rsa.pub` и скопировать его.   
4) Открыть [github](https://github.com/) -> Settings -> SSH and GPG keys -> New SSH key -> Произвольно заполнить поле _Title_. В поле _Кey_ вставить ключ из буфера -> Add SSH key.  
5) При создании нового репозитория, копировать его командой _Clone with SSH_.