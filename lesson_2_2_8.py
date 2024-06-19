from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
link = "https://suninjuly.github.io/file_input.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.NAME, "firstname").send_keys("Dmitrii")
    browser.find_element(By.NAME, "lastname").send_keys("Arbuzov")
    browser.find_element(By.NAME, "email").send_keys("arbuzvkysniy@gmail.com")
    patch = os.path.abspath(os.path.dirname(__file__))
    patch1 = os.path.join(patch, "file_2.2.8.txt")
    browser.find_element(By.ID, "file").send_keys(patch1)
    browser.find_element(By.CLASS_NAME, "btn").click()

finally:
    time.sleep(10)
    browser.quit()