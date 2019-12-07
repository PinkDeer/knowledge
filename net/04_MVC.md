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

#### Представления

Представления не являющиеся специфическими для отдельного контроллера, хранятся в папке под названием _Views/Shared_.