from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


def test_positive(app):
    app.auth.login()

    app.wd.find_element_by_xpath("//span[text()='Catalog']").click()

    wait = WebDriverWait(app.wd, 5)
    wait.until(ec.presence_of_element_located((By.XPATH, "//form[@name='catalog_form']")))
    app.wd.find_element_by_xpath("//form[@name='catalog_form']//a[text()='Rubber Ducks']").click()
    items_num = len(app.wd.find_elements_by_xpath("//*[@class='dataTable']//img/../a"))

    for i in range(items_num):
        app.wd.find_elements_by_xpath("//*[@class='dataTable']//img/../a")[i].click()
        logs = app.wd.get_log("browser")

        if len(logs) > 0:
            print("В логе браузера нет сообщений.")
        else:
            print("Сообщения в логе браузера:")
            for l in logs:
                print(l)

        app.wd.get("http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1")
