### Bash

#### Basics

###### Go to the root directory
```
\$ cd /
```
###### Go to your home directory
```
$ cd
```
###### Print working directory
```
$ pwd
```
######  Absolute path
An absolute path is defined as the specifying the location of a file or directory from the root directory(/).
```
/dev
/usr
/usr/bin
/usr/local/bin
```
###### Relative path
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

###### Working directory "."
A special directory "." points to the current directory
```
\$ ./script.sh
```

#### Linux Commands
###### ls
Invoked without any arguments, ls lists the files in the current working directory.
```
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
* -i option lists the inode number before the filename.
