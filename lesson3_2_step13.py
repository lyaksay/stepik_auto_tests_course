from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class TestRegistration(unittest.TestCase):
    def test_registration_1(self):
        try:
            link = "https://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.get(link)

            # Ваш код, который заполняет обязательные поля
            input1 = browser.find_element(By.CSS_SELECTOR, '.first_block > .first_class > .first')
            input1.send_keys("Ivan")
            input2 = browser.find_element(By.CSS_SELECTOR, '.first_block > .second_class > .second')
            input2.send_keys("Petrov")
            input3 = browser.find_element(By.CSS_SELECTOR, '.first_block > .third_class > .third')
            input3.send_keys("Smolensk")

            # Отправляем заполненную форму
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            time.sleep(8)
            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            assert "Congratulations! You have successfully registered!" == welcome_text
            self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Registration "
                                                                                                 "message does not "
                                                                                                 "match")

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(10)
            # закрываем браузер после всех манипуляций
            browser.quit()

    def test_registration_2(self):
        try:
            link = "https://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.get(link)

            # Ваш код, который заполняет обязательные поля
            input1 = browser.find_element(By.CSS_SELECTOR, '.first_block > .first_class > .first')
            input1.send_keys("Ivan")
            input2 = browser.find_element(By.CSS_SELECTOR, '.first_block > .second_class > .second')
            input2.send_keys("Petrov")
            input3 = browser.find_element(By.CSS_SELECTOR, '.first_block > .third_class > .third')
            input3.send_keys("Smolensk")

            # Отправляем заполненную форму
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            time.sleep(8)
            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            # assert "Congratulations! You have successfully registered!" == welcome_text
            self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Registration "
                                                                                                 "message does not "
                                                                                                 "match")

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(10)
            # закрываем браузер после всех манипуляций
            browser.quit()


if __name__ == "__main__":
    unittest.main()
