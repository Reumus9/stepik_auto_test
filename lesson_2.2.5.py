from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math 

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:   
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)
    browser.find_element(By.ID, "answer").send_keys(y)
    browser.execute_script("window.scrollBy(0, 100);")
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()
    button = browser.find_element(By.CLASS_NAME, "btn")

    button.click()

finally:
    time.sleep(10)
    browser.quit()
