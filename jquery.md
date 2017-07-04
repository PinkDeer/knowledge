[Atom](/atom.md) || [Bash](bash.md) || [CSS](css.md) || [Gems](/gems.md) || [Github](/github.md) || [HTML](html.md) || [jQuery](/jquery.md) || [Linux](/linux.md) || [Rails](rails.md) || [Ruby](ruby.md) || [SQL](sql.md) || [SSH](ssh.md) || [Tasks](tasks.md)

## jQuery


* [Основы](#основы)
* [Плагины](#Плагины)

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
[![up](/image/up.png)](#jquery)

#### Плагины  

##### Very simple jQuery color picker

[Github](https://github.com/tkrotoff/jquery-simplecolorpicker)

Разбор: 1.30 [Ruby School (Video) lessons 23](https://vimeo.com/104440956)  
Пример: [Ruby School, (Github) lessons 23](https://github.com/PinkDeer/ruby/tree/master/rubyschool/lesson23)

Cкачать
```
wget https://raw.githubusercontent.com/tkrotoff/jquery-simplecolorpicker/master/jquery.simplecolorpicker.css
wget https://raw.githubusercontent.com/tkrotoff/jquery-simplecolorpicker/master/jquery.simplecolorpicker.js
```
Подллючение в layout
```
<script src="jquery.simplecolorpicker.js"></script>
<link rel="stylesheet" href="jquery.simplecolorpicker.css">
```
HTML
```
<select name="colorpicker">
  <option value="#7bd148">Green</option>
  <option value="#5484ed">Bold blue</option>
  ...
  <option value="#e1e1e1">Gray</option>
</select>
```
javascript
```
$('select[name="colorpicker"]').simplecolorpicker();
```


##### datetimepicker

[Github](https://github.com/xdan/datetimepicker)

Разбор 1.10 https://vimeo.com/105281212  
Пример: [Ruby School, (Github) lessons 26](https://github.com/PinkDeer/ruby/tree/master/rubyschool/lesson26)

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
[![up](/image/up.png)](#jquery)
