from bs4 import BeautifulSoup
import requests
from pprint import pprint
import os
import csv

def get_article_detail(url):#為了取得時間，必須先進入網頁在爬取當下標題的時間
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    time_element = soup.find_all("span", class_="article-meta-value")  # 找到包含完整時間的元素
    if time_element:
        return time_element[3].text.strip()
    else:
        return ""
def get_articles_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    articles = soup.find_all("div", class_="r-ent")#出來會是一團數據含有r-ent
    article_data = {}

    #用字典處理會比較容易，列表不好控制值
    #跑迴圈一一取出，如需要更深入的內容就繼續往下.find
    for article in articles:
        title_element = article.find("div", class_="title")
        if not title_element.a:  # 如果沒有超連結，跳過該篇文章
            continue
        
        title = title_element.text.strip()
        rate = article.find("div", class_="nrec").text.strip()
        article_url = "https://www.ptt.cc" + article.find("div", class_="title").a["href"]
        #以上取的方式也可以使用持續使用.find再利用屬性[""]，或是整理成一行
        #文章的時間卡在文章網頁裡頭，先透過func取的時間
        date = get_article_detail(article_url)#date的數據內容透過上面func幫我處理
        article_dict = {"title": title, "rate": rate, "date": date}
        article_data[title] = article_dict

    return article_data

base_url = "https://www.ptt.cc/bbs/movie/index.html"

# 先抓第一頁的東西及可以推演的內容
response = requests.get(base_url)
soup = BeautifulSoup(response.text, "html.parser")
prev_page_link = soup.find("a", string="‹ 上頁")["href"]#使用 ["href"] 就是從 <a> 元素中提取 href 屬性的值
page_index = int(prev_page_link[prev_page_link.index("index") + len("index"):prev_page_link.index(".html")])
#先抓index字的索引值然後針對字串[:]索引某數到某數，會求得一組index數字例如9640
article_data = get_articles_data(base_url)

# 拿可以推演的內容反推索引要更改的值依序扣一
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

output_file2= "Week3/movie.txt"
if not os.path.exists(output_file2):
    with open(output_file2, "w") as file:
        for value in article_data.values():
            line = f"{value['title']},{value['rate']},{value['date']}\n"
            file.write(line)
    print("movie.txt finished")
else:
    print("movie.txt exists")