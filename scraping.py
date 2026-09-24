import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article", class_="product_pod")

with open("scraped_books.txt", "w", encoding="utf-8") as file:
    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text

        file.write(f"{title} - {price}\n")
        print(title, "-", price)

print("Klart! Datan har sparats i scraped_books.txt")