import pytest
from selenium import webdriver


@pytest.fixture
def wd(request):
    wd = webdriver.Chrome()
    wd.implicitly_wait(2)
    request.addfinalizer(wd.quit)
    return wd


@pytest.fixture
def wd_ff(request):
    wd = webdriver.Firefox(firefox_binary="C:/Program Files/Mozilla Firefox/firefox.exe")
    request.addfinalizer(wd.quit)
    return wd


@pytest.fixture
def wd_ff_esr(request):
    wd = webdriver.Firefox(
        firefox_binary="C:/Program Files/Mozilla Firefox ESR/firefox.exe",
        capabilities={"marionette": False})
    request.addfinalizer(wd.quit)
    return wd


@pytest.fixture
def wd_ff_nightly(request):
    wd = webdriver.Firefox(firefox_binary="C:/Program Files/Firefox Nightly/firefox.exe")
    request.addfinalizer(wd.quit)
    return wd


@pytest.fixture
def wd_ie(request):
    wd = webdriver.Ie()
    request.addfinalizer(wd.quit)
    return wd
