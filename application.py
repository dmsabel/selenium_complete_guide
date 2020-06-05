from selenium import webdriver

from helpers.auth import AuthHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(2)

        self.auth = AuthHelper(self.wd)