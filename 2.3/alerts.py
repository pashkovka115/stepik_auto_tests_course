from time import sleep
import os
from selenium import webdriver



link = "http://suninjuly.github.io/file_input.html"

browser = webdriver.Chrome()
browser.get(link)
sleep(1)

try:
    alert = browser.switch_to.alert
    alert.accept()

    confirm.dismiss()

    prompt = browser.switch_to.alert
    prompt.send_keys("My answer")
    prompt.accept()

finally:
    sleep(20)
    browser.quit()



