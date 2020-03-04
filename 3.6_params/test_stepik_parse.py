import time
import math

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

# answer = str(math.log(int(time.time())))

links = [
    'https://stepik.org/lesson/236895/step/1',
    'https://stepik.org/lesson/236896/step/1',
    'https://stepik.org/lesson/236897/step/1',
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1'
]


@pytest.mark.parametrize('link', links)
def test_stepik_lesson(link):
    try:
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.get(link)

        textarea = WebDriverWait(driver=driver, timeout=10).until(
            EC.element_to_be_clickable((By.TAG_NAME, 'textarea'))
        )

        # textarea = driver.find_element_by_tag_name('textarea')
        textarea.clear()
        answer = str(math.log(int(time.time())))
        textarea.send_keys(answer)

        button = driver.find_element_by_css_selector('section.attempt-wrapper__body button')
        button.click()

        pre = driver.find_element_by_tag_name('pre').text

        assert pre == 'Correct!', f'строка на странице: {pre}, ожидается: "Correct!", ссылка: {link}'

    finally:
        driver.quit()

































