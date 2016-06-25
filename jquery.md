[Atom](/atom.md) [Bash](bash.md) [Gems](/gems.md) [Github](/github.md) [jQuery](/jquery.md) [HTML](html.md) [Rails](rails.md) [Ruby](ruby.md) [Tasks](tasks.md)

## jQuery


* [Основы](#основы)
* [Пакеты](#Плагины)

#### Основы:

[Ruby School, (Github) lessons 23](https://github.com/PinkDeer/ruby/tree/master/rubyschool/lesson23)

$('  ')...

$ - вызов jQuery
('   ') - задаем параметр, в кавычках селектор
Селектор может иметь вид: #aaa, .aaa
C "решеткой" необходимо обращаться по id (по идентификатору), в элеметна задается атрибут id
"Точка" помещается - в класс


Если jQuery вызывается в body, то код ниже выполняется только после полной загрузке страницы
```
<script>
  $(function()  {
    // любой javascript код
  });
</script>
```

#### Плагины  

##### jQuery color picker

[Github](https://github.com/tkrotoff/jquery-simplecolorpicker)

Разбор: 1.30 [Ruby School (Video) lessons 23](https://vimeo.com/104440956)

Код: [Ruby School, (Github) lessons 23](https://github.com/PinkDeer/ruby/tree/master/rubyschool/lesson23)


#####

[Github](https://github.com/xdan/datetimepicker)
Разбор 1.10 https://vimeo.com/105281212

Скачать

```
wget https://raw.githubusercontent.com/xdan/datetimepicker/master/jquery.datetimepicker.css
wget https://raw.githubusercontent.com/xdan/datetimepicker/master/jquery.datetimepicker.js
```

 Подллючение в layout

 ```
 <script src="jquery.datetimepicker.js"></script>
 <link rel="stylesheet" href="jquery.datetimepicker.css">
 ```
 HTML
 ```
 <input id="datetimepicker" type="text" >
 ```
 javascript
 ```
 jQuery('#datetimepicker').datetimepicker();
 ```
