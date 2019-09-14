from selenium import webdriver
import time

try: 
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    classes = ["first", "second", "third"]
    for i in range(len(classes)):
        browser.find_element_by_css_selector("div.first_block ." + classes[i]).send_keys("0")

    browser.find_element_by_css_selector("button.btn").click()
    time.sleep(1)

    welcome_text = browser.find_element_by_tag_name("h1").text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()