from selenium.webdriver.support.wait import WebDriverWait


class ItemPageHelper:

    def __init__(self, wd):
        self.wd = wd

    def add_item_to_cart(self):
        quantity = self.wd.find_element_by_css_selector("span.quantity").text
        self.wd.find_element_by_css_selector("button[name=add_cart_product]").click()
        wait = WebDriverWait(self.wd, 10)
        wait.until_not(lambda d: d.find_element_by_name("span.quantity").text == quantity)
