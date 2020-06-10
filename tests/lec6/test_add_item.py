import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def test_positive(app):
    def check_checkbox(xpath_locator):
        if not app.wd.find_element_by_xpath(xpath_locator).is_selected():
            app.wd.find_element_by_xpath(xpath_locator).click()

    item_name = "Yellow submarine duck"

    app.auth.login()
    wait = WebDriverWait(app.wd, 10)
    time.sleep(1)

    wait.until(ec.element_to_be_clickable((By.XPATH, "//span[text()='Catalog']")))
    app.wd.find_element_by_xpath("//span[text()='Catalog']").click()

    wait.until(ec.element_to_be_clickable((By.XPATH, "//a[text()=' Add New Product']")))
    app.wd.find_element_by_xpath("//a[text()=' Add New Product']").click()

    wait.until(ec.visibility_of_element_located((By.XPATH, "//h1[text()=' Add New Product']")))

    # Заполняем данные на вкладке General
    app.wd.find_element_by_xpath("//strong[text()='Status']/../label[text()=' Enabled']/input").click()
    app.wd.find_element_by_xpath("//strong[text()='Name']/..//input").send_keys(item_name)
    app.wd.find_element_by_xpath("//strong[text()='Code']/..//input").send_keys("12345")
    check_checkbox("//input[@data-name='Rubber Ducks']")
    check_checkbox("//td[text()='Unisex']/../td/input")
    app.wd.find_element_by_css_selector("input[name=quantity]").send_keys(34)
    select_status = Select(app.wd.find_element_by_css_selector("select[name=sold_out_status_id]"))
    select_status.select_by_visible_text("Temporary sold out")
    app.wd.find_element_by_css_selector("input[name='new_images[]']").send_keys(f"{app.base_path}/files/item_pic.jpg")
    app.wd.find_element_by_css_selector("input[name=date_valid_from]").send_keys("31.12.2019")
    app.wd.find_element_by_css_selector("input[name=date_valid_to]").send_keys("31.12.2022")

    # Заполняем данные на вкладке Information
    app.wd.find_element_by_xpath("//a[text()='Information']").click()
    time.sleep(1)

    select_manufacturer = Select(app.wd.find_element_by_css_selector("select[name=manufacturer_id]"))
    select_manufacturer.select_by_visible_text("ACME Corp.")
    app.wd.find_element_by_css_selector("input[name=keywords]").send_keys("Duck")
    app.wd.find_element_by_css_selector("input[name='short_description[en]']").send_keys("Short description for item")
    app.wd.find_element_by_css_selector("div.trumbowyg-editor").send_keys("This is a description for item.")
    app.wd.find_element_by_css_selector("input[name='head_title[en]']").send_keys("Yellow submarine duck")
    app.wd.find_element_by_css_selector("input[name='meta_description[en]']").send_keys("Yellow submarine duck")

    # Заполняем данные на вкладке Prices
    app.wd.find_element_by_xpath("//a[text()='Prices']").click()
    time.sleep(1)

    app.wd.find_element_by_css_selector("input[name=purchase_price]").send_keys("12,34")
    select_currency = Select(app.wd.find_element_by_css_selector("select[name=purchase_price_currency_code]"))
    select_currency.select_by_visible_text("Euros")
    app.wd.find_element_by_css_selector("input[name='prices[USD]']").send_keys("13.45")
    app.wd.find_element_by_css_selector("input[name='prices[EUR]']").send_keys("12.34")

    # Кликаем на кнопку "Save"
    app.wd.find_element_by_css_selector("button[name=save]").click()
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "div.notice.success")))

    res = app.wd.find_elements_by_xpath(f"//table[@class='dataTable']//a[text()='{item_name}']")
    assert len(res) == 1, "Товар не был добавлен!"
