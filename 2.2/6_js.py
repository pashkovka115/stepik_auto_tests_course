from time import sleep

from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))



link = "http://suninjuly.github.io/execute_script.html"

browser = webdriver.Chrome()
browser.get(link)
sleep(1)

try:
    result = browser.find_element_by_id('input_value').text
    x = calc(result)

    button = browser.find_element_by_tag_name("button")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button) # скролим для появления элемента
    browser.execute_script("window.scrollBy(0, 100);", button) # скролим для появления элемента

    answer = browser.find_element_by_id('answer')
    answer.send_keys(x)

    robotCheckbox = browser.find_element_by_id('robotCheckbox')
    robotCheckbox.click()

    robotsRule = browser.find_element_by_id('robotsRule')
    robotsRule.click()

    button.click()
# 28.88168139210362

finally:
    sleep(20)
    browser.quit()



