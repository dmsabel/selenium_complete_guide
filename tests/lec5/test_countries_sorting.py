def test_positive(app):
    app.auth.login()

    app.wd.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    country_rows_list = app.wd.find_elements_by_css_selector("form[name=countries_form] tr.row")

    country_list = []
    country_with_zones_list = []

    # Получаем названия стран (отдельно получаем названия стран, содержащих больше одной зоны)
    for country_row in country_rows_list:
        zones = country_row.find_element_by_css_selector("td:nth-of-type(6)").text
        country_name = country_row.find_element_by_css_selector("td:nth-of-type(5) a").text
        country_list.append(country_name)
        if zones != "0":
            country_with_zones_list.append(country_name)

    # Проверяем сортировку списка
    country_list_exp = sorted(country_list)
    assert country_list == country_list_exp, "Список стран отсортирован некорректно!"

    # Переходим на страницы стран, содержащих более одной зоны, и получаем названия зон
    for country_name in country_with_zones_list:
        app.wd.find_element_by_xpath(f"//form[@name='countries_form']//a[text() = '{country_name}']").click()

        zone_el_list = app.wd.find_elements_by_css_selector("table.dataTable td:nth-of-type(3)")[:-1]
        zone_list = []

        for zone_el in zone_el_list:
            zone_list.append(zone_el.text)

        app.wd.get("http://localhost/litecart/admin/?app=countries&doc=countries")
        
        # Проверяем сортировку списка зон для каждой страны
        zone_list_exp = sorted(zone_list)
        assert zone_list == zone_list_exp, f"Список зон для страны {country_name} отсортирован некорректно!"
