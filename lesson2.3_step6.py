
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    windows = browser.window_handles
    browser.switch_to.window(windows[1])

    x = browser.find_element(By.ID, "input_value")
    x_text = x.text
    y = calc(x_text)

    input_1 = browser.find_element(By.ID, 'answer')
    input_1.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(8)
    # закрываем браузер после всех манипуляций
    browser.quit()
