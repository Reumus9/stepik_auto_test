from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "https://suninjuly.github.io/explicit_wait2.html"
try:
    browser.get(link)
    browser.implicitly_wait(3)
    WebDriverWait(browser,13).until(ec.text_to_be_present_in_element((By.ID, 'price'),"$100"))
    browser.find_element(By.ID, "book").click()
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)
    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.ID, "solve").click()
finally:

    time.sleep(10)
    browser.quit()








