from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector("[name='lastname']")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector("[name='email']")
    input3.send_keys("ivan_petrov@mail.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')  
    browser.find_element_by_id("file").send_keys(file_path)
    browser.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(30)
    browser.quit()