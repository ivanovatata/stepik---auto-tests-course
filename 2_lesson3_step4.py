from selenium import webdriver
import time
import math


def calc(x):
    return str( math.log( abs( 12 * math.sin( int( x ) ) ) ) )

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # press button
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # accept alert
    alert = browser.switch_to.alert
    alert.accept()

    # calculate y
    x_element = browser.find_element_by_css_selector(".nowrap#input_value")
    x = x_element.text
    y = calc(x)

    # send y to the form
    answer = browser.find_element_by_css_selector("#answer.form-control")
    answer.send_keys(y)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
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
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()