from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    price = WebDriverWait(browser, 30).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))

    button = browser.find_element_by_css_selector("button#book.btn")
    button.click()

    # calculate y
    x_element = browser.find_element_by_css_selector(".nowrap#input_value")
    x = x_element.text
    y = calc(x)

    # send y to the form
    answer = browser.find_element_by_css_selector("#answer.form-control")
    answer.send_keys(y)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button#solve.btn")
    button.click()

    # print answer
    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert_text)

    # accept alert
    alert = browser.switch_to.alert
    alert.accept()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()
