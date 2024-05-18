import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
}
data = requests.get("https://www.melon.com/chart/", headers=headers)

soup = BeautifulSoup(data.text, "html.parser")

# print(soup)

lst50 = soup.select(
    "#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a "
)

lst100 = soup.select(
    "#lst100 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a "
)

for e in lst50 + lst100:
    print(e["title"])
