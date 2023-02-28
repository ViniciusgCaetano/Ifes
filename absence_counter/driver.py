from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser=webdriver.Firefox()
browser.get("https://wiki.ubuntu.com")
element=browser.find_element(By.ID,"searchinput")
element.send_keys("typing")
print(element)
time.sleep(3)
browser.close()

