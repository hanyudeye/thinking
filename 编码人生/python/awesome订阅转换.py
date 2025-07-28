import re

input_file = "资讯阅读/awesome-rss-feed.md"
output_file = "资讯阅读/awesome-rss-feed-with-protocol.md"

def add_https(domain):
    domain = domain.strip()
    if not domain or domain.startswith("http"):
        return domain
    return f"https://{domain}"

with open(input_file, encoding="utf-8") as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    # 只处理表格行（含有 | 并且有 Domain 列）
    if re.match(r"\\|.*\\|.*\\|.*\\|", line):
        parts = line.strip().split("|")
        if len(parts) >= 4:
            domain = parts[-2].strip()
            # 跳过表头
            if domain.lower() == "domain":
                new_lines.append(line)
                continue
            # 替换
            parts[-2] = " " + add_https(domain) + " "
            new_line = "|".join(parts)
            new_lines.append(new_line + "\n")
        else:
            new_lines.append(line)
    else:
        new_lines.append(line)

with open(output_file, "w", encoding="utf-8") as f:
    f.writelines(new_lines)

print(f"已处理并写入到 {output_file}")