from time import sleep

from selenium import webdriver

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
sleep(2)

try:
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button) # скролим для появления элемента
    # browser.execute_script("window.scrollBy(0, 100);") # Эта команда проскроллит страницу на 100 пикселей вниз
    button.click()
    assert True

finally:
    sleep(3)
    browser.quit()



