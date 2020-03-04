from time import sleep

from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

driver = webdriver.Chrome()
driver.get('http://suninjuly.github.io/get_attribute.html')
sleep(2)


try:
    img = driver.find_element_by_id('treasure')
    x = img.get_attribute('valuex')
    result = calc(x)

    answer = driver.find_element_by_id('answer')
    answer.clear()
    answer.send_keys(result)

    robotCheckbox = driver.find_element_by_id('robotCheckbox')
    robotCheckbox_checked = robotCheckbox.get_attribute('checked')
    if not robotCheckbox_checked:
        robotCheckbox.click()

    robotsRule = driver.find_element_by_id('robotsRule')
    robotsRule_checked = robotsRule.get_attribute('checked')
    if not robotsRule_checked:
        robotsRule.click()

    button = driver.find_element_by_css_selector('form button')
    button_disabled = button.get_attribute('disabled')
    if not button_disabled:
        button.click()


#

except Exception as e:
    print(e)
finally:
    sleep(30)
    driver.quit()

