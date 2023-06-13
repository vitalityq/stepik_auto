import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


driver.get("http://suninjuly.github.io/explicit_wait2.html")

button = driver.find_element("id", "book")

WebDriverWait(driver, 12).until(
    EC.text_to_be_present_in_element(("id", "price"), "100")
)
button.click()
driver.execute_script("window.scrollBy(0, 100);")


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


x_element = driver.find_element("css selector", "#input_value")
x = x_element.text
y = calc(x)
driver.find_element("id", "answer").send_keys(y)
button = driver.find_element("id", "solve")
button.click()

time.sleep(10)
