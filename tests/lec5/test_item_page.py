import re

import pytest


@pytest.mark.parametrize('app', ["chrome", "firefox", "ie"], indirect=True)
def test_positive(app):
    def rgba_str_to_dict(rgba_str):
        re_res = re.search(r"rgba?\((\d+), (\d+), (\d+)(, \d+)?\)", rgba_str)
        return {
            "red": re_res[1],
            "green": re_res[2],
            "blue": re_res[3]
        }

    # Заходим на главную страицу (mp = main page), получаем данные о товаре
    app.wd.get("http://localhost/litecart/en/")
    item = app.wd.find_element_by_css_selector("div#box-campaigns a.link")

    name_mp = item.find_element_by_css_selector("div.name").text

    price_reg_mp = item.find_element_by_css_selector("s.regular-price")
    price_reg_text_mp = price_reg_mp.text
    price_reg_color_mp = rgba_str_to_dict(price_reg_mp.value_of_css_property("color"))
    price_reg_decor_mp = price_reg_mp.value_of_css_property("text-decoration")
    price_reg_font_weight_mp = price_reg_mp.value_of_css_property("font-weight")
    price_reg_size_mp = price_reg_mp.size

    price_cam_mp = item.find_element_by_css_selector("strong.campaign-price")
    price_cam_text_mp = price_cam_mp.text
    price_cam_color_mp = rgba_str_to_dict(price_cam_mp.value_of_css_property("color"))
    price_cam_decor_mp = price_cam_mp.value_of_css_property("text-decoration")
    price_cam_font_weight_mp = price_cam_mp.value_of_css_property("font-weight")
    price_cam_size_mp = price_cam_mp.size

    # Проверяем стили, шрифты и размеры цен
    assert price_reg_color_mp["red"] == price_reg_color_mp["green"] == price_reg_color_mp["blue"], \
        "Цвет обычной цены не серый!"
    assert price_cam_color_mp["green"] == "0" and price_cam_color_mp["blue"] == "0", "Цвет акционной цены не красный!"
    assert "line-through" in price_reg_decor_mp, "Обычная цена должна быть перечеркнута!"
    assert not ("line-through" in price_cam_decor_mp), "Акционная цена не должна быть перечеркнута!"
    assert int(price_reg_font_weight_mp) in range(100, 501), "Шрифт обычной цены не должен быть жирным!"
    assert int(price_cam_font_weight_mp) in range(600, 901), "Шрифт акционной цены должен быть жирным!"
    assert (price_reg_size_mp["height"] < price_cam_size_mp["height"] and
            price_reg_size_mp["width"] < price_cam_size_mp["width"]), "Акционная цена должна быть больше обычной!"

    # Переходим на страницу товара (ip = item page), получаем данные о товаре
    item.click()

    name_ip = app.wd.find_element_by_css_selector("div#box-product .title").text

    price_reg_ip = app.wd.find_element_by_css_selector("s.regular-price")
    price_reg_color_ip = rgba_str_to_dict(price_reg_ip.value_of_css_property("color"))
    price_reg_text_ip = app.wd.find_element_by_css_selector("s.regular-price").text
    price_reg_decor_ip = \
        app.wd.find_element_by_css_selector("s.regular-price").value_of_css_property("text-decoration")
    price_reg_font_weight_ip = \
        app.wd.find_element_by_css_selector("s.regular-price").value_of_css_property("font-weight")
    price_reg_size_ip = app.wd.find_element_by_css_selector("s.regular-price").size

    price_cam_ip = app.wd.find_element_by_css_selector("strong.campaign-price")
    price_cam_color_ip = rgba_str_to_dict(price_cam_ip.value_of_css_property("color"))
    price_cam_text_ip = app.wd.find_element_by_css_selector("strong.campaign-price").text
    price_cam_decor_ip = \
        app.wd.find_element_by_css_selector("strong.campaign-price").value_of_css_property("text-decoration")
    price_cam_font_weight_ip = \
        app.wd.find_element_by_css_selector("strong.campaign-price").value_of_css_property("font-weight")
    price_cam_size_ip = app.wd.find_element_by_css_selector("strong.campaign-price").size

    # Проверяем стили, шрифты и размеры цен
    assert price_reg_color_ip["red"] == price_reg_color_ip["green"] == price_reg_color_ip["blue"], \
        "Цвет обычной цены не серый!"
    assert price_cam_color_ip["green"] == "0" and price_cam_color_ip["blue"] == "0", "Цвет акционной цены не красный!"
    assert "line-through" in price_reg_decor_ip, "Обычная цена должна быть перечеркнута!"
    assert not ("line-through" in price_cam_decor_ip), "Акционная цена не должна быть перечеркнута!"
    assert int(price_reg_font_weight_ip) in range(100, 501), "Шрифт обычной цены не должен быть жирным!"
    assert int(price_cam_font_weight_ip) in range(600, 901), "Шрифт акционной цены должен быть жирным!"
    assert (price_reg_size_ip["height"] < price_cam_size_ip["height"] and
            price_reg_size_ip["width"] < price_cam_size_ip["width"]), "Акционная цена должна быть больше обычной!"

    # Проверяем, что данные на страницах совпадают
    assert name_mp == name_ip, "Название товара на главной странице и странице товара не совпадают!"
    assert price_reg_text_mp == price_reg_text_ip, "Обычная цена на главной странице и странице товара не совпадают!"
    assert price_cam_text_mp == price_cam_text_ip, "Акционная цена на главной странице и странице товара не совпадают!"
