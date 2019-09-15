import unittest
from selenium import webdriver
import time

class TestAbs(unittest.TestCase):
    def test_registration1_test(self):
        self.registration_on_link("http://suninjuly.github.io/registration1.html")
    def test_registration2_test(self):
        self.registration_on_link("http://suninjuly.github.io/registration2.html")

    def registration_on_link(self, link):
        browser = webdriver.Chrome()
        browser.get(link)
        classes = ["first", "second", "third"]
        for i in range(len(classes)):
            browser.find_element_by_css_selector("div.first_block ." + classes[i]).send_keys("0")
        browser.find_element_by_css_selector("button.btn").click()
        time.sleep(1)
        welcome_text = browser.find_element_by_tag_name("h1").text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, f"Welcome text is '{welcome_text}''")
        browser.quit()

if __name__ == "__main__":
    unittest.main()