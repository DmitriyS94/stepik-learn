from selenium import webdriver
import time
import math

url = "http://suninjuly.github.io/find_xpath_form"
# url1 = "http://suninjuly.github.io/simple_form_find_task.html"
# url2 = "http://suninjuly.github.io/find_link_text"
# a = str(math.ceil(math.pow(math.pi, math.e)*10000))

try:
    driver = webdriver.Chrome(executable_path='/home/dmitriy/PycharmProjects/stepik/chromedriver')
    driver.get(url)
    input1 = driver.find_element_by_tag_name("input")
    input1.send_keys("Dmitriy")
    input2 = driver.find_element_by_name("last_name")
    input2.send_keys("Suslov")
    input3 = driver.find_element_by_class_name("form-control.city")
    input3.send_keys("Cheboksary")
    input4 = driver.find_element_by_id("country")
    input4.send_keys("Russia")
    button = driver.find_element_by_xpath("//button[@type='submit']")
    button.click()

finally:
    time.sleep(10)
    driver.quit()