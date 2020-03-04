from time import sleep

from selenium.webdriver.support.ui import Select
from selenium import webdriver


# link = 'http://suninjuly.github.io/selects1.html'
link = 'http://suninjuly.github.io/selects2.html'

browser = webdriver.Chrome()
browser.get(link)
sleep(1)

try:
    num1 = browser.find_element_by_id('num1').text
    num2 = browser.find_element_by_id('num2').text
    print(f'{num1} + {num2} == {int(num1) + int(num2)}')
    my_summ = str(int(num1) + int(num2))


    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(my_summ) # ищем элемент с текстом "Python"

    sleep(2)

    button = browser.find_element_by_css_selector('form button.btn')
    button.click()


# except Exception as e:
#     print(e)

# 28.880317772626352
# 28.88031784842005

finally:
    sleep(20)
    browser.quit()





