import sys

sys.path.append(r"C:\\GitHub Repos\\testing-project-2024")

import unittest
from src.sortLib import get_prices
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
    def testSortPriceDesc(self, url, title):
        prices = get_prices(url, title, self.driver)
        flag = True
        for i in range(0, len(prices) - 1):
            if prices[i] < prices[i + 1]:
                flag = False
        self.assertTrue(flag)

    def tearDown(self) -> None:
        return self.driver.close()


if __name__ == "__main__":
    unittest.main()
