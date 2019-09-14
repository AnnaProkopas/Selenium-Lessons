Это конспект пройденных лекций. Да, мне удобно вести его так ))
--------------------------
```
python3 -m venv selenium_env
source selenium_env/bin/activate
```

## Управляем браузером:

```python
from selenium import webdriver
driver = webdriver.Chrome()
textarea = driver.find_element_by_css_selector(".textarea")
textarea.send_keys("get()")
submit_button = driver.find_element_by_css_selector(".submit-submission")
submit_button.click()
driver.quit()
```
Введение
========================
Удобно добавлять собственные аттрибуты на страницу для стабильности тестов, их особенности:

  -   веб-сайт должен использовать стандарт HTML5 (большинство современных сайтов соответствует этому требованию)
  -   атрибут всегда должен начинаться со слова: **data**, например, data-button
  -   использовать можно только латинские буквы, дефис (-), двоеточие (:) и подчёркивание ( _ )

Искать лучше так: [id="bullet"], вместо \#bullet.
Но для классов эффективнее .lead или с уточнением: .lead.text-muted, вместо [class="lead"].
**Поиск классов чувствителен к регистру:** .Lead.
Используем связи!

  -  родителя и потомка: \#post2 .title
  -  родитель и дочерний: \#post2 > div.title 
  -  родитель и порядковый номер потомка: \#posts > .item:nth-child(2) > .title
  -  несколько классов: .title.second

