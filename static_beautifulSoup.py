import requests
from bs4 import BeautifulSoup
import time

start_time = time.time()

url = "https://quotes.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

print(soup.title.text)
quotes = soup.find_all("span", class_="text")
for quote in quotes:
    print(quote.text)

end_time = time.time()
print(f"\n BeautifulSoup Execution Time: {end_time - start_time:.2f} seconds")
