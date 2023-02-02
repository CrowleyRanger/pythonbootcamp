from bs4 import BeautifulSoup
import requests
from requests.models import LocationParseError

response = requests.get("https://news.ycombinator.com/news")
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
articles = soup.find_all(name="a", class_="storylink")

article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.get_text()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [int(score.get_text().split()[0]) for score in soup.find_all(name="span", class_="score")]

highest_score = max(article_upvotes)
largest_index = article_upvotes.index(highest_score)

print(f"""\n=== Article with more upvotes ===

ARTICLE: {article_texts[largest_index]}
LINK: {article_links[largest_index]}
UPVOTES: {highest_score}
""")

# with open("website.html", encoding="utf8") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, "html.parser")

# all_anchor_tags = soup.find_all(name="a")

# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# # print(heading)

# h3_section_heading = soup.find(name="h3", class_="heading")
# print(h3_section_heading)

# name = soup.select_one(selector="#name")
# print(name)

# headings = soup.select(".heading")