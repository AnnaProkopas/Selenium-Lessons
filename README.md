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

# Тестовые фреймворки

[руководство про написание юнит-тестов в Python](https://realpython.com/python-testing/)

[ Пирамида тестов на практике](https://habr.com/ru/post/358950/)

### Выводим ошибки правильно

```python
assert self.is_element_present('new_announcement_button', timeout=30), "No new announcement button on profile page"
```
Способы сздания сообщений об ошибке:
- ```"Wrong text, got" + actual_result + ", something wrong"```
- ```"Let's count together! {}, then goes {}, and then {}".format("one", "two", "three")``` [подробнее](https://realpython.com/python-string-formatting/#2-new-style-string-formatting-strformat)
- [подробнее](https://realpython.com/python-string-formatting/#3-string-interpolation-f-strings-python-36)
```python
str1 = "one"
str2 = "two"
str3 = "third"
f"Let's count together! {str1}, then goes {str2}, and then {str3}"
```
> Переменная может сменить значение
>```python
>catalog_text = self.catalog_link.text # считываем текст и записываем его в переменную
>assert catalog_text == "Каталог", \
>    f"Wrong language, got {catalog_text} instead of 'Каталог'"  
>```

Можно выделить три основных тестовых фреймворка для Python: **unittest, PyTest** и **nose**.
## unittest
>название тестового метода должно начинаться со слова "test_" или заканчиваться словом "_test"
```python
def test_name_for_your_test():
```
- Тесты обязательно должны находиться в специальном тестовом классе
- Вместо assert должны использоваться специальные assertion методы

[документация unittest](https://docs.python.org/3/library/unittest.html)

## PyTest

1) 
   ```
   pip install pytest==5.1.1
   pytest test_abs_project.py
   ```

2) Подробный отчёт с поддержкой цветовых схем из коробки.

3) PyTest не требует написания дополнительных специфических конструкций в тестах, как того требует unittest (no boilerplate).

4) Для проверок используется стандартный assert из Python.

5) Возможность создания динамических фикстур (специальных функций, которые настраивают тестовые окружения и готовят тестовые данные).

6) Дополнительные возможности по настройке фикстур.

7) Параметризация тестов — для одного теста можно задать разные параметры (тест запустится несколько раз с разными тестовыми данными).

8) Наличие маркировок (marks), которые позволяют маркировать тесты для их выборочного запуска.

9)  Возможность передавать дополнительные параметры через командную строку для настройки тестовых окружений.

10) Большое количество плагинов, которые расширяют возможности PyTest и позволяют решать узкоспециализированные проблемы, что может сэкономить много времени.
    
Запуск:
```
pytest Module\ 3/lesson2_step12.py 
```
### Версии пакетов ...
Сохраняем:
```
pip freeze > requirements.txt
```
Читаем/качаем/устанавливаем:
```
pip install -r requirements.txt
```
- если мы не передали никакого аргумента в команду, а написали просто pytest, тест-раннер начнёт поиск в текущей директории
- как аргумент можно передать файл, путь к директории или любую комбинацию директорий и файлов, например: 
```python
pytest scpripts/selenium_scripts
# найти все тесты в директории scripts/selenium_scripts

pytest test_user_interface.py
# найти и выполнить все тесты в файле 

pytest scripts/drafts.py::test_register_new_user_parametrized
# найти тест с именем test_register_new_user_parametrized в указанном файле в указанной директории и выполнить 
```
- дальше происходит рекурсивный поиск: то есть PyTest обойдет все вложенные директории
- во всех директориях PyTest ищет файлы, которые удовлетворяют правилу  test_*.py или *_test.py (то есть начинаются на test_ или заканчиваются _test и имеют расширение .py)
- внутри всех этих файлов находит тестовые функции по следующему правилу:
  - все тесты, название которых начинается с test, которые находятся вне классов
  - все тесты, название которых начинается с test внутри классов, имя которых начинается с Test (и без метода __init__ внутри класса)

[Conventions for Python test discovery](https://docs.pytest.org/en/latest/goodpractices.html#conventions-for-python-test-discovery)\
[Полезные команды для Pytest](https://gist.github.com/amatellanes/12136508b816469678c2)
```python
pytest -v 
#verbose, то есть подробный
```
## fixtures

Фикстуры в контексте PyTest — это вспомогательные функции для наших тестов, которые не являются частью тестового сценария.

Фикстура, возвращающая значение:

```python
@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    return browser

class TestMainPage1():
    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, browser):
```
Для каждого метода создается новый browser.

**Финализаторы**
```python
@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    # этот код выполнится после завершения теста
    print("\nquit browser..")
    browser.quit()
```
Иначе:
```python
@pytest.fixture()
def browser(request):
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    def fin():
        print("\nquit browser..")
        browser.close()
    request.addfinalizer(fin)
    return browser
```
Управление областью видимости ***scope***: **“function”, “class”, “module”, “session”**. Фикстура вызовется один раз для метода/класса/модуля/всех тестов, запущеннных в сессии.
```python
@pytest.fixture(scope="class")
```
Автовызов фикстуры:
```python
@pytest.fixture(autouse=True)
```
[habr](https://habr.com/ru/company/yandex/blog/242795/)\
[medium](https://medium.com/@dmrlx/%D0%B2%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5-%D0%B2-pytest-cc6175c7d0dc)\
[docs.pytest](https://docs.pytest.org/en/latest/fixture.html)

## Маркировка тестов
Маркируем методы и классы:
```python
@pytest.mark.mark_name
```
Запуск:
```
pytest -s -v -m mark_name test_file.py
```
Но надо сделать это явно:\
pytest.ini
```
[pytest]
markers =
    mark_name1: marker for ...
    mark_name2: comment, not required
    win10
```
### Инверсия 
```
pytest -s -v -m "not mark_name" test_file.py
```
### Объединение
```
pytest -s -v -m "mark_name1 or mark_name2" test_file.py
```
### Пересечение, один тест - несколько макировок
```
pytest -s -v -m "mark_name1 and win10" test_file.py
```
### Пропуск теста
```python
@pytest.mark.skip
```
### В ожидании падения
```python
@pytest.mark.xfail
```
Когда починят: **XPASS** (“unexpectedly passing” - неожиданно проходит)

Указывать причины - хороший тон.
```python
    @pytest.mark.xfail(reason="fixing this bug right now")
```
Запуск с reason:
```python
pytest -rx -v test_fixture10a.py
#подробности по XPASS
pytest -rX -v test_fixture10b.py
```
[Подробнее в документации](https://docs.pytest.org/en/latest/skipping.html)
## Параметризация, конфигурирование, плагины