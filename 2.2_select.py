import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import math
from selenium.webdriver.support.ui import Select


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://suninjuly.github.io/selects1.html")

x_element = driver.find_element("id", "num1")
y_element = driver.find_element("id", "num2")
x = x_element.text
y = y_element.text
z = int(x) + int(y)

select = Select(driver.find_element("tag name", "select"))
select.select_by_value(str(z))

driver.find_element("class name", "btn.btn-default").click()
time.sleep(10)
