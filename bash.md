## Bash


* [cd](#cd)
* [ls](#ls)
* [mkdir](#mkdir)
* [kill](#kill)


### cd

---

#### Go to the root directory
```
\$ cd /
```
#### Go to your home directory
```
$ cd
```
#### Print working directory
```
$ pwd
```
#### Absolute path
An absolute path is defined as the specifying the location of a file or directory from the root directory(/).
```
/dev
/usr
/usr/bin
/usr/local/bin
```
#### Relative path
Relative path is defined as path related to the present working directory(pwd).
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
[Examples](http://www.linuxnix.com/abslute-path-vs-relative-path-in-linuxunix/)

#### Working directory "."
A special directory "." points to the current directory
```
\$ ./script.sh
```
[To contents](#bash)


### ls

---

([en](https://en.wikipedia.org/wiki/Ls)|[rus](http://rus-linux.net/MyLDP/consol/hdrguide/rusman/ls.htm))

Invoked without any arguments, ls lists the files in the current working directory.
```l
\$ ls
```
Without options, ls displays files in a bare format. This bare format however makes it difficult to establish the type, permissions, and size of the files. The most common options to reveal this information or change the list of files are:

*  -l long format, displaying Unix file types, permissions, number of hard links, owner, group, size, last-modified date and filename
*  -f do not sort. Useful for directories containing large numbers of files.
*  -F appends a character revealing the nature of a file, for example, * for an executable, or / for a directory. Regular files have no suffix.
*  -a lists all files in the given directory, including those whose names start with "." (which are hidden files in Unix). By default, these files are excluded from the list.
*  -R recursively lists subdirectories. The command ls -R / would therefore list all files.
*  -d shows information about a symbolic link or directory, rather than about the link's target or listing the contents of a directory.
*  -t sort the list of files by modification time.
*  -h print sizes in human readable format. (e.g., 1K, 234M, 2G, etc.) This option is not part of the POSIX standard, although implemented in several systems, e.g., GNU coreutils in 1997, FreeBSD 4.5 in 2002, and Solaris 9 in 2002.
* -i option lists the inode ([en](https://en.wikipedia.org/wiki/Inode)|[rus](https://ru.wikipedia.org/wiki/Inode)) number before the filename.

[To contents](#bash)


### mkdir

---

([en](https://en.wikipedia.org/wiki/Mkdir)|[rus](https://ru.wikipedia.org/wiki/Mkdir))

```
$ mkdir folder
```
or
```
$ mkdir -p folder/folder2/folder3
```
[To contents](#bash)


### kill

---

([en](http://linux.die.net/man/1/killall)|[rus](http://rus-linux.net/MyLDP/BOOKS/MDK-10/process-signals.html)|[habr](https://habrahabr.ru/post/95102/))

killall - kill processes by name
```
killall firefox
```
or
```
admin@pingvinus:~$ ps -Aef | grep firefox
admin     2275     1 11 07:42 ?        00:05:52 /usr/lib/firefox-3.5.8/firefox
admin     2821  2800  0 08:32 pts/2    00:00:00 grep firefox
admin@pingvinus:~$ kill 2275
```
[To contents](#bash)
