from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class CartPageHelper:

    def __init__(self, wd):
        self.wd = wd

    def get_items_quantity(self):
        shortcuts_num = len(self.wd.find_elements_by_css_selector("li.shortcut"))
        if shortcuts_num == 0:
            items_num = 1
        else:
            items_num = shortcuts_num
        return items_num

    def select_first_item(self):
        if len(self.wd.find_elements_by_css_selector("li.shortcut")) > 0:
            self.wd.find_elements_by_css_selector("li.shortcut")[0].click()

    def remove_first_item(self):
        self.select_first_item()

        table = self.wd.find_element_by_css_selector("div#order_confirmation-wrapper table")

        self.wd.find_elements_by_css_selector("button[name=remove_cart_item]")[0].click()

        wait = WebDriverWait(self.wd, 10)
        wait.until(ec.staleness_of(table))
