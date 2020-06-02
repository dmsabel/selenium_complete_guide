import time


def test_positive(wd_ch):
    def is_element_present(locator):
        return len(wd_ch.find_elements_by_css_selector(locator)) > 0

    def click(css_locator):
        wd_ch.find_element_by_css_selector(css_locator).click()
        time.sleep(1)

    # Авторизация
    wd_ch.get("http://localhost/litecart/admin/")
    wd_ch.find_element_by_name("username").send_keys("admin")
    wd_ch.find_element_by_name("password").send_keys("admin")
    click("[name = login]")

    # Находим и кликаем по всем элементам меню
    li_list = wd_ch.find_elements_by_css_selector("ul#box-apps-menu li#app-")

    i = 1
    for _ in li_list:
        loc_li = f"li#app-:nth-child({i})"
        click(loc_li)

        # Если элемент меню содержит подэлементы, проходим по ним
        loc_ul = f"{loc_li} ul.docs"
        if is_element_present(loc_ul):
            j = 1
            li_nested_list = wd_ch.find_elements_by_css_selector(f"{loc_ul} li")

            for _ in li_nested_list:
                loc_li_nested = f"{loc_ul} li:nth-child({j})"
                click(loc_li_nested)

                assert is_element_present("h1")
                j += 1
        assert is_element_present("h1")
        i += 1
