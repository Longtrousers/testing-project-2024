import unittest
import sys
from selenium import webdriver
from parameterized import parameterized
sys.path.append(r"C:\\Users\\Arfus\\Documents\\GitHub\\testing-project-2024")
import src.filteringLib as filteringLib




class TestHepsiburadaScraping(unittest.TestCase):
    
#----------------------------------------------- BRAND ----------------------------------------------- #
    brand_params = [("https://www.hepsiburada.com/ara?q=bilgisayar&markalar=asus","asus"),
              ("https://www.hepsiburada.com/ara?q=çanta&markalar=mango","mango"),
              ("https://www.hepsiburada.com/ara?q=kalem","zig"),
              ("https://www.hepsiburada.com/ara?q=telefon&markalar=apple","apple"),
              ("https://www.hepsiburada.com/ara?q=bisiklet&markalar=salcano","salcano")]
    
    @parameterized.expand(brand_params)
    def test_product_brands(self,url,brand):
        product_names = filteringLib.get_products(url)

        for product_name in product_names:
            self.assertIn(brand, product_name.lower(), f"Bu ürün {brand} markasına ait değil: {product_name}")
            
    
#----------------------------------------------- TYPE ----------------------------------------------- #

    def test_pencil_type(self):
        url = "https://www.hepsiburada.com/ara?q=kalem&filtreler=MainCategory.Id:21037855"
        product_names = filteringLib.get_products(url)
        for product_name in product_names:
            self.assertIn("tükenmez", product_name.lower(), f"Bu ürün Tükenmez kalem değildir: {product_name}")
            
    def test_bicycle_type(self):
        url = "https://www.hepsiburada.com/ara?q=bisiklet&filtreler=MainCategory.Id:353125"
        product_names = filteringLib.get_products(url)
        for product_name in product_names:
            self.assertIn("dağ bisikleti", product_name.lower(), f"Bu ürün Dağ Bisikleti değildir: {product_name}")
            
    def test_bag_type(self):
        url = "https://www.hepsiburada.com/ara?q=çanta&filtreler=MainCategory.Id:60003897"
        product_names = filteringLib.get_products(url)
        for product_name in product_names:
            self.assertIn("el çantası", product_name.lower(), f"Bu ürün El çantası değildir: {product_name}")
            
    def test_carTire_type(self):
        url = "https://www.hepsiburada.com/oto-lastikler-c-259720?filtreler=mevsim:Yaz"
        product_names = filteringLib.get_products(url)
        for product_name in product_names:
            self.assertIn("yaz", product_name.lower(), f"Bu ürün yaz lastiği değildir: {product_name}")
            
    def test_bulb_type(self):
        url = "https://www.hepsiburada.com/ampuller-c-13003202?filtreler=ampulcinsi:LED"
        product_names = filteringLib.get_products(url)
        for product_name in product_names:
            self.assertIn("led", product_name.lower(), f"Bu ürün led bulb değildir: {product_name}")
    
#----------------------------------------------- PRICE ----------------------------------------------- #

    price_params = [("https://www.hepsiburada.com/ara?q=bilgisayar&filtreler=fiyat:14300-42400",14300,42400),
              ("https://www.hepsiburada.com/ara?q=telefon&filtreler=fiyat:87900-99500",87900,99500),
              ("https://www.hepsiburada.com/ara?q=çanta&filtreler=fiyat:6400-32700",6400,32700),
              ("https://www.hepsiburada.com/ara?q=kalem&filtreler=fiyat:0-1100",0,1100),
              ("https://www.hepsiburada.com/ara?q=bisiklet&filtreler=fiyat:39900-97500",39900,97500)]
    
    @parameterized.expand(price_params)
    def test_prices_within_range(self,url,min,max):
    
        prices = filteringLib.get_prices(url)
        prices_within_range = all(min <= price <= max for price in prices)
        self.assertTrue(prices_within_range, "Tüm ürünlerin fiyatları istenilen aralıkta değil.")
        
    # def test_rating_filter(self):
    #     url = "https://www.hepsiburada.com/ara?q=bilgisayar&puan=4-max"
    #     driver =  webdriver.Firefox()
    #     ratings = sortLib.get_ratings(url,"Hepsiburada",driver)
    #     print(ratings)
    #     rating_with_in_range = all(4 <= rating <= 5 for rating in ratings)
    #     self.assertTrue(rating_with_in_range, "Tüm ürünlerin fiyatları istenilen aralıkta değil.")

            
if __name__ == "__main__":
    unittest.main()