## Статьи для CSS:
[learn.javascript.ru](https://learn.javascript.ru/css-selectors)\
[www.w3schools.com](https://www.w3schools.com/cssref/css_selectors.asp)\
[developer.mozilla.org](https://developer.mozilla.org/ru/docs/Web/CSS/CSS_%D0%A1%D0%B5%D0%BB%D0%B5%D0%BA%D1%82%D0%BE%D1%80%D1%8B)
# XPath
1.  XPath запрос всегда начинается с символа / или //
	
	-  ```/ ->  ">"```
	-  ```// -> "_"```
	
	Начинаем всегда с вершины дерева - html
	
	-   ```/html/body/header```
	-   ```//header```
	
2.  Символ [ ] - это команда фильтрации
	
	-  аттрибут (id, class, title) ```//img[@id='bullet']```
	-  порядковый номер ```//div[@class="row"]/div[2]```
	-  полное совпадение текста ```//p[text()="Lenin cat"]```
	-  частичное совпадение текста или атрибута: ```//p[contains(text(), "cat")]``` и  ```//div[contains(@class, "navbar")]```
	-  булевые операции: and, or, not ```//img[@name='bullet-cat' and @data-type='animal']```
	
3.  Символ * - команда выбора всех элементов
	```//div/*[@class="jumbotron-heading"]```
4.  Поиск по классу в XPath регистрозависим
	```//div/*[@class="Jumbotron-heading"]``` не найдёт элемента на странице
##  Особенности приятного использования XPath:

-  Что важно знать про XPath, чтобы пользоваться им безболезненно:
-  Не используйте селекторы вида //div[1]/div[2]/div[3] без крайней нужды: по такому селектору невозможно с первого раза понять, что за элемент вы ищете. А когда структура страницы хоть немного изменится, то ваш селектор с большой вероятностью перестанет работать;
-  Если есть возможность использовать CSS-селекторы: сlass, id или name - лучше использовать их вместо поиска по XPath;
-  Можно искать по полному или частичному совпадению текста или любого атрибута;
-  Можно использовать булевы операции и простую арифметику;
-  Можно удобно перемещаться по структуре документа (переходить к потомкам и к родителям);
-  Подойдет, когда у сайта всё плохо с атрибутами и нет возможности достучаться до разработчиков;
-  Есть мнение, что поиск по XPath в среднем медленнее, чем по css. Но достоверно это неизвестно;
-  Не стоит использовать разные расширения для браузеров по поиску XPath: они подбирают нечитабельные и переусложненные селекторы. Лучше потратить немного времени и разобраться в синтаксисе самостоятельно, тем более, что он не очень сложный.

### Полезные ссылки при изучении XPath:

-  [w3schools](https://www.w3schools.com/xml/xpath_syntax.asp}
-  [microsoft](https://msdn.microsoft.com/ru-ru/library/ms256086(v=vs.120).aspx}
-  [msiter](https://msiter.ru/tutorials/xpath/syntax}
-  [habr](https://habr.com/post/114772/}
-  [internetka](http://internetka.in.ua/xpath-start-part1/}
-  [internetka](http://internetka.in.ua/xpath-start-part2/}
-  [herinternetkae](http://internetka.in.ua/xpath-start-part3/}
-  [internetka](http://internetka.in.ua/xpath-start4/}
-  [testerslittlehelper](https://testerslittlehelper.wordpress.com/2016/07/10/real-xpath/}
-  [drive.google](https://drive.google.com/file/d/0B_IyyodHL4rXcU1BY1R1TzFXbmc/view}

# Поиск элементов при помощи Selentium


-  **find_element_by_id**
-  **find_element_by_css_selector**
-  **find_element_by_xpath**
-  find_element_by_name
-  find_element_by_tag_name
-  find_element_by_class_name
-  find_element_by_link_text
-  find_element_by_partial_link_text

```python
from selenium.webdriver.common.by import By
#...
browser.find_element(By.ID, "submit_button")
```

```python
By.ID 
By.CSS_SELECTOR 
By.XPATH
By.NAME
By.TAG_NAME 
By.CLASS_NAME 
By.LINK_TEXT
By.PARTIAL_LINK_TEXT 
```

 \colorbox{whitecodegray}{browser.close()} \# закроет текущее
 \colorbox{whitecodegray}{browser.quit()} \# закроет открытые
 Добавим \colorbox{whitecodegray}{ try/finally} для закрытия даже с ошибкой выполнения 
### find_elements
 
 ```python
 x_element.get_attribute("valuex")
 ```
 Значение аттрибута отсутствует \rightarrow "false"
 Аттрибут не задан явно \rightarrow "true"
 Аттрибута нет \rightarrow None
 ### Списки, обычные и выпадающие
 
 -  У каждого элемента списка обычно есть уникальное значение атрибута value
 -  В списках может быть разрешено выбирать как только один, так и несколько вариантов, в зависимости от типа списка
 -  Визуально списки могут различаться тем, что в одном случае все варианты скрыты в выпадающем меню ([here](http://suninjuly.github.io/selects1.html}), а в другом все варианты или их часть видны ([here](http://suninjuly.github.io/selects2.html})
 
 Специальный класс Select:
 ```python
 from selenium.webdriver.support.ui import Select
select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value("1") 
 ```
 Методы:
 
 -  select_by_value( "value" )
 -  select.select_by_visible_text( "text" )
 -  select.select_by_index(index) - с нуля
 
 ### Метод execute_script
 
```python
    browser = webdriver.Chrome()
    #browser.execute_script("alert('Robots at work');")
    #browser.execute_script("document.title='Script executing';")
    #browser.execute_script('document.title="Script executing";')
    browser.execute_script("document.title='Script executing';alert('Robots at work');") 
```
 Кнопка может быть перекрыта:
```python
button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()
```
 На определенное количество пикселей:
```python
browser.execute_script("window.scrollBy(0, 100);")
```
 На Js:
```javascript
button = document.getElementsByTagName("button")[0];
button.scrollIntoView();
```

### Загрузка файлов
 
```python
import os 

current_dir = os.path.abspath(os.path.dirname(__file__))    
file_path = os.path.join(current_dir, 'file.txt')          
element.send_keys(file_path)
```
Подробности о модуле os:
[here](https://docs.python.org/3/library/os.path.html}
### Alert

```python
alert = browser.switch_to.alert
alert.accept()
alert_text = alert.text
```
### Confirm

```python
confirm = browser.switch_to.alert
confirm.accept()
confirm.dismiss()
```
### Prompt

```python
prompt = browser.switch_to.alert
prompt.send_keys("My answer")
prompt.dismiss()
prompt.accept()
```
### Смена вкладки браузера

массив имен вкладок (текущая, вторая вкладка):
```python
browser.window_handles[0]
browser.window_handles[1]
```
переключение между вкладками:
```python
browser.switch_to.window(window_name)
```
Т. к. WebDriver работает только с одной вкладкой.
### Неявное ожидание (Implicit wait)

WebDriver ищет каждый элемент в течение 5 секунд:
```python
browser.implicitly_wait(5)
```

Если произойдет ошибка, то WebDriver выбросит одно из следующих исключений (exceptions):

-  Если элемент не был найден за отведенное время, то мы получим NoSuchElementException.
-  Если элемент был найден в момент поиска, но при последующем обращении к элементу DOM изменился, то получим StaleElementReferenceException. Например, мы нашли элемент Кнопка и через какое-то время решили выполнить с ним уже известный нам метод click. Если кнопка за это время была скрыта скриптом, то метод применять уже бесполезно — элемент "устарел" (stale) и мы увидим исключение.
-  Если элемент был найден в момент поиска, но сам элемент невидим (например, имеет нулевые размеры), и реальный пользователь не смог бы с ним взаимодействовать, то получим ElementNotVisibleException.


Рассмотрим пример с кнопкой, которая отправляет данные:

-  Кнопка может быть неактивной, то её нельзя кликнуть;
Кнопка может содержать текст, который меняется в зависимости от действий пользователя. Например, текст "Отправить" после нажатия кнопки поменяется на "Отправлено";
-  Кнопка может быть перекрыта каким-то другим элементом или быть невидимой.

### Явное ожидание (Explicit wait)}

```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
#...
button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "verify"))
    )
```
Правила модуля expected_conditions:

-  title_is
-  title_contains
-  presence_of_element_located
-  visibility_of_element_located
-  visibility_of
-  presence_of_all_elements_located
-  text_to_be_present_in_element
-  text_to_be_present_in_element_value
-  frame_to_be_available_and_switch_to_it
-  invisibility_of_element_located
-  element_to_be_clickable
-  staleness_of
-  element_to_be_selected
-  element_located_to_be_selected
-  element_selection_state_to_be
-  element_located_selection_state_to_be
-  alert_is_present

[selenium-python](https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.expected_conditions)

## Дополнительные ссылки
В этом уроке мы постарались собрать ссылки на ресурсы, где вы сможете найти дополнительную информацию по использованию Selenium и о тонкостях при работе с ним:

**Общее**

-  [selenium-python](https://selenium-python.com/)
-  [selenium-python](http://selenium-python.readthedocs.io)
-  [chrome.driver](http://chrome.driver.chromium.org/getting-started)
-  [guru99](https://www.guru99.com/selenium-tutorial.html) - Туториал на английском, ориентирован на Java.﻿
-  [guru99](https://www.guru99.com/live-selenium-project.html) - Можно попробовать писать автотесты для демо-сайта ﻿банка. Тоже Java.
-  [barancev](http://barancev.github.io/good-locators/) - что такое хорошие селекторы
-  [barancev](http://barancev.github.io/what-is-path-env-var/) - что за PATH переменная? 

**Ожидания в Selenium WebDriver**

- [seleniumhq]https://docs.seleniumhq.org/docs/04_webdriver_advanced.jsp)
- [selenium-python]https://selenium-python.readthedocs.io/waits.html)
- [selenium-python]https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.expected_condition)
- [stackoverflow]https://stackoverflow.com/questions/15122864/selenium-wait-until-document-is-ready)
- [codeship]https://blog.codeship.com/get-selenium-to-wait-for-page-load/)

# Текстовые фреймворки
