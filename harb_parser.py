import requests
from bs4 import BeautifulSoup

def title_viewing_article(url, headers):
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    response.unicoding = "utf-8"
    soup = BeautifulSoup(response.text, "html.parser")
    articles_list = soup.find("div", class_="tm-articles-list")
    articles = articles_list.find_all("article", class_="tm-articles-list__item")
    cnt = 0
    list = []
    for article in articles:
        cnt += 1
        title = article.select_one("h2.tm-title.tm-title_h2 a span").get_text(strip=True)
        viewing = article.select_one(".reach-counter .tm-icon-counter__value").get_text(strip=True)
        info = (f"{cnt}. {title}... | Просмотры: {viewing}")
        list.append(info)
    return list

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 YaBrowser/25.10.0.0 Safari/537.36"}
url = "https://habr.com/ru/articles/top/daily/"

if __name__ == "__main__":
    list_articles = title_viewing_article(url, headers)
    for element in list_articles:
        print(element)
