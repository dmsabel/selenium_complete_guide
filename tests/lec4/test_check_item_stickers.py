def test_positive(wd_ch):
    wd_ch.get("http://localhost/litecart/")

    li_list = wd_ch.find_elements_by_css_selector("li.product")

    for li in li_list:
        assert len(li.find_elements_by_css_selector(".sticker")) == 1
