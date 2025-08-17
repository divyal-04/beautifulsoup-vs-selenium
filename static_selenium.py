from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

start_time = time.time()

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://quotes.toscrape.com/")
time.sleep(2)

quotes = driver.find_elements(By.CLASS_NAME, "text")
for quote in quotes:
    print(quote.text)

driver.quit()

end_time = time.time()
print(f"\n Selenium Execution Time: {end_time - start_time:.2f} seconds")
