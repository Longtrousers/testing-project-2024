from selenium import webdriver
from re import sub
import selenium
import selenium.webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def get_prices(url: str, title: str, driver) -> list[int]:
    driver.get(url)
    assert title in driver.title

    price_divs = driver.find_elements(
        By.XPATH,
        "//div[@class='product-list']//div[@data-test-id='price-current-price']",
    )
    for i in price_divs:
        print(i.text)
    prices = list(
        map(
            lambda x: int(sub("\\D+", "", x.text)),
            price_divs,
        )
    )
    return prices
