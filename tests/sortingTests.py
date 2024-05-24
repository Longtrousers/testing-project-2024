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
    def setUp(self):
        param_master = [(
            "https://www.hepsiburada.com/ara?q=bilgisayar"
        ),
            (
            "https://www.hepsiburada.com/ara?q=çanta"
        )]
        self.driver = webdriver.Firefox()
        self.title = "Hepsiburada"

    @parameterized.expand(
        {
            (
                "https://www.hepsiburada.com/ara?q=bilgisayar&siralama=azalanfiyat"
            ),
            (
                "https://www.hepsiburada.com/ara?q=çanta&siralama=azalanfiyat"
            ),
        }
    )
    @unittest.skip("penis")
    def testSortPriceHigh(self, url):
        prices = get_prices(url, self.title, self.driver)
        flag = True
        for i in range(0, len(prices) - 1):
            if prices[i] < prices[i + 1]:
                flag = False
        self.assertTrue(flag)

    @parameterized.expand(
        {
            (
                "https://www.hepsiburada.com/ara?q=bilgisayar&siralama=artanfiyat"
            ),
            (
                "https://www.hepsiburada.com/ara?q=çanta&siralama=artanfiyat"
            ),
        }
    )
    @unittest.skip("penis")
    def testSortPriceLow(self, url):
        prices = get_prices(url, self.title, self.driver)
        flag = True
        for i in range(0, len(prices) - 1):
            if prices[i] > prices[i + 1]:
                flag = False
        self.assertTrue(flag)

    @parameterized.expand(
        {
            (
                "https://www.hepsiburada.com/ara?q=bilgisayar&siralama=yorumsayisi"),
            (
                "https://www.hepsiburada.com/ara?q=çanta&siralama=yorumsayisi"
            ),
        }
    )
    @unittest.skip("penis")
    def testSortReviewsHigh(self, url):
        reviews = get_reviews(url, self.title, self.driver)
        flag = True
        for i in range(0, len(reviews) - 1):
            if reviews[i] < reviews[i + 1]:
                flag = False
        self.assertTrue(flag)

    @parameterized.expand(
        {
            (
                "https://www.hepsiburada.com/ara?q=bilgisayar&siralama=indirimurunler",
            ),
            (
                "https://www.hepsiburada.com/ara?q=çanta&siralama=indirimurunler",
            ),
        }
    )
    @unittest.skip("penis")
    def testSortDiscountsHigh(self, url):
        sales = get_discounts(url, self.title, self.driver)
        flag = True
        for i in range(0, len(sales) - 1):
            if sales[i] < sales[i + 1]:
                flag = False
        self.assertTrue(flag)

    @parameterized.expand(
        {
            (
                "https://www.hepsiburada.com/ara?q=bilgisayar&siralama=degerlendirmepuani",
            ),
            (
                "https://www.hepsiburada.com/ara?q=çanta&siralama=degerlendirmepuani",
            ),
        }
    )
    def testSortRatingsHigh(self, url):
        ratings = get_ratings(url, self.title, self.driver)
        print(ratings)
        flag = True
        for i in range(0, len(ratings) - 1):
            if ratings[i] < ratings[i + 1]:
                flag = False
        self.assertTrue(flag)

    def tearDown(self) -> None:
        return self.driver.close()


if __name__ == "__main__":
    unittest.main()
