from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
import unittest



class TestRegister(unittest.TestCase):

    def test_register1(self):
        link = "http://suninjuly.github.io/registration1.html"

        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        form = browser.find_element_by_tag_name('form')
        first_block = form.find_element_by_css_selector('div.first_block')

        first_name = first_block.find_element_by_css_selector('input.first')
        last_name = first_block.find_element_by_css_selector('input.second')
        email = first_block.find_element_by_css_selector('input.third')

        first_name.send_keys('Мой текст для регистрации')
        last_name.send_keys('Мой текст для регистрации')
        email.send_keys('Мой текст для регистрации')

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, 'Зарегестрироваться не удалось.')

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(5)
        # закрываем браузер после всех манипуляций
        browser.quit()


    def test_register2(self):
        link = "http://suninjuly.github.io/registration2.html"

        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        form = browser.find_element_by_tag_name('form')
        first_block = form.find_element_by_css_selector('div.first_block')

        first_name = first_block.find_element_by_css_selector('input.first')
        last_name = first_block.find_element_by_css_selector('input.second')
        email = first_block.find_element_by_css_selector('input.third')

        first_name.send_keys('Мой текст для регистрации')
        last_name.send_keys('Мой текст для регистрации')
        email.send_keys('Мой текст для регистрации')

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, 'Зарегестрироваться не удалось.')

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(5)
        # закрываем браузер после всех манипуляций
        browser.quit()



if __name__ == "__main__":
    unittest.main()


