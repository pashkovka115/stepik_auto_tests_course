from time import sleep
from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))



link = "http://suninjuly.github.io/redirect_accept.html"

browser = webdriver.Chrome()
browser.get(link)
sleep(1)

try:
    browser.find_element_by_tag_name('button').click()

    first_window = browser.window_handles[0]
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    sleep(1)
    input_value = browser.find_element_by_id('input_value').text
    answer = browser.find_element_by_id('answer')

    answer.send_keys(calc(input_value))

    browser.find_element_by_tag_name('button').click()
    sleep(1)
    alert = browser.switch_to.alert
    answer_num = alert.text

    print('Ответ:', answer_num)

except Exception as e:
    print(e)


finally:
    sleep(20)
    browser.quit()



