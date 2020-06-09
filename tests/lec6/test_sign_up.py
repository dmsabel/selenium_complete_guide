import random
import string
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def test_positive(app):
    def generate_email():
        symbols = string.ascii_letters + string.digits
        gen_str = "".join([random.choice(symbols) for _ in range(10)])
        return f"Test_{gen_str}@email.com"

    email = generate_email()
    password = "12345"

    # Заходим на главную страницу приложения, кликаем на ссылку создания нового пользователя и заполняем данные
    app.wd.get("http://localhost/litecart/en/")
    app.wd.find_element_by_xpath("//a[text()='New customers click here']").click()

    time.sleep(1)

    app.wd.find_element_by_css_selector("input[name=firstname]").send_keys("Fname")
    app.wd.find_element_by_css_selector("input[name=lastname]").send_keys("Lname")
    app.wd.find_element_by_css_selector("input[name=address1]").send_keys("Address")
    app.wd.find_element_by_css_selector("input[name=postcode]").send_keys("12345")
    app.wd.find_element_by_css_selector("input[name=city]").send_keys("City")
    app.wd.find_element_by_css_selector("input[name=email]").send_keys(email)
    app.wd.find_element_by_css_selector("input[name=phone]").send_keys("12345")
    app.wd.find_element_by_css_selector("input[name=password]").send_keys(password)
    app.wd.find_element_by_css_selector("input[name=confirmed_password]").send_keys(password)
    ActionChains(app.wd).click(app.wd.find_element_by_css_selector("span.select2-selection"))\
        .send_keys("United States").send_keys(Keys.ENTER).perform()

    app.wd.find_element_by_css_selector("button[name=create_account]").click()

    time.sleep(1)

    # Приложение почему-то не дает выбрать зону, пока не попытаешься создать аккаунт (элемент не активный),
    # поэтому приходится заполнять пароль и кликать на кнопку создания два раза
    app.wd.find_element_by_css_selector("input[name=password]").send_keys(password)
    app.wd.find_element_by_css_selector("input[name=confirmed_password]").send_keys(password)
    select_zone = Select(app.wd.find_element_by_css_selector("select[name=zone_code]"))
    select_zone.select_by_visible_text("Arizona")

    app.wd.find_element_by_css_selector("button[name=create_account]").click()

    # Ждем, пока не появится сообщение об успешном создании аккаунта, после чего разлогиниваемся
    wait = WebDriverWait(app.wd, 10)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "div.notice.success")))
    app.wd.find_element_by_xpath("//a[text()='Logout']").click()

    # Заходим в приложение под только что созданным пользователем
    wait = WebDriverWait(app.wd, 10)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "input[name=email]")))

    app.wd.find_element_by_css_selector("input[name=email]").send_keys(email)
    app.wd.find_element_by_css_selector("input[name=password]").send_keys(password)
    app.wd.find_element_by_css_selector("button[name=login]").click()

    # Ждем, пока не появится сообщение об успешной авторизации, после чего разлогиниваемся
    wait = WebDriverWait(app.wd, 10)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "div.notice.success")))
    app.wd.find_element_by_xpath("//a[text()='Logout']").click()
