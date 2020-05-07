from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # находим num1
    num1_element = browser.find_element_by_css_selector("#num1")
    num1 = num1_element.text

    # находим num2
    num2_element = browser.find_element_by_css_selector("#num2")
    num2 = num2_element.text

    # считаем сумму
    s = int(num1) + int(num2)
    print(s)

    # передаем значение sum в поле ответа
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(s))  # ищем элемент с sum

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

