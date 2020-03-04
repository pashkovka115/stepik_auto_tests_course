from time import sleep

from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))



browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/math.html')
sleep(2)

try:
    x = browser.find_element_by_id('input_value').text
    result = calc(x)

    answer = browser.find_element_by_id('answer')
    answer.send_keys(result)

    checkbox = browser.find_element_by_id('robotCheckbox')
    checkbox_checked = checkbox.get_attribute('checked')
    if not checkbox_checked:
        checkbox.click()

    robots_rule = browser.find_element_by_id('robotsRule')
    robots_rule_checked = robots_rule.get_attribute('checked')
    if not robots_rule_checked:
        robots_rule.click()

    sleep(3)

    button = browser.find_element_by_tag_name('button')
    button.click()
except Exception as e:
    print(e)

finally:
    browser.quit()




