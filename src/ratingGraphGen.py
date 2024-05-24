from re import sub
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import matplotlib.pyplot as plt
import numpy as np
sys.path.append(r"C:\\GitHub Repos\\testing-project-2024")
from src.sortLib import get_reviews, get_ratings


def get_ratings2(url: str, title: str, driver) -> tuple[list[int], list[int]]:
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
ratings, reviews = get_ratings2(
    "https://www.hepsiburada.com/ara?q=bilgisayar&siralama=degerlendirmepuani", "Hepsiburada", driver)
driver.close()
print(ratings)
print(reviews)

total = sum(reviews)
weighted_ratings = [ratings[i] * reviews[i] /
                    total for i in range(0, len(ratings))]
print(weighted_ratings)
reviews = list(map(lambda x: x / 10, reviews))

fig, ax = plt.subplots()
ax.plot(weighted_ratings, label="weighted")
ax.plot(ratings, label="ratings")
ax.plot(reviews, label="reviews")
lgd = ax.legend(loc="upper right")
plt.show()
ratings = np.array(ratings)
reviews = np.array(reviews)
m, b = np.polyfit(range(0, len(ratings)), ratings, 1)

fig, ax = plt.subplots()
ax.scatter(range(0, len(ratings)), ratings)
ax.plot(range(0, len(ratings)), m*ratings + b)
plt.show()
