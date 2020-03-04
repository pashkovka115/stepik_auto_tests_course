from time import sleep
from selenium import webdriver



link = "http://suninjuly.github.io/wait2.html"

browser = webdriver.Chrome()
# говорим WebDriver ждать все элементы в течение 5 секунд
browser.implicitly_wait(5)
browser.get(link)


try:

    button = browser.find_element_by_id("verify")
    button.click()
    message = browser.find_element_by_id("verify_message")

    assert "successful" in message.text

except Exception as e:
    print(e)


finally:
    sleep(5)
    browser.quit()



