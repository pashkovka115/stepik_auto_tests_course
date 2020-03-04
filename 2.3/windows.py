from time import sleep
import os
from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))



link = "http://suninjuly.github.io/alert_accept.html"

browser = webdriver.Chrome()
browser.get(link)
sleep(1)

try:
    browser.switch_to.window(window_name)
    first_window = browser.window_handles[0]
    new_window = browser.window_handles[1]

finally:
    sleep(20)
    browser.quit()



