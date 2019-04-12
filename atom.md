## Atom


### Настройка:

* Edit -> Preferences -> uncheck "Open Empty Editor On Start"
* Project Home: /home/...
* Packages -> Core Packages -> autosave -> Setting -> check "Enabled"

### Обновление
```
#!/bin/bash
wget -q https://github.com/atom/atom/releases/latest -O /tmp/latest
wget --progress=bar -q $(awk -F '[<>]' '/href=".*atom-amd64.deb/ {match($0,"href=\"(.*.deb)\"",a); print "https://github.com/" a[1]} ' /tmp/latest) -O /tmp/atom-amd64.deb --show-progress
dpkg -i /tmp/atom-amd64.deb
```
Или:
```
sudo add-apt-repository ppa:webupd8team/atom
sudo apt-get update
sudo apt-get install atom
```

### Полезные команды

_ctrl + /_ - комментарий
_ctrl + shift + d_ - копия строки
_shift + tab_ - смещение на один tab влево
