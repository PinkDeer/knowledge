[Atom](/atom.md) || [Bash](bash.md) || [CSS](css.md) || [Gems](/gems.md) || [Git](/git.md) || [HTML](html.md) || [jQuery](/jquery.md) || [Linux](/linux.md) || [Rails](rails.md) || [Ruby](ruby.md) || [SQL](sql.md) || [SSH](ssh.md) || [Tasks](tasks.md)

## Atom


* [Найcтройка](#настройка)
* [Пакеты](#пакеты)

#### [Официальный сайт](https://atom.io/)

#### Настройка:

---

* Edit -> Preferences -> uncheck "Open Empty Editor On Start"
* Project Home: /home/...
* Packages -> Core Packages -> autosave -> Setting -> check "Enabled"

Обновление:
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

[![up](/image/up.png)](#atom)

#### Пакеты:

---

* [atom beautify](https://atom.io/packages/atom-beautify)
* [file Icons](https://atom.io/packages/file-icons)
* [language Slim](https://atom.io/packages/language-slim)
* [minimap](https://atom.io/packages/minimap)
* [pigments](https://atom.io/packages/pigments)
* [minimap-pigments](https://atom.io/packages/minimap-pigments)
* ~~[Terminal Plus](https://atom.io/packages/terminal-plus)~~
* [PlatformIO IDE Terminal](https://atom.io/packages/platformio-ide-terminal)
* [indent-guide-improved](https://atom.io/packages/indent-guide-improved)
* [Open Recent](https://atom.io/packages/open-recent)
* [Highlight Selected](https://atom.io/packages/highlight-selected)
* [autoclose-html](https://atom.io/packages/autoclose-html)
* [autocomplete-paths](https://atom.io/packages/autocomplete-paths)
* [color-picker](https://atom.io/packages/color-picker)
* [copy-path](https://atom.io/packages/copy-path)
* [pdf-view](https://atom.io/packages/pdf-view)
* [minimap-highlight-selected](https://atom.io/packages/minimap-highlight-selected)
* [emmet](https://atom.io/packages/emmet)
* [lorem](https://atom.io/packages/lorem)
* [markdown-preview-plus](https://atom.io/packages/markdown-preview-plus)
* [linter](https://atom.io/packages/linter)
  * [erb](https://atom.iohttps://atom.io/packages/markdown-preview-plus/packages/linter-erb)
  * [css](https://atom.io/packages/linter-csslint)
  * [haml](https://atom.io/packages/linter-haml)
  * [sass](https://atom.io/packages/linter-sass-lint)
  * [scss](https://atom.io/packages/linter-scss-lint)
  * [slim](https://atom.io/packages/linter-slim)

[![up](/image/up.png)](#atom)