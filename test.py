import pytest
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()


@allure.severity(allure.severity_level.NORMAL)
def test_open_browser(open_browser):
    driver.get("https://www.amazon.com/")
    driver.implicitly_wait(10)
    driver.find_element(By.ID, "nav-hamburger-menu").click()
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, "//div[@id='hmenu-content']/ul/li[10]/a/div").click()
    driver.implicitly_wait(10)
    driver.find_element(By.LINK_TEXT, "Beading & Jewelry Making").click()
    driver.find_element(By.XPATH, "//li[@id='n/12896151']/span/a/span").click()
    driver.implicitly_wait(10)
    driver.find_element(By.ID, "a-autoid-0-announce").click()
    driver.implicitly_wait(10)
    driver.find_element(By.ID, "s-result-sort-select_2").click()
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH,
                        "//div[@id='search']/div/div/div/span/div/div[4]/div/div/div/div/div[2]/div/h2/a/span").click()


@allure.severity(allure.severity_level.NORMAL)
def test_simple_customer_review(rating):
    expected_min_score = "4"
    review_score = driver.find_element(By.ID, "acrCustomerReviewText")
    review_score = str(review_score)
    assert review_score >= expected_min_score


@allure.severity(allure.severity_level.NORMAL)
def test_price(price):
    expected_price_limit = "4000"
    price = driver.find_element(By.ID, "corePriceDisplay_desktop_feature_div")
    price = str(price)

    if price < expected_price_limit:
        assert True
    else:
        allure.attach(driver.get_screenshot_as_png(), name="amazonReport",
                      attachment_type=AttachmentType.PNG)
        assert False


driver.close()
# try:
# assert price < expected_price_limit
# except NoSuchElementException:
# assert False
# except ValueError:
# assert False
