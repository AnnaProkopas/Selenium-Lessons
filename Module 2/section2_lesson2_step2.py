from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x1 = browser.find_element_by_id("num1").text
    print(x1)
    x2 = browser.find_element_by_id("num2").text
    y = int(x1) + int(x2)
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_visible_text(str(y)) 

    browser.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(10)
    browser.quit()