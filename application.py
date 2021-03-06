from selenium import webdriver
import os

from helpers.auth import AuthHelper
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener

from helpers.cart import CartPageHelper
from helpers.item import ItemPageHelper
from helpers.main import MainPageHelper


class MyListener(AbstractEventListener):
    def before_find(self, by, value, driver):
        print(by, value)

    def after_find(self, by, value, driver):
        print(by, value, "found")

    def on_exception(self, exception, driver):
        print(exception)


class Application:

    def __init__(self, browser="chrome"):
        desired_cap = {"proxy": {"proxyType": "MANUAL", "httpProxy": "localhost:8888"}}

        if browser == "chrome":
            self.wd = EventFiringWebDriver(webdriver.Chrome(desired_capabilities=desired_cap), MyListener())
        elif browser == "firefox":
            self.wd = EventFiringWebDriver(
                webdriver.Firefox(firefox_binary="C:/Program Files/Mozilla Firefox/firefox.exe",
                                  desired_capabilities=desired_cap),
                MyListener())
        elif browser == "ie":
            self.wd = EventFiringWebDriver(webdriver.Ie(desired_capabilities=desired_cap), MyListener())
        elif browser == "remote":
            self.wd = webdriver.Remote("192.168.0.14:4444/wd/hub", desired_capabilities={"browserName": "chrome"})
        elif browser == "cloud":
            # https://automate.browserstack.com/
            browserstack_url = 'https://bsuser71559:r7PWQ2qs5fq7bwqzwzbx@hub-cloud.browserstack.com/wd/hub'

            desired_cap = {
                'os': 'Windows',
                'os_version': '10',
                'browser': 'Chrome',
                'browser_version': '80',
                'name': "bsuser71559's First Test"
            }

            self.wd = webdriver.Remote(
                command_executor=browserstack_url,
                desired_capabilities=desired_cap
            )

        self.wd.implicitly_wait(2)

        self.base_path = os.path.dirname(os.path.abspath(__file__))

        # =========== HELPERS ===========
        self.auth = AuthHelper(self.wd)
        self.main = MainPageHelper(self.wd)
        self.cart = CartPageHelper(self.wd)
        self.item = ItemPageHelper(self.wd)
