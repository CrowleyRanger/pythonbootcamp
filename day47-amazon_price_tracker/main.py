from bs4 import BeautifulSoup
import requests

wanted_price = 150.00
url = "https://www.amazon.com.br/dp/150672163X/?coliid=I2O1QR1O8AYKSK&colid=1OO4EK09B6SCR&psc=1&ref_=lv_ov_lig_dp_it"

response = requests.get(url)
text = response.text
soup = BeautifulSoup(response.text, 'html.parser')

price = soup.find(id="price").get_text()
price_float = float(price.split("$")[1])


if wanted_price <= price_float:
    print("The product you wanted at Amazon.com is at a price you wished for!")
else:
    print("Not yet amigo")

print("Working with APIs is a pain in the ass for sure!")
print(price)