from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/simple_form_find_task.html")
button = browser.find_element_by_id("submit_button")
browser.quit()

#----------------------------------------------------------------------------
#from selenium import webdriver

from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/simple_form_find_task.html")
button = browser.find_element(By.ID, "submit_button")
browser.quit()