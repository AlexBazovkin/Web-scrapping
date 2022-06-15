import requests
from bs4 import BeautifulSoup as BS
from fake_headers import Headers
from pprint import pprint


if __name__ == "__main__":

# Generate fake headers
    HEADER = Headers(
        browser="chrome",
        os="win",
        headers=True
    ).generate()

url = "https://habr.com/ru/all/"
KEYWORDS = ['дизайн', 'фото', 'web', 'python']




res = requests.get(url, headers=HEADER)
soup = BS(res.text, features='html.parser')
articles = soup.find_all(class_="tm-article-snippet")

for article in articles:
    for keyword in KEYWORDS:
        if keyword.lower() in article.text.lower():
            published = article.find(class_="tm-article-snippet__datetime-published").text
            header = article.find(class_="tm-article-snippet__title tm-article-snippet__title_h2").text
            link = article.find(class_="tm-article-snippet__title-link").attrs["href"]
            art_url = url + link
            print(f'{published} - {header} - {art_url}')