import pytest
from selenium.webdriver.chrome import webdriver


@pytest.fixture(params=["expected_min_score,  expected_price_limit"])
def open_browser(request):
    return request.param


@pytest.fixture()
def rating():
    expected_min_score = "4"
    return expected_min_score


@pytest.fixture()
def price():
    expected_price_limit = "4000"
    return expected_price_limit
