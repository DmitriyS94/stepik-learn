import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select


url = "http://suninjuly.github.io/selects1.html"

try:
    driver = webdriver.Chrome(executable_path="/home/dmitriy/PycharmProjects/stepik/chromedriver")
    driver.get(url)
    num1 = driver.find_element_by_xpath("//span[@id='num1']")
    x = num1.text
    num2 = driver.find_element_by_xpath("//span[@id='num2']")
    y = num2.text
    a = str(int(x)+int(y))
    select = Select(driver.find_element_by_tag_name("select"))
    select.select_by_value(a)
    submit = driver.find_element_by_xpath("//button[@type='submit']").click()
    time.sleep(15)

finally:
    driver.quit()