import sys
import os
import unittest
from parameterized import parameterized
from selenium import webdriver
# project_path = os.path.abspath(os.path.join('..'))
# if project_path not in sys.path:
#     sys.path.insert(0, project_path)]
sys.path.append(r"C:\\GitHub Repos\\testing-project-2024")
from src.sortLib import get_discounts, get_prices, get_ratings, get_reviews

class TestSorting(unittest.TestCase):
    # Parameters for test are atomized for easier testing.
    # Sorting queries are added in tests.
    param_master = ["bilgisayar", "çanta", "ayakkabı", "telefon", "kalem"]
    #aram_master = ["telefon"]
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.title = "Hepsiburada"

    @parameterized.expand(param_master)
    #@unittest.skip("")
    def testSortPriceHigh(self, item_name):
        url = f"https://www.hepsiburada.com/ara?q={item_name}&siralama=azalanfiyat"
        prices = get_prices(url, self.title, self.driver)
        print(f"{item_name} prices: {prices}")
        flag = True
        for i in range(0, len(prices) - 1):
            if prices[i] < prices[i + 1]:
                flag = False
        self.assertTrue(flag)

    @parameterized.expand(param_master)
    #@unittest.skip("")
    def testSortPriceLow(self, item_name):
        url = f"https://www.hepsiburada.com/ara?q={item_name}&siralama=artanfiyat"
        prices = get_prices(url, self.title, self.driver)
        print(f"{item_name} prices: {prices}")
        flag = True
        for i in range(0, len(prices) - 1):
            if prices[i] > prices[i + 1]:
                flag = False
        self.assertTrue(flag)

    @parameterized.expand(param_master)
    #@unittest.skip("")
    def testSortReviewsHigh(self, item_name):
        url = f"https://www.hepsiburada.com/ara?q={item_name}&siralama=yorumsayisi"
        reviews = get_reviews(url, self.title, self.driver)
        print(f"{item_name} review: {reviews}")
        flag = True
        for i in range(0, len(reviews) - 1):
            if reviews[i] < reviews[i + 1]:
                flag = False
        self.assertTrue(flag)

    @parameterized.expand(param_master)
    #@unittest.skip("")
    def testSortDiscountsHigh(self, item_name):
        url = f"https://www.hepsiburada.com/ara?q={item_name}&siralama=indirimurunler"
        discounts = get_discounts(url, self.title, self.driver)
        print(f"{item_name} discounts: {discounts}")
        flag = True
        for i in range(0, len(discounts) - 1):
            if discounts[i] < discounts[i + 1]:
                flag = False
        self.assertTrue(flag)

    @parameterized.expand(param_master)
    @unittest.skip("")
    def testSortRatingsHigh(self, item_name):
        url = f"https://www.hepsiburada.com/ara?q={item_name}&siralama=degerlendirmepuani"
        ratings = get_ratings(url, self.title, self.driver)
        print(f"{item_name} ratings: {ratings}")
        flag = True
        for i in range(0, len(ratings) - 1):
            if ratings[i] < ratings[i + 1]:
                flag = False
        self.assertTrue(flag)

    def tearDown(self) -> None:
        return self.driver.close()


if __name__ == "__main__":
    unittest.main()
