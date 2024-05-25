from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# WebDriver'ı başlat
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Hepsiburada'da arama sonuçları sayfasına git
driver.get('https://www.hepsiburada.com/ara?q=bilgisayar&puan=4-max')

# Sayfanın yüklenmesini beklemek için uyku zamanı
time.sleep(5)

# Ürünlerin olduğu listeyi bul
product_containers = driver.find_elements(By.XPATH, "//div[@class='product-list']//ul[@data-baseweb='star-rating']/li/div")
print(product_containers)



# WebDriver'ı kapat
driver.quit()
