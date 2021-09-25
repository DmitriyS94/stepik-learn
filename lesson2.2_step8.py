import time
from selenium import webdriver
import os


url = "http://suninjuly.github.io/file_input.html"

try:
    driver = webdriver.Chrome(executable_path="/home/dmitriy/PycharmProjects/stepik/chromedriver")
    driver.get(url)
    name = driver.find_element_by_xpath("//input[@type='text'][@name='firstname']")
    name.send_keys("Dmitriy")
    lastname = driver.find_element_by_xpath("//input[@type='text'][@name='lastname']")
    lastname.send_keys("Suslov")
    email = driver.find_element_by_xpath("//input[@type='text'][@name='email']")
    email.send_keys("test@gmail.com")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test.txt')
    element = driver.find_element_by_xpath("//input[@type='file'][@id='file']")
    element.send_keys(file_path)
    submit = driver.find_element_by_xpath("//button[@type='submit']").click()
    time.sleep(15)

finally:
    driver.quit()

