import time
from selenium import webdriver
import math

url = "http://suninjuly.github.io/alert_accept.html"

try:
    driver = webdriver.Chrome(executable_path="/home/dmitriy/PycharmProjects/stepik/chromedriver")
    driver.get(url)
    accept = driver.find_element_by_xpath("//button[@type='submit']").click()
    alert = driver.switch_to.alert
    alert.accept()
    exec_num = driver.find_element_by_xpath("//span[@id='input_value']")
    x = exec_num.text
    y = str(math.log(abs(12 * math.sin(int(x)))))
    result = driver.find_element_by_xpath("//input[@id='answer']")
    result.send_keys(y)
    submit = driver.find_element_by_xpath("//button[@type='submit']").click()
    alert_result = driver.switch_to.alert
    alert_result = alert.text
    print(alert_result)
    # time.sleep(20)


finally:
    driver.quit()
