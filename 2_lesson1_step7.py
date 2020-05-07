from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # находим x и считаем для него calc(x)
    x_element = browser.find_element_by_css_selector("img#treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)

    # передаем значение calc(x) в поле ответа
    answer = browser.find_element_by_css_selector("#answer")
    answer.send_keys(y)

    # ставим чекбокс
    option1 = browser.find_element_by_css_selector("#robotCheckbox")
    option1.click()

    #ставим радиобаттон
    option2 = browser.find_element_by_css_selector("#robotsRule")
    option2.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

