import requests
from bs4 import BeautifulSoup
import sys

def get_all_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    links = []
    for a in soup.find_all('a', href=True):
        full_url = a['href']
        if not full_url.startswith('http'):
            full_url = 'http://yangqinyuan.com' + full_url if full_url.startswith('/') else url + '/' + full_url
        links.append(full_url)
    return links

# 目标URL
url = "http://yangqinyuan.com/menu/essay.html"
all_links = get_all_links(url)

# print("网页中的所有链接：")
# for link in all_links:
#     print(link)

# sys.exit(0)

# 保存为Markdown文件
with open("get_links.md", "w", encoding="utf-8") as f:
    f.write(str(all_links) )
