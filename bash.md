### Полезные команды

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

#### Chrome
```
# Install
# via http://askubuntu.com/questions/510056/how-to-install-google-chrome

wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
sudo sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
sudo apt-get update
sudo apt-get install google-chrome-stable


# Update

sudo apt-get --only-upgrade install google-chrome-stable
```
