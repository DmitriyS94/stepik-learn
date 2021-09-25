import time
from selenium import webdriver
import math

url = "http://suninjuly.github.io/math.html"


# def calc(x):
#     return str(math.log(abs(12 * math.sin(int(x)))))

try:
    driver = webdriver.Chrome(executable_path="/home/dmitriy/PycharmProjects/stepik/chromedriver")
    driver.get(url)
    # time.sleep(1)
    x_element = driver.find_element_by_xpath("//span[@id='input_value']")
    # time.sleep(5)
    x = x_element.text
    y = str(math.log(abs(12 * math.sin(int(x)))))
    result = driver.find_element_by_xpath("//input[@id='answer']")
    result.send_keys(y)
    not_robot = driver.find_element_by_css_selector("[for='robotCheckbox']").click()
    robot_ruled = driver.find_element_by_css_selector("[for='robotsRule']").click()
    button = driver.find_element_by_xpath("//button[@type='submit']").click()
    time.sleep(10)
finally:
    driver.quit()










