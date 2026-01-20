import os

import requests
from bs4 import BeautifulSoup


def get_article_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    links = []
    # 假设文章链接在<a>标签中，指向/essay/路径
    for a in soup.find_all('a', href=True):
        if '/essay/' in a['href']:
            full_url = 'http://yangqinyuan.com' + a['href'] if a[
                'href'].startswith('/') else a['href']
            if full_url not in links:
                links.append(full_url)
    return links


def scrape_article(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    # 标题
    title = soup.find('h1')
    title_text = title.get_text().strip() if title else "无标题"

    # 获取整个body文本
    body_text = soup.body.get_text(separator='\n',
                                   strip=True) if soup.body else ""

    # 找到标题后的内容
    if title_text in body_text:
        start = body_text.find(title_text) + len(title_text)
        # 找到"Written on"或类似结束标记
        end_markers = ["Written on", "杨钦元 | 博客", "故事", "随笔"]
        end = len(body_text)
        for marker in end_markers:
            pos = body_text.find(marker, start)
            if pos != -1:
                end = min(end, pos)
        content_text = body_text[start:end].strip()
    else:
        content_text = "内容未找到"

    return f"# {title_text}\n\n{content_text}\n\n---\n\n"


# 已知文章链接（从主页提取）
article_urls = [
    'http://yangqinyuan.com/essay/tzcl.html',
    'http://yangqinyuan.com/essay/zongjie.html',
    'http://yangqinyuan.com/essay/something.html',
    'http://yangqinyuan.com/essay/lqxq.html',
    'http://yangqinyuan.com/essay/sj.html',
    'http://yangqinyuan.com/essay/yywb.html',
    'http://yangqinyuan.com/essay/yl.html',
    'http://yangqinyuan.com/essay/shpy.html',
    'http://yangqinyuan.com/essay/tl.html',
    'http://yangqinyuan.com/essay/tlgl.html',
    'http://yangqinyuan.com/essay/sd.html',
    'http://yangqinyuan.com/essay/tl.html',
    'http://yangqinyuan.com/essay/qp.html',
    'http://yangqinyuan.com/essay/sgg.html',
    'http://yangqinyuan.com/essay/fhjb.html',
    'http://yangqinyuan.com/essay/fri.html',
    'http://yangqinyuan.com/essay/rh.html',
    'http://yangqinyuan.com/essay/mz.html',
    'http://yangqinyuan.com/essay/yq.html',
    'http://yangqinyuan.com/essay/sc.html',
    'http://yangqinyuan.com/essay/qx.html',
    'http://yangqinyuan.com/essay/mhsx.html',
    'http://yangqinyuan.com/essay/ssgd.html',
    'http://yangqinyuan.com/essay/xd.html',
    'http://yangqinyuan.com/essay/jl.html',
    'http://yangqinyuan.com/essay/fxgd.html',
    'http://yangqinyuan.com/essay/yq.html',
    'http://yangqinyuan.com/essay/chaos.html',
    'http://yangqinyuan.com/essay/dx.html',
    'http://yangqinyuan.com/essay/dmdy.html',
    'http://yangqinyuan.com/essay/xtxfx.html',
    'http://yangqinyuan.com/essay/fs.html',
    'http://yangqinyuan.com/essay/hf.html',
    'http://yangqinyuan.com/essay/jojo.html',
    'http://yangqinyuan.com/essay/learnfromeverything.html',
    'http://yangqinyuan.com/essay/fs.html',
    'http://yangqinyuan.com/essay/xde.html',
    'http://yangqinyuan.com/essay/star.html',
    'http://yangqinyuan.com/essay/shit.html',
    'http://yangqinyuan.com/essay/fsx.html',
    'http://yangqinyuan.com/essay/youmo.html',
    'http://yangqinyuan.com/essay/sch.html',
    'http://yangqinyuan.com/essay/merrychris.html',
    'http://yangqinyuan.com/essay/hole.html',
    'http://yangqinyuan.com/essay/show-up.html',
    'http://yangqinyuan.com/essay/platform.html',
    'http://yangqinyuan.com/essay/diaocha.html',
    'http://yangqinyuan.com/essay/yama.html',
    'http://yangqinyuan.com/essay/cost02.html',
    'http://yangqinyuan.com/essay/lashen.html',
    'http://yangqinyuan.com/essay/ljyl.html',
    'http://yangqinyuan.com/essay/travel.html',
    'http://yangqinyuan.com/essay/gives.html',
    'http://yangqinyuan.com/essay/beidong.html',
    'http://yangqinyuan.com/essay/fengkong.html',
    'http://yangqinyuan.com/essay/insure.html',
    'http://yangqinyuan.com/essay/didi.html',
    'http://yangqinyuan.com/essay/turtle.html',
    'http://yangqinyuan.com/essay/invest.html',
    'http://yangqinyuan.com/essay/wind.html',
    'http://yangqinyuan.com/essay/face-and-cost.html',
    'http://yangqinyuan.com/essay/cost.html',
    'http://yangqinyuan.com/essay/trust.html',
    'http://yangqinyuan.com/essay/play.html',
    'http://yangqinyuan.com/essay/bitcon.html',
    'http://yangqinyuan.com/essay/net02.html',
    'http://yangqinyuan.com/essay/simple.html',
    'http://yangqinyuan.com/essay/change.html',
    'http://yangqinyuan.com/essay/brain01.html',
    'http://yangqinyuan.com/essay/be-flower.html',
    'http://yangqinyuan.com/essay/gym.html',
    'http://yangqinyuan.com/essay/self-identity.html',
    'http://yangqinyuan.com/essay/emotion.html',
    'http://yangqinyuan.com/essay/batna.html',
    'http://yangqinyuan.com/essay/gaotie.html',
    'http://yangqinyuan.com/essay/find-fav-job.html',
    'http://yangqinyuan.com/essay/oldman.html',
    'http://yangqinyuan.com/essay/about-pm.html',
    'http://yangqinyuan.com/essay/positive-sum-game.html',
    'http://yangqinyuan.com/essay/sports.html',
    'http://yangqinyuan.com/essay/flow.html',
    'http://yangqinyuan.com/essay/re.html'
]
all_content = ""
for url in article_urls:
    article_content = scrape_article(url)
    all_content += article_content

# 保存为Markdown文件
with open("blog_content.md", "w", encoding="utf-8") as f:
    f.write(all_content)

print("博客内容已保存到 blog_content.md")
