import unittest
import sys
sys.path.append(r"C:\\Users\\Arfus\\Documents\\GitHub\\testing-project-2024")
import src.filteringLib as filteringLib



class TestHepsiburadaScraping(unittest.TestCase):
    def test_asus_products(self):
        url = "https://www.hepsiburada.com/ara?q=bilgisayar&markalar=asus"
        product_names = filteringLib.get_asus_products(url)

        for product_name in product_names:
            self.assertIn("asus", product_name, f"Bu ürün Asus markasına ait değil: {product_name}")
    
    def test_prices_within_range(self):
        url = "https://www.hepsiburada.com/ara?q=bilgisayar&filtreler=fiyat:14400-42600"
        prices = filteringLib.get_prices(url)
        print(prices)
        prices_within_range = all(14400 <= price <= 42600 for price in prices)

        self.assertTrue(prices_within_range, "Tüm ürünlerin fiyatları istenilen aralıkta değil.")

            

if __name__ == "__main__":
    unittest.main()
