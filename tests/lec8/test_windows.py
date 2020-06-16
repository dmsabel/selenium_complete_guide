from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


def test_positive(app):
    class WaitNewWindow:
        def __init__(self, old_windows_list):
            self._old_windows_list = old_windows_list

        def __call__(self, driver):
            windows_list = driver.window_handles
            res = list(set(windows_list) - set(self._old_windows_list))
            if len(res) > 0:
                return res[0]

    app.auth.login()
    app.wd.get("http://localhost/litecart/admin/?app=countries&doc=countries")

    wait = WebDriverWait(app.wd, 10)
    wait.until(ec.presence_of_element_located((By.XPATH, "//h1[text()=' Countries']")))

    app.wd.find_element_by_xpath("//a[text()=' Add New Country']").click()

    wait.until(ec.visibility_of_element_located((By.XPATH, "//h1[text()=' Add New Country']")))
    external_links_list = app.wd.find_elements_by_css_selector("i.fa-external-link")
    list_len = len(external_links_list)

    main_window = app.wd.current_window_handle

    for i in range(list_len):
        old_windows = app.wd.window_handles
        app.wd.find_elements_by_css_selector("i.fa-external-link")[i].click()
        new_window = wait.until(WaitNewWindow(old_windows))
        app.wd.switch_to_window(new_window)
        app.wd.close()
        app.wd.switch_to_window(main_window)

