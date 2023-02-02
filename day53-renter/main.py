from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time

FORMS_LINK = "https://forms.gle/9T7TKcQXsZS8tn339"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0",
    "Accept-Language": "en-US,en;q=0.5"
}

response = requests.get("https://www.zillow.com/homes/for_rent/", headers=header)

website_html = response.text
soup = BeautifulSoup(website_html, 'html.parser')

link_list = []
link_elements = soup.select(".list-card-top a")
for link in link_elements:
    href = link["href"]
    if "href" not in href:
        link_list.append(f"https://www.zillow.com{href}")
    else:
        link_list.append(href)

address_elements = soup.select(".list-card-info address")
address_list = [address.get_text().split(" | ")[-1] for address in address_elements]

price_elements = soup.select(".list-card-info .list-card-price")
price_list = [price.get_text() for price in price_elements]

print(address_list)
print(price_list)

WEBDRIVER_PATH = "C:/Users/Mr.Nachos/Desktop/Courses/...Udemy/100 Days of Python/webdriver/geckodriver.exe"
driver = webdriver.Firefox(executable_path=WEBDRIVER_PATH)

for n in range(len(link_list)):
    driver.get(FORMS_LINK)
    time.sleep(5)

    address = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div')

    address.send_keys(address_list[n])
    price.send_keys(price_list[n])
    link.send_keys(link_list[n])
    submit_button.click()