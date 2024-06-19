from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
from selenium.webdriver.support.ui import Select

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x= browser.find_element(By.ID, "num1").text
    y= browser.find_element(By.ID, "num2").text
    Select(browser.find_element(By.ID, "dropdown")).select_by_value(str(int(x)+int(y)))
    browser.find_element(By.CLASS_NAME, "btn").click()
finally:
    time.sleep(15)
    browser.quit()