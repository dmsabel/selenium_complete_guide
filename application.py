from selenium import webdriver

from helpers.auth import AuthHelper


class Application:

    def __init__(self, browser="chrome"):
        if browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "firefox":
            self.wd = webdriver.Firefox(firefox_binary="C:/Program Files/Mozilla Firefox/firefox.exe")
        elif browser == "ie":
            self.wd = webdriver.Ie()

        self.wd.implicitly_wait(2)

        self.auth = AuthHelper(self.wd)
