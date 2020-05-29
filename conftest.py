import pytest
from selenium import webdriver


@pytest.fixture
def wd_ch(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


@pytest.fixture
def wd_ff(request):
    wd = webdriver.Firefox()
    request.addfinalizer(wd.quit)
    return wd


@pytest.fixture
def wd_ie(request):
    wd = webdriver.Ie()
    request.addfinalizer(wd.quit)
    return wd
