from time import sleep
import os
from selenium import webdriver



link = "http://suninjuly.github.io/file_input.html"

browser = webdriver.Chrome()
browser.get(link)
sleep(1)

try:
    form = browser.find_element_by_tag_name('form')

    form.find_element_by_name('firstname').send_keys('First Name')
    form.find_element_by_name('lastname').send_keys('Last Name')
    form.find_element_by_name('email').send_keys('email@email.com')

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла


    form.find_element_by_id('file').send_keys(file_path)

    sleep(1)

    button = form.find_element_by_tag_name('button.btn')
    button.click()

# 28.88258850920861

finally:
    sleep(20)
    browser.quit()



