## mvc

### Заметки

#### Контроллеры

Метод _index_ возвращает строку:
```
public string Index()
{
    return "Text";
}
```

Объект _ViewResult_ создается посредством вызова метода View с указанием представления:
```
 public ViewResult Index()
        {

            return View("MyView");  
        }
```

__ViewBag__ - динамический объект, в котором можно устанавливать произвольные свойства, делая их значения доступными в представлении.  
Пример:  
controller
```
public ViewResult Index()
{
    int hour = DateTime.Now.Hour;
    ViewBag.Greeting = hour < 12 ? "Good Morning" : "Good Afternoon";
    return View("MyView");  
}
```
view
```
<p>@ViewBag.Greeting, World!</p>
```

Если метод действия вызывает метод _View_ без аргументов, то визуализируется стандартное представление, у которого будет такое же имя как и у метода действия.  
Например, в данном случае представление будет иметь имя _Form.cshtml_
```
public ViewResult Form()
{
    return View();
}
```


#### Представления

Представления не являющиеся специфическими для отдельного контроллера, хранятся в папке под названием _Views/Shared_.  

URL для метода действия определенного в том же контроллере, для которого визуализируется представление 
```
<a asp-action="Form">Click</a>
```
