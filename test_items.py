import time

from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_check(browser):
    browser.get(link)
    btn = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert btn, 'Cелектор кнопки не найден'
    print(btn)
    time.sleep(30)
