## Bash


* [cd](#cd)
* [ls](#ls)
* [mkdir](#mkdir)
* [touch](#touch)
* [echo](#echo)
* [cat и cp](#cat-и-cp)
* [mv)](#mv)
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

### cat и cp

---

([en](http://linux.die.net/man/1/cat)|[rus](http://rus-linux.net/lib.php?name=/MyLDP/consol/HuMan/cat-ru.html))

Для вывода содержимого файла на терминал используется команда cat:
```
\$ cat copyme
firstfile
```
([en](http://linux.die.net/man/1/cp)|[rus](https://ru.wikipedia.org/wiki/Cp))

Теперь мы можем приступить к разбору базовой функциональности команды cp. Эта команда принимает два аргумента. Первый — имя уже существующего файла ('copyme'), второй — название новой копии, которую мы хотим сделать ('copiedme').
```
\$ cp copyme copiedme
```
Можем убедиться, что новая копия файла имеет другой номер инода (это значит что мы получили действительно новый отдельный файл, а не просто ссылку на старый)
```
\$ ls -i copyme copiedme
  648284 copiedme   650704 copyme
```

[![up](/image/up.png)](#bash)

### mv

---

([en](http://linux.die.net/man/1/mv)|[rus](https://ru.wikipedia.org/wiki/Mv))


Теперь применим команду mv чтобы переименовать файл ("copiedme" –> "movedme"). Номер инода после этой операции не меняется, а изменяется только название файла.
```
\$ mv copiedme movedme
\$ ls -i movedme
  648284 movedme
```
Номер инода не изменяется только при условии, что переименованный файл остается в пределах той файловой системы где находился исходный файл. Мы рассмотрим подробнее устройство файловых систем в одной из следующих частей этого пособия.
Команда mv позволяет не только переименовывать файлы, но и перемещать их. Например, чтобы переместить файл /var/tmp/myfile.txt в директорию /home/user нужно дать команду:
```
\$ mv /var/tmp/myfile.txt /home/user
```
Файл будет перемещен в домашнюю директорию пользователя user даже если она находится в другой файловой системе (в этом случае файл будет скопирован в новое место после чего оригинал будет удален). Как вы могли уже догадаться, перемещение файла в другую файловую систему приводит к изменению его инода. Это происходит потому, что каждая файловая система имеет свой отдельный набор инодов.

> Нужно заметить, существует вероятность, что новый присвоенный номер инода может совпасть со старым, но она чрезвычайно мала.

Чтобы переместить одновременно несколько файлов в одну директорию нужно написать:
```
\$ mv /var/tmp/myfile1.txt /var/tmp/myfile2.txt /home/user
```
или
```
\$ mv -t /home/user /var/tmp/myfile1.txt /var/tmp/myfile2.txt
```
Если добавить опцию '-v', на экран будет выведен отчет о проделанной операции:
```
\$ mv -vt /home/user /var/tmp/myfile1.txt /var/tmp/myfile2.txt
   '/var/tmp/myfile1.txt' -> '/home/user/myfile1.txt'
   '/var/tmp/myfile2.txt' -> '/home/user/myfile2.txt'
```

[![up](/image/up.png)](#bash)


### kill

---

([en](http://linux.die.net/man/1/killall)|[rus](http://rus-linux.net/MyLDP/BOOKS/MDK-10/process-signals.html)|[rus2](http://rus-linux.net/MyLDP/consol/kill.html)|[habr](https://habrahabr.ru/post/95102/))

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
