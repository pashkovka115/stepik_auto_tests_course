from time import sleep
import os
from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))



link = "http://suninjuly.github.io/execute_script.html"

browser = webdriver.Chrome()
browser.get(link)
sleep(1)

try:
    element = browser.find_element_by_css_selector('[type="file"]')

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    element.send_keys(file_path)

finally:
    sleep(20)
    browser.quit()



