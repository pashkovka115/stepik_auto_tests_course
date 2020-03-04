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
    browser.find_element_by_tag_name('button').click()
    browser.switch_to.alert.accept()

    sleep(1)
    result = browser.find_element_by_id('input_value').text
    x = calc(result)

    input_text = browser.find_element_by_css_selector('input[type="text"]')
    input_text.send_keys(x)

    button = browser.find_element_by_tag_name('button')
    button.click()

    # 28.92514941211471

    # alert = browser.switch_to.alert
    # alert.accept()
    #
    # confirm.dismiss()
    #
    # prompt = browser.switch_to.alert
    # prompt.send_keys("My answer")
    # prompt.accept()

finally:
    sleep(20)
    browser.quit()



