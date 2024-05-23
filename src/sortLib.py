from re import sub
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def get_prices(url: str, title: str, driver) -> list[int]:
    driver.get(url)
    assert title in driver.title

    price_divs = driver.find_elements(
        By.XPATH, "//div[@class='product-list']//div[@data-test-id='price-current-price']")
    prices = list(map(lambda x: int(sub("\\D+", "", x.text)), price_divs))
    return prices


def get_reviews(url: str, title: str, driver) -> list[int]:
    driver.get(url)
    assert title in driver.title

    review_divs = driver.find_elements(
        By.XPATH, "//div[@class='product-list']//div[@data-test-id='review']//div[2]")
    reviews = list(map(lambda x: int(sub("\\D+", "", x.text)), review_divs))
    return reviews


def get_discounts(url: str, title: str, driver) -> list[int]:
    driver.get(url)
    assert title in driver.title

    sales_divs = driver.find_elements(
        By.XPATH, "//div[@class='product-list']//div[@data-test-id='price-prev-price-discount']")
    sales = list(map(lambda x: int(sub("\\D+", "", x.text)), sales_divs))
    print(sales)

    return sales


def get_ratings(url: str, title: str, driver) -> list[int]:
    driver.get(url)
    assert title in driver.title

    # Each rating has 5 uls which all have one div
    ratings_divs = driver.find_elements(
        By.XPATH, "//div[@class='product-list']//ul[@data-baseweb='star-rating']/li/div")
    ratings = []

    for i in range(0, len(ratings_divs)):  # Compact those divs into ratings
        _ = ratings_divs[i].get_attribute("width")
        if _ is not None:
            if len(ratings) <= i // 5:
                ratings.append(float(_.replace("%", "")) / 100)
            else:
                ratings[i // 5] += float(_.replace("%", "")) / 100

    return ratings
