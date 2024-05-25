import unittest
import sys
from selenium import webdriver
from parameterized import parameterized
sys.path.append(r"C:\\Users\\Arfus\\Documents\\GitHub\\testing-project-2024")
import src.filteringLib as filteringLib




class TestHepsiburadaScraping(unittest.TestCase):
    
#----------------------------------------------- BRAND ----------------------------------------------- #
    params = [("https://www.hepsiburada.com/ara?q=bilgisayar&markalar=asus","asus"),
              ("https://www.hepsiburada.com/ara?q=çanta&markalar=mango","mango"),
              ("https://www.hepsiburada.com/ara?q=kalem","zig"),
              ("https://www.hepsiburada.com/ara?q=telefon&markalar=apple","apple"),
              ("https://www.hepsiburada.com/ara?q=bisiklet&markalar=salcano","salcano")]
    
    @parameterized.expand(params)
    def test_product_brands(self,url,brand):
        product_names = filteringLib.get_products(url)

        for product_name in product_names:
            self.assertIn(brand, product_name, f"Bu ürün {brand} markasına ait değil: {product_name}")
            
    
#----------------------------------------------- TYPE ----------------------------------------------- #

    # def test_pencil_type(self):
    #     url = "https://www.hepsiburada.com/ara?q=kalem&filtreler=MainCategory.Id:21037855"
    #     product_names = filteringLib.get_products(url)
    #     for product_name in product_names:
    #         self.assertIn("tükenmez", product_name, f"Bu ürün Tükenmez kalem değildir: {product_name}")
    
#----------------------------------------------- PRICE ----------------------------------------------- #
    # def test_prices_within_range(self):
    #     url = "https://www.hepsiburada.com/ara?q=bilgisayar&filtreler=fiyat:14400-42600"
    #     prices = filteringLib.get_prices(url)
    #     prices_within_range = all(14400 <= price <= 42600 for price in prices)

    #     self.assertTrue(prices_within_range, "Tüm ürünlerin fiyatları istenilen aralıkta değil.")
        
    # def test_rating_filter(self):
    #     url = "https://www.hepsiburada.com/ara?q=bilgisayar&puan=4-max"
    #     driver =  webdriver.Firefox()
    #     ratings = sortLib.get_ratings(url,"Hepsiburada",driver)
    #     print(ratings)
    #     rating_with_in_range = all(4 <= rating <= 5 for rating in ratings)
    #     self.assertTrue(rating_with_in_range, "Tüm ürünlerin fiyatları istenilen aralıkta değil.")

            
if __name__ == "__main__":
    unittest.main()
