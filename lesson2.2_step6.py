import time
import math
from selenium import webdriver
from selenium.webdriver.support.ui import Select

url = "http://suninjuly.github.io/execute_script.html"

try:
    driver = webdriver.Chrome(executable_path="/home/dmitriy/PycharmProjects/stepik/chromedriver")
    driver.get(url)
    x_element = driver.find_element_by_xpath("//span[@id='input_value']")
    x = x_element.text
    y = str(math.log(abs(12 * math.sin(int(x)))))
    driver.execute_script("window.scrollBy(0, 150);")
    result = driver.find_element_by_xpath("//input[@id='answer']")
    result.send_keys(y)
    iamrobot = driver.find_element_by_css_selector("[for='robotCheckbox']").click()
    robotsRule = driver.find_element_by_css_selector("[for='robotsRule']").click()
    button = driver.find_element_by_xpath("//button[@type='submit']").click()
    time.sleep(10)
finally:
    driver.quit()
