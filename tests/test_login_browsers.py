def test_login_chrome(wd_ch):
    wd_ch.get("http://localhost/litecart/admin/")
    wd_ch.find_element_by_name("username").send_keys("admin")
    wd_ch.find_element_by_name("password").send_keys("admin")
    wd_ch.find_element_by_name("login").click()


def test_login_firefox(wd_ff):
    wd_ff.get("http://localhost/litecart/admin/")
    wd_ff.find_element_by_name("username").send_keys("admin")
    wd_ff.find_element_by_name("password").send_keys("admin")
    wd_ff.find_element_by_name("login").click()


def test_login_firefox_nightly(wd_ff_nightly):
    wd_ff_nightly.get("http://localhost/litecart/admin/")
    wd_ff_nightly.find_element_by_name("username").send_keys("admin")
    wd_ff_nightly.find_element_by_name("password").send_keys("admin")
    wd_ff_nightly.find_element_by_name("login").click()


def test_login_ie(wd_ie):
    wd_ie.get("http://localhost/litecart/admin/")
    wd_ie.find_element_by_name("username").send_keys("admin")
    wd_ie.find_element_by_name("password").send_keys("admin")
    wd_ie.find_element_by_name("login").click()
