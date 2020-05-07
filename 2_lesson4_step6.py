from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/cats.html")

    browser.find_element_by_id("button")

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()