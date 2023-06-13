import time
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("http://suninjuly.github.io/file_input.html")

driver.find_element("name", "firstname").send_keys("Vitali")
driver.find_element("name", "lastname").send_keys("Clicev")
driver.find_element("name", "email").send_keys("test@test.test")

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'test.txt')
driver.find_element("id", "file").send_keys(file_path)

driver.find_element("class name", "btn.btn-primary").click()
time.sleep(10)
