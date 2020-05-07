from selenium import webdriver
import time
import math


def calc(x):
    return str( math.log( abs( 12 * math.sin( int( x ) ) ) ) )


try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # находим x и считаем для него calc(x)
    x_element = browser.find_element_by_css_selector(".nowrap#input_value")
    x = x_element.text
    y = calc(x)

    # передаем значение calc(x) в поле ответа
    answer = browser.find_element_by_css_selector("#answer.form-control")
    answer.send_keys(y)

    # ставим чекбокс
    option1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
    option1.click()

    #ставим радиобаттон
    option2 = browser.find_element_by_css_selector("[for='robotsRule']")
    option2.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

