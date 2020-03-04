from time import sleep

from selenium.webdriver.support.ui import Select
from selenium import webdriver


# link = 'http://suninjuly.github.io/selects2.html'

browser = webdriver.Chrome()
# browser.get(link)
sleep(1)

try:
    browser.execute_script("document.title='Script executing'; alert('Robots at work');")

finally:
    sleep(5)
    browser.quit()





