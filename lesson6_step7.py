import time
from selenium import webdriver

url = "http://suninjuly.github.io/huge_form.html"

try:
    driver = webdriver.Chrome(executable_path="/home/dmitriy/PycharmProjects/stepik/chromedriver")
    driver.get(url)
    elements = driver.find_elements_by_tag_name("input")
    for element in elements:
        element.send_keys("null")

    button = driver.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(15)
    driver.quit()
