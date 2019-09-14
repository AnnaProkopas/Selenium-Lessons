import os 
from selenium import webdriver

link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

element = browser.find_element_by_id("answer")
current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
element.send_keys(file_path)
print(os.path.abspath(__file__))
print(os.path.abspath(os.path.dirname(__file__)))