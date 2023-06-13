import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import math


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


driver.get("http://suninjuly.github.io/alert_accept.html")

driver.find_element("class name", "btn.btn-primary").click()

confirm = driver.switch_to.alert
confirm.accept()


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


x_element = driver.find_element("css selector", "#input_value")
x = x_element.text
y = calc(x)

driver.find_element("id", "answer").send_keys(y)

driver.find_element("class name", "btn.btn-primary").click()

time.sleep(10)
