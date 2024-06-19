from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

try:
    link = " http://suninjuly.github.io/find_link_text"
    chrome = webdriver.Chrome()
    chrome.get(link)

    link1 = chrome.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
    link1.click()

    input1 = chrome.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = chrome.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = chrome.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Smolensk")
    input4 = chrome.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = chrome.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(10)
finally:
    chrome.quit()
