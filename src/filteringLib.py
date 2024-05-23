from re import sub
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def get_asus_products(url):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # Hepsiburada sayfasına gidin
    url = "https://www.hepsiburada.com/ara?q=bilgisayar&markalar=asus"
    driver.get(url)
    # Sayfanın tamamen yüklenmesi için biraz bekleyin
    time.sleep(5)
    # Ürünlerin marka adlarını içeren elementleri bulun
    products = driver.find_elements(By.XPATH, "//div[@class='product-list']//h3[@data-test-id='product-card-name']")
    product_names = [product.text.lower() for product in products]
    driver.quit()
    return product_names

def get_prices(url):
    driver = webdriver.Chrome()
    # Hepsiburada sitesini ziyaret et
    driver.get(url)
    # Ürünlerin fiyatlarını kontrol et
    price_divs = driver.find_elements(By.XPATH, "//div[@class='product-list']//div[@data-test-id='price-current-price']")
    prices = list(map(lambda x: int(sub("\D+", "", x.text)[0:-2]), price_divs))
    return prices



if __name__ == "__main__":
    url = "https://www.hepsiburada.com/ara?q=bilgisayar&markalar=asus"
    asus_products = get_asus_products(url)
    for product_name in asus_products:
        if "asus" in product_name:
            print(f"Ürün Asus markasına ait: {product_name}")
        else:
            print(f"Bu ürün Asus markasına ait değil: {product_name}")
