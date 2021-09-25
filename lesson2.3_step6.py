import textwrap
import time
from selenium import webdriver
import math

url = "http://suninjuly.github.io/redirect_accept.html"

try:
    driver = webdriver.Chrome(executable_path="/home/dmitriy/PycharmProjects/stepik/chromedriver")
    driver.get(url)
    first_window = driver.window_handles[0]
    button = driver.find_element_by_xpath("//button[@type='submit']").click()
    window = driver.window_handles[1]
    driver.switch_to.window(window)
    exec_num = driver.find_element_by_xpath("//span[@id='input_value']")
    x = exec_num.text
    y = str(math.log(abs(12 * math.sin(int(x)))))
    result = driver.find_element_by_xpath("//input[@id='answer']")
    result.send_keys(y)
    submit = driver.find_element_by_xpath("//button[@type='submit']").click()
    alert = driver.switch_to.alert
    alert = alert.text
    print(alert)

finally:
    driver.quit()
