from parameterized import parameterized
from selenium import webdriver
from src.sortLib import get_prices, get_reviews, get_discounts
import unittest
import sys

sys.path.append(r"C:\\GitHub Repos\\testing-project-2024")


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

    def tearDown(self) -> None:
        return self.driver.close()


if __name__ == "__main__":
    unittest.main()
