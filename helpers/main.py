import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class MainPageHelper:

    def __init__(self, wd):
        self.wd = wd

    def select_item(self):
        self.wd.get("https://litecart.stqa.ru/ru/")
        self.wd.find_elements_by_css_selector("div#box-most-popular li.product")[0].click()

    def open_cart(self):
        self.wd.find_element_by_xpath("//a[text()='Checkout »']").click()

        wait = WebDriverWait(self.wd, 10)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "div#order_confirmation-wrapper table")))
        time.sleep(1)
