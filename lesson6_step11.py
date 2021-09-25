from selenium import webdriver
import time

url = "http://suninjuly.github.io/registration2.html"

try:
    driver = webdriver.Chrome(executable_path="/home/dmitriy/PycharmProjects/stepik/chromedriver")
    driver.get(url)
    first_name = driver.find_element_by_xpath("//input[@type='text'][@class='form-control first'][@placeholder='Input your name']")
    first_name.send_keys("Dmitriy")
    email = driver.find_element_by_xpath("//input[@type='text'][@class='form-control third'][@placeholder='Input your email']")
    email.send_keys("test@gmail.com")
    phone = driver.find_element_by_xpath("//input[@type='text'][@class='form-control first'][@placeholder='Input your phone']")
    phone.send_keys("12345678")
    address = driver.find_element_by_xpath("//input[@type='text'][@class='form-control second'][@placeholder='Input your address']")
    address.send_keys("Cheboksary")
    button = driver.find_element_by_xpath("//button[@type='submit']").click()
    time.sleep(2)
    welcome_text_elt = driver.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    print(welcome_text)
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(3)
    driver.quit()
