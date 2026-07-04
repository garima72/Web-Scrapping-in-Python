

import requests
from bs4 import BeautifulSoup
import os




urls = [
    "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html",
    "https://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html"
]

target_price = 50


for url in urls:
    print("=" * 50)

    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.find("h1").text

    
    price = soup.find("p", class_="price_color").text


    image = soup.find("img")["src"]
    image_url = "https://books.toscrape.com/" + image.replace("../", "")

    
    img_response = requests.get(image_url)

    
    filename = title.replace(" ", "_").replace("/", "_") + ".jpg"

    with open(f"images/{filename}", "wb") as file:
        file.write(img_response.content)

    
    price_value = float(price.replace("£", "").replace("Â", "").strip())
    print("Title :", title)
    print("Price :", price)
    print("Image URL :", image_url)
    print("Image Downloaded Successfully!")

    if price_value <= target_price:
        print("Price Comparison : Good Deal!")
    else:
        print("Price Comparison : Too Expensive! ")