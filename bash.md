## Bash


* [cd](#cd)
* [ls](#ls)
* [mkdir](#mkdir)
* [touch](#touch)
* [echo](#echo)
* [kill](#kill)

> Большинство команд Linux могут быть запущены с параметром  "--help" 
>
> Более расширенная информация доступна из командной строки с использованием так называемых страниц руководства ("manual pages" или манов) - "man <command>"
>
> Список встроенных командах bash может быть получен вводом команды  help. А помощь по любой встроенной команде можно получить, набрав, например, так: help cd
>
> [Подробней](https://www.sao.ru/hq/sts/linux/doc/lnag/2.html)


### cd

---

#### Перейти в корневую директорию
```
\$ cd /
```
#### Перейти к домашнюю директорию

```
$ cd
```
Без аргумента cd переместит вас в домашнюю директорию. Для суперпользователя домашней обычно является директория /root, а для обычных пользователей — /home/username/. 

~ — специальное имя, указывающее в bash на домашнюю директорию пользователя.

#### Текущаю рабочая директория
```
$ pwd
```
#### Абсолютный путь

Абсолютный путь всегда начинается с /.

```
/dev
/usr
/usr/bin
/usr/local/bin
```
#### Отноcительный путь

Путь отноcительно текущей директории (pwd).
```
\$ cd local/bin
\$ pwd
/usr/local/binn
```
```
/home/user/file.txt
or
~/file.txt
```
[Пример](http://www.linuxnix.com/abslute-path-vs-relative-path-in-linuxunix/)

#### Использование ".."

Относительные пути могут содержать одну или несколько директорий "..". ".." указывает на родительскую директорию по отношению к нашей рабочей директории

```
\$ pwd
/usr/local/bin
\$ cd ..
\$ pwd
/usr/local
```
Можно добавить .. к относительному пути. Это позволит переместиться в директорию, которая находится на одном уровне с той в которой мы находимся

```
\$ pwd
/usr/local
\$ cd ../share
\$ pwd
/usr/share
```
[![up](/image/up.png)](#bash)

#### Рабочая директория "."

Специальная директория "." указывающаю на текущую директорию.
```
\$ ./script.sh
```
[![up](/image/up.png)](#bash)

####  Домашние директории других пользователей

Но что если нам нужно указать файл в домашней директории другого пользователя? Для этого после тильды нужно указать имя этого пользователя. Например, чтобы указать на файл fredsfile.txt находящийся в домашней директории пользователя fred:

```
\$ ./myprog ~fred/fredsfile.txt
```


### ls

---

([en](https://en.wikipedia.org/wiki/Ls)|[rus](http://rus-linux.net/MyLDP/consol/hdrguide/rusman/ls.htm))


ls без аргументов, выводит на экран список файлов хранящихся в рабочей директории:

```l
\$ ls
```

[![up](/image/up.png)](#bash)



### mkdir

---

([en](https://en.wikipedia.org/wiki/Mkdir)|[rus](https://ru.wikipedia.org/wiki/Mkdir))

```
$ mkdir folder
```
Создание вложенной структуры директорий
```
$ mkdir -p folder/folder2/folder3
```
[![up](/image/up.png)](#bash)



### touch

---

([en](https://en.wikipedia.org/wiki/Touch_%28Unix%29)|[rus](http://itcollider.ru/forum/linuxoid/1181-komanda-touch-v-linux.html))

Команда touch обновляет время последнего доступа к файлу если он уже существует или создает новый пустой файл, если его ещё нету.

```
\$ touch filename
```


[![up](/image/up.png)](#bash)



### echo

---

([en](http://linux.die.net/man/1/echo)|[rus](https://ru.wikipedia.org/wiki/Echo)|[habr](https://habrahabr.ru/post/119436/))

echo - команда, предназначенная для отображения строки текста
```
\$ echo "firstfile"
```
Может служить для записи строки в файл, если используется > файл будет перезаписан, если >> строка будет дописана в конец файла.
```
\$ echo "firstfile" > filename
```

[![up](/image/up.png)](#bash)


### kill

---

([en](http://linux.die.net/man/1/killall)|[rus](http://rus-linux.net/MyLDP/BOOKS/MDK-10/process-signals.html)|[habr](https://habrahabr.ru/post/95102/))

killall - принудительное завершение программы
```
killall firefox
```
или
```
admin@pingvinus:~$ ps -Aef | grep firefox
admin     2275     1 11 07:42 ?        00:05:52 /usr/lib/firefox-3.5.8/firefox
admin     2821  2800  0 08:32 pts/2    00:00:00 grep firefox
admin@pingvinus:~$ kill 2275
```
[![up](/image/up.png)](#bash)
