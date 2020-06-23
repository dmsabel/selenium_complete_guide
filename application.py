from selenium import webdriver
import os

from helpers.auth import AuthHelper
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener


class MyListener(AbstractEventListener):
    def before_find(self, by, value, driver):
        print(by, value)

    def after_find(self, by, value, driver):
        print(by, value, "found")

    def on_exception(self, exception, driver):
        print(exception)


class Application:

    def __init__(self, browser="chrome"):
        if browser == "chrome":
            self.wd = EventFiringWebDriver(webdriver.Chrome(), MyListener())
        elif browser == "firefox":
            self.wd = EventFiringWebDriver(
                webdriver.Firefox(firefox_binary="C:/Program Files/Mozilla Firefox/firefox.exe"), MyListener())
        elif browser == "ie":
            self.wd = EventFiringWebDriver(webdriver.Ie(), MyListener())
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
        self.auth = AuthHelper(self.wd)
