from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

url = "http://suninjuly.github.io/explicit_wait2.html"

try:
    driver= webdriver.Chrome(executable_path="/home/dmitriy/PycharmProjects/stepik/chromedriver")
    driver.get(url)
    # driver.implicitly_wait(15)
    # result = driver.find_element_by_xpath("//")
    button = WebDriverWait(driver, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    button_book = driver.find_element_by_xpath("//button[@id='book']").click()
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
