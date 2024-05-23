from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# Hepsiburada sitesine gidin
driver.get("https://www.hepsiburada.com/ara?q=bilgisayar&puan=4-max")

# Ürünlerin bulunduğu alanı seçme
products = driver.find_elements(By.XPATH, "//div[@class='product-list']//div[@data-test-id='review']")
print(products)
# Her ürün için kontrol yapma
for product in products:
    # Ürünün puanını alma
    stars_element = product.find_element(By.XPATH, ".//span[contains(@class, 'ratings')]/span")
    stars = float(stars_element.get_attribute("title").split()[0])  # Puanı ondalık sayıya dönüştürme

    # Puan kontrolü
    if stars >= 4:
        print("Ürünün puanı 4 ve üzeri:", product.text)
    else:
        print("Ürünün puanı 4 ve altı:", product.text)

# Tarayıcıyı kapatma
driver.quit()
