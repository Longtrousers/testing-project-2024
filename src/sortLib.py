from re import sub
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import matplotlib.pyplot as plt
import numpy as np


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


def get_sales(url: str, title: str, driver) -> list[int]:
    driver.get(url)
    assert title in driver.title

    sales_divs = driver.find_elements(
        By.XPATH, "//div[@class='product-list']//div[@data-test-id='price-prev-price-discount']")
    sales = list(map(lambda x: int(sub("\\D+", "", x.text)), sales_divs))
    print(sales)

    return sales


def get_ratings(url: str, title: str, driver) -> tuple[list[int], list[int]]:
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
                ratings.append(float(_.replace("%", "")) / 5)
            else:
                ratings[i // 5] += float(_.replace("%", "")) / 5

    return ratings, get_reviews(url, title, driver)


driver = webdriver.Firefox()
ratings, reviews = get_ratings(
    "https://www.hepsiburada.com/ara?q=bilgisayar&siralama=degerlendirmepuani", "Hepsiburada", driver)
print(ratings)
print(reviews)

total = sum(reviews)
weighted_ratings = [i * reviews[i] / total for i in ratings]

fig, ax = plt.subplots()
ax.plot

# ratings = np.array(ratings)
# reviews = np.array(reviews)
# m, b = np.polyfit(range(0, len(ratings)), ratings, 1)

# fig, ax = plt.subplots()
# ax.scatter(range(0, len(ratings)), ratings)
# ax.plot(range(0, len(ratings)), m*ratings + b)
# plt.show()
driver.close()
