import time
from selenium import webdriver
import math

url = "http://suninjuly.github.io/get_attribute.html"

try:
    driver = webdriver.Chrome(executable_path="/home/dmitriy/PycharmProjects/stepik/chromedriver")
    driver.get(url)
    number = driver.find_element_by_id("treasure")
    number_checked = number.get_attribute("valuex")
    x = number_checked
    y = str(math.log(abs(12 * math.sin(int(x)))))
    result = driver.find_element_by_xpath("//input[@id='answer']")
    result.send_keys(y)
    not_robot = driver.find_element_by_css_selector("[id='robotCheckbox']").click()
    robot_ruled = driver.find_element_by_css_selector("[id='robotsRule']").click()
    button = driver.find_element_by_xpath("//button[@type='submit']").click()
    time.sleep(10)
finally:
    driver.quit()