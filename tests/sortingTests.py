import sys

sys.path.append(r"C:\\GitHub Repos\\testing-project-2024")

import unittest
from src.sortLib import get_prices, get_reviews, get_sales
from selenium import webdriver
from parameterized import parameterized


class TestSorting(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    @parameterized.expand(
        {
            (
                "https://www.hepsiburada.com/ara?q=bilgisayar&siralama=azalanfiyat",
                "Hepsiburada",
            ),
            (
                "https://www.hepsiburada.com/ara?q=çanta&siralama=azalanfiyat",
                "Hepsiburada",
            ),
        }
    )
    @unittest.skip("penis")
    def testSortHigh(self, url, title):
        prices = get_prices(url, title, self.driver)
        flag = True
        for i in range(0, len(prices) - 1):
            if prices[i] < prices[i + 1]:
                flag = False
        self.assertTrue(flag)

    @parameterized.expand(
        {
            (
                "https://www.hepsiburada.com/ara?q=bilgisayar&siralama=artanfiyat",
                "Hepsiburada",
            ),
            (
                "https://www.hepsiburada.com/ara?q=çanta&siralama=artanfiyat",
                "Hepsiburada",
            ),
        }
    )
    @unittest.skip("penis")
    def testSortLow(self, url, title):
        prices = get_prices(url, title, self.driver)
        flag = True
        for i in range(0, len(prices) - 1):
            if prices[i] > prices[i + 1]:
                flag = False
        self.assertTrue(flag)

    @parameterized.expand(
        {
            (
                "https://www.hepsiburada.com/ara?q=bilgisayar&siralama=yorumsayisi",
                "Hepsiburada",
            ),
            (
                "https://www.hepsiburada.com/ara?q=çanta&siralama=yorumsayisi",
                "Hepsiburada",
            ),
        }
    )
    @unittest.skip("penis")
    def testSortReviewsHigh(self, url, title):
        reviews = get_reviews(url, title, self.driver)
        flag = True
        for i in range(0, len(reviews) - 1):
            if reviews[i] < reviews[i + 1]:
                flag = False
        self.assertTrue(flag)

    @parameterized.expand(
        {
            (
                "https://www.hepsiburada.com/ara?q=bilgisayar&siralama=indirimurunler",
                "Hepsiburada",
            ),
            (
                "https://www.hepsiburada.com/ara?q=çanta&siralama=indirimurunler",
                "Hepsiburada",
            ),
        }
    )
    @unittest.skip("penis")
    def testSortSalesHigh(self, url, title):
        sales = get_sales(url, title, self.driver)
        flag = True
        for i in range(0, len(sales) - 1):
            if sales[i] < sales[i + 1]:
                flag = False
        self.assertTrue(flag)

    def tearDown(self) -> None:
        return self.driver.close()


if __name__ == "__main__":
    unittest.main()
