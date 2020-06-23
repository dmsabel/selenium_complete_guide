import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class AuthHelper:

    def __init__(self, wd):
        self.wd = wd

    def login(self):
        self.wd.get("http://localhost/litecart/admin/")
        self.wd.find_element_by_name("username").send_keys("admin")
        self.wd.find_element_by_name("password").send_keys("admin")
        self.wd.find_element_by_name("login").click()

        time.sleep(1)

        wait = WebDriverWait(self.wd, 10)
        wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, "div.logotype")))
