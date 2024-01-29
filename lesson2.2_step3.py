
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код
    num_1 = browser.find_element(By.ID, 'num1')
    num_1_text = num_1.text
    num_2 = browser.find_element(By.ID, 'num2')
    num_2_text = num_2.text
    rslt = int(num_1_text) + int(num_2_text)
    select = Select(browser.find_element(By.TAG_NAME, 'select'))
    select.select_by_value(str(rslt))  # ищем элемент с текстом "Python"

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(8)
    # закрываем браузер после всех манипуляций
    browser.quit()
