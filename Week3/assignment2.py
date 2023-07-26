from bs4 import BeautifulSoup
import requests
from pprint import pprint
import os
import csv
def get_articles_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    articles = soup.find_all("div", class_="r-ent")
    article_data = {}
    # 用字典處理會比較容易，列表不好控制值
    for article in articles:
        title = article.find("div", class_="title").text.strip()
        rate = article.find("div", class_="nrec").text.strip()
        date = article.find("div", class_="date").text.strip()
        article_dict = {"title": title, "rate": rate, "date": date}
        article_data[title] = article_dict

    return article_data

base_url = "https://www.ptt.cc/bbs/movie/index.html"

# Get data from the first page
response = requests.get(base_url)
soup = BeautifulSoup(response.text, "html.parser")
prev_page_link = soup.find("a", string="‹ 上頁")["href"]
page_index = int(prev_page_link[prev_page_link.index("index") + len("index"):prev_page_link.index(".html")])

article_data = get_articles_data(base_url)

# Get data from the previous three pages
for i in range(3):
    page_index -= 1
    prev_page_url = f"https://www.ptt.cc/bbs/movie/index{page_index}.html"
    article_data.update(get_articles_data(prev_page_url))#list時或是用+=類似extend
pprint(article_data)
print(article_data)
print(len(article_data))

output_file = "Week3/movies.csv"
fields=["title","rate","date"]
if not os.path.exists(output_file):
    with open(output_file, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        for item in article_data.values():
            writer.writerow(item)
    print("movies.csv finished")
else:
    print("movies.csv exists")        