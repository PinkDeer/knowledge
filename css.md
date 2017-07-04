[Atom](/atom.md) || [Bash](bash.md) || [CSS](css.md) || [Gems](/gems.md) || [Github](/github.md) || [HTML](html.md) || [jQuery](/jquery.md) || [Linux](/linux.md) || [Rails](rails.md) || [Ruby](ruby.md) || [SQL](sql.md) || [SSH](ssh.md) || [Tasks](tasks.md)

## CSS

* [sass](#sass)
	* [Вложения](#Вложения)
	* [Переменные](#Переменные)


### sass


---


#### Вложения

Пример 1:


.css
```
.center {
  text-align: center;
}
.center h1 {
  margin-bottom: 10px;
}
```
.scss
```
.center {
  text-align: center;
  h1 {
    margin-bottom: 10px;
  }
}
```


Пример 2:
.css
```
#logo {
  float: left;
  margin-right: 10px;
  font-size: 1.7em;
  color: #fff;
  text-transform: uppercase;
  letter-spacing: -1px;
  padding-top: 9px;
  font-weight: bold;
}
#logo:hover {
  color: #fff;
  text-decoration: none;
}
```
.scss
```
#logo {
  float: left;
  margin-right: 10px;
  font-size: 1.7em;
  color: #fff;
  text-transform: uppercase;
  letter-spacing: -1px;
  padding-top: 9px;
  font-weight: bold;
  &:hover {
    color: #fff;
    text-decoration: none;
  }
 }
```

[![up](/image/up.png)](#css)


#### Переменные


.css
```
h2 {
  .
  .
  .
  color: #777;
}
.
.
.
footer {
  .
  .
  .
  color: #777;
}
```
.scss добавляем переменную _$light-gray: #777;_
```
$light-gray: #777;
.
.
.
h2 {
  .
  .
  .
  color: $light-gray;
}
.
.
.
footer {
  .
  .
  .
  color: $light-gray;
}
```
[![up](/image/up.png)](#css)


[Atom](/atom.md) || [Bash](bash.md) || [CSS](css.md) || [Gems](/gems.md) || [Github](/github.md) || [HTML](html.md) || [jQuery](/jquery.md) || [Linux](/linux.md) || [Rails](rails.md) || [Ruby](ruby.md) || [SQL](sql.md) || [SSH](ssh.md) || [Tasks](tasks.md)
