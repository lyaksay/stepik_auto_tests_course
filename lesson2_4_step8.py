from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    wait = WebDriverWait(browser, 10)
    element = wait.until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    button = browser.find_element(By.ID, 'book')
    button.click()

    x = browser.find_element(By.ID, "input_value")
    x_text = x.text
    y = calc(x_text)

    input_1 = browser.find_element(By.ID, 'answer')
    input_1.send_keys(y)

    button = browser.find_element(By.ID, 'solve')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
