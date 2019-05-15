## Linux

### Заметки

#### Установка видеодрайвера Intel
```
sudo add-apt-repository ppa:oibaf/graphics-drivers
sudo apt-get update
sudo apt-get dist-upgrade
```

#### swap

Очистить swap ([подробнее](http://igorka.com.ua/2010-09-14/ochistka-swap-pamyati-v-ubuntu-i-parametr-swappiness/))
```
sudo swapoff -a && sudo swapon -a
```
