# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# browser = webdriver.Chrome()
# browser.get("http://suninjuly.github.io/wait1.html")
#
# time.sleep(1)
# button = browser.find_element(By.ID, "verify")
# button.click()
# message = browser.find_element(By.ID, "verify_message")
#
# assert "successful" in message.text
# time.sleep(5)
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
# говорим WebDriver искать каждый элемент в течение 5 секунд
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/wait1.html")

button = browser.find_element(By.ID, "verify")
button.click()
message = browser.find_element(By.ID, "verify_message")

assert "successful" in message.text
time.sleep(5)
