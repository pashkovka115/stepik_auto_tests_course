from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))



link = "http://suninjuly.github.io/explicit_wait2.html"

browser = webdriver.Chrome()
# говорим WebDriver ждать все элементы в течение 5 секунд
browser.implicitly_wait(5)
browser.get(link)


try:

    # говорим Selenium проверять в течение 14 секунд, пока не появится интересующая цена
    # ждём нужный текст
    WebDriverWait(browser, 14).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )
    # , а потом начинаем искать кнопку
    button = browser.find_element_by_id('book')
    button.click()

    input_value = browser.find_element_by_id('input_value').text
    x = calc(input_value)

    answer = browser.find_element_by_id('answer')
    answer.clear()
    answer.send_keys(x)

    solve = browser.find_element_by_id('solve')
    solve.click()

    alert = browser.switch_to.alert
    print('Ответ:', alert.text)

# 28.96932557245588
except Exception as e:
    print(e)


finally:
    sleep(20)
    browser.quit()


# title_is
# title_contains
# presence_of_element_located
# visibility_of_element_located
# visibility_of
# presence_of_all_elements_located
# text_to_be_present_in_element
# text_to_be_present_in_element_value
# frame_to_be_available_and_switch_to_it
# invisibility_of_element_located
# element_to_be_clickable
# staleness_of
# element_to_be_selected
# element_located_to_be_selected
# element_selection_state_to_be
# element_located_selection_state_to_be
# alert_is_present
