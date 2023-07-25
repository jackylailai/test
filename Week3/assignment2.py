from bs4 import BeautifulSoup
import requests
from pprint import pprint

url="https://www.ptt.cc/bbs/movie/index.html"
# 發送請求並取得響應
response = requests.get(url)
# 解析 HTML 內容
soup = BeautifulSoup(response.text, 'html.parser')
# 找到所有文章的元素
articles = soup.find_all('div', class_='r-ent')

# 儲存文章資訊的列表
article_data = []

for article in articles:
    # 文章標題
    title = article.find('div', class_='title').text.strip()
    # 推文數量
    rate = article.find('div', class_='nrec').text.strip()
    # 發佈時間
    date = article.find('div', class_='date').text.strip()
    article_data.append(f"{title},{rate},{date}")
pprint(article_data)