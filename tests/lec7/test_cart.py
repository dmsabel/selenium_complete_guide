import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


@pytest.mark.parametrize('app', ["cloud"], indirect=True)
def test_positive(app):
    # Добавляем в корзину три товара
    for _ in range(3):
        app.wd.get("https://litecart.stqa.ru/ru/")

        app.wd.find_elements_by_css_selector("div#box-most-popular li.product")[0].click()

        quantity = app.wd.find_element_by_css_selector("span.quantity")
        quantity_text = quantity.text
        app.wd.find_element_by_css_selector("button[name=add_cart_product]").click()
        wait = WebDriverWait(app.wd, 10)
        wait.until_not(lambda d: d.find_element_by_name("span.quantity").text == quantity_text)

    # Нажимаем на ссылку 'Checkout'
    app.wd.find_element_by_xpath("//a[text()='Checkout »']").click()
    shortcuts_num = len(app.wd.find_elements_by_css_selector("li.shortcut"))

    if shortcuts_num == 0:
        items_num = 1
    else:
        items_num = shortcuts_num

    # Ждем загрузку страницы с корзиной
    wait = WebDriverWait(app.wd, 10)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "div#order_confirmation-wrapper table")))
    time.sleep(1)

    # Удаляем все товары из корзины
    for _ in range(items_num):
        if len(app.wd.find_elements_by_css_selector("li.shortcut")) > 0:
            app.wd.find_elements_by_css_selector("li.shortcut")[0].click()

        table = app.wd.find_element_by_css_selector("div#order_confirmation-wrapper table")

        app.wd.find_elements_by_css_selector("button[name=remove_cart_item]")[0].click()

        wait = WebDriverWait(app.wd, 10)
        wait.until(ec.staleness_of(table))
