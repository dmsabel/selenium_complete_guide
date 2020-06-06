import time


def test_positive(app):
    app.auth.login()

    # Переходим на страницу геозон
    app.wd.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")
    county_elem_list = app.wd.find_elements_by_css_selector("form[name=geo_zones_form] td:nth-of-type(3) a")

    # Получаем список стран на странице с геозонами
    country_names = []
    for c in county_elem_list:
        country_names.append(c.text)

    # Для каждой страны получаем список геозон и проверяем его сортировку
    for country_name in country_names:
        time.sleep(2)

        app.wd.find_element_by_xpath(f"//form[@name='geo_zones_form']//a[text()='{country_name}']").click()

        zone_dropdown_list = app.wd.find_elements_by_css_selector("table#table-zones select[name*=zone_code]")
        zone_list = []
        for dropdown in zone_dropdown_list:
            zone = dropdown.find_element_by_css_selector("option[selected]").text
            zone_list.append(zone)

        zone_list_exp = sorted(zone_list)
        assert zone_list == zone_list_exp, "Список геозон отсортирован некорректно!"

        app.wd.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")
