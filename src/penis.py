from re import sub
from turtle import title
from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get(r"https://www.hepsiburada.com/monster-abra-a5-v20-4-2-intel-core-i5-12450h-32-gb-ram-1-tb-ssd-6-gb-rtx-4050-freedos-15-6-fhd-144-hz-oyun-bilgisayari-pm-HBC00004WGDRF")


driver.execute_script('window.scrollBy(0, 500)')
WebDriverWait(driver, 10).until(EC.presence_of_element_located(
    (By.XPATH, "//button[@id='onetrust-accept-btn-handler']")))
button = driver.find_element(By.XPATH, "//button[@id='addToCart']")
button.click()
print(button)
