import re

input_file = "资讯阅读/rss,安全类订阅，英文.xml"
# input_file = "资讯阅读/a.xml"
output_file = "资讯阅读/rss_blogs.md"


# with open("资讯阅读/rss,安全类订阅，英文.xml", encoding="utf-8") as f:
with open(input_file, encoding="utf-8") as f:
    content = f.read()

# 匹配所有 outline 标签的 title 和 htmlUrl
matches = re.findall(r'title="([^"]+)"[^>]*htmlUrl="([^"]+)"', content)
# 去重
unique = {}
for title, url in matches:
    unique[url] = title

# 输出 md 格式
# for url, title in sorted(unique.items()):
    # print(f"- [{title}]({url})")

with open(output_file, "w", encoding="utf-8") as f:
    for url, title in sorted(unique.items(), key=lambda x: x[1].lower()):
        f.write(f"- [{title}]({url})\n")

print(f"已写入 {len(unique)} 个博客链接到 {output_file}")