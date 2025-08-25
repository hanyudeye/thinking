# 代码执行环节
def main(start_date: str, end_date: str, text: list) -> dict:
    import csv, io, json
    from datetime import datetime

    # 连接文本行
    content = "\n".join(text)
    reader = csv.DictReader(io.StringIO(content), delimiter='|')

    sd = datetime.strptime(start_date, "%Y-%m-%d").date()
    ed = datetime.strptime(end_date,   "%Y-%m-%d").date()

    total_rows = 0
    filtered = []

    for row in reader:
        total_rows += 1

        # 清洗字段名可能含空格
        ct_raw = row.get("创建时间") or row.get(" 创建时间 ") or ""
        ct_raw = ct_raw.strip()
        if not ct_raw:
            continue

        # 解析多种时间格式
        ct = None
        for fmt in ("%Y/%m/%d %H:%M", "%Y-%m-%d %H:%M",
                    "%Y/%m/%d %H:%M:%S", "%Y-%m-%d %H:%M:%S"):
            try:
                ct = datetime.strptime(ct_raw, fmt)
                break
            except:
                pass
        if not ct:
            continue

        # 筛选时间范围
        if sd <= ct.date() <= ed:
            filtered.append(row)

    output = {
        "total_rows": total_rows,
        "total_filtered": len(filtered),
        "filtered": filtered
    }

    return {"result": json.dumps(output, ensure_ascii=False)}

